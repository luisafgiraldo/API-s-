#!/bin/bash

API_KEY=M2JxcTRoaW1rdHgyaHpubzZrcGRnOnlmekFzYUxZM05QSTIyaWRpa2xJN0JFaHNOUFV0emxq
PARALLEL_REQUESTS=10
TOTAL_REQUESTS=60

LOG_FILE="request_log_tier1.txt"
COUNTER_200=0
COUNTER_429=0
COUNTER_OTHER=0

# Verificar existencia de la imagen
if [[ ! -f "./simple-table.png" ]]; then
  echo "❌ Imagen simple-table.png no encontrada. Abortando script." > "$LOG_FILE"
  exit 1
fi

# Reiniciar log si existe
echo "📅 Starting request log - $(date)" > "$LOG_FILE"

process_request() {
  local i=$1
  start_time=$(date +%s.%N)

  # Ejecutar request
  response=$(curl -X 'POST' \
    'https://api.va.staging.landing.ai/v1/tools/agentic-document-analysis' \
    -H "Authorization: Basic $API_KEY" \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'image=@./simple-table.png;' \
    -s -w "\nSTATUS_CODE:%{http_code}" 2>> "$LOG_FILE")

  end_time=$(date +%s.%N)
  elapsed_time=$(echo "$end_time - $start_time" | bc)

  # Separar cuerpo y status code
  status_code=$(echo "$response" | grep "STATUS_CODE:" | cut -d':' -f2)
  body=$(echo "$response" | sed '/STATUS_CODE:/d')

  # Log detallado
  {
    echo "[$(date)] Request $i:"
    echo "Status Code: $status_code"
    echo "Elapsed Time: ${elapsed_time}s"
    echo "Response Body:"
    echo "$body"
    echo "------------------------------"
  } >> "$LOG_FILE"

  # Incrementar contadores
  if [[ "$status_code" == "200" ]]; then
    echo "200" >> .status_temp
  elif [[ "$status_code" == "429" ]]; then
    echo "429" >> .status_temp
  else
    echo "OTHER" >> .status_temp
  fi
}

# Eliminar archivo temporal de contadores si existe
rm -f .status_temp

# Ejecutar en paralelo
for ((i=1; i<=TOTAL_REQUESTS; i++)); do
  process_request $i &
  if (( i % PARALLEL_REQUESTS == 0 )) || (( i == TOTAL_REQUESTS )); then
    wait
  fi
done

# Contar resultados
COUNTER_200=$(grep -c '^200$' .status_temp)
COUNTER_429=$(grep -c '^429$' .status_temp)
COUNTER_OTHER=$(grep -c '^OTHER$' .status_temp)

# Resumen final
{
  echo ""
  echo "===== SUMMARY ====="
  echo "Total 200 responses: $COUNTER_200"
  echo "Total 429 responses: $COUNTER_429"
  echo "Total other responses: $COUNTER_OTHER"
  echo "==================="
} >> "$LOG_FILE"

# Limpiar archivo temporal
rm -f .status_temp

echo "✅ Requests completed. Log saved to $LOG_FILE"
