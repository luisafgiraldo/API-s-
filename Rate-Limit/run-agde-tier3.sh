#!/bin/bash

API_KEY=cXVsN2t2eDNyYnN1M2EwdHRqeXp1OkFQeUpQa1Y4Y3hucXBDaWpFbHBJdlYzWXJsakRndG1K
PARALLEL_REQUESTS=60
TOTAL_REQUESTS=180

LOG_FILE="request_log.txt"
COUNTER_200=0
COUNTER_429=0
COUNTER_OTHER=0

# Reiniciar log si existe
echo "Starting request log - $(date)" > "$LOG_FILE"

process_request() {
  local i=$1
  start_time=$(date +%s.%N)
  status_code=$(curl -X 'POST' \
    'https://api.va.staging.landing.ai/v1/tools/agentic-document-analysis' \
    -H "Authorization: Basic $API_KEY" \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'image=@./simple-table.png;' -s -o /dev/null -w "%{http_code}")

  end_time=$(date +%s.%N)
  elapsed_time=$(echo "$end_time - $start_time" | bc)

  # Log por cada request
  {
    echo "Request $i:"
    echo "Status Code: $status_code"
    echo "Elapsed Time: ${elapsed_time}s"
    echo "------------------------------"
  } >> "$LOG_FILE"

  # Incrementar contadores (en archivo temporal para procesos concurrentes)
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

for ((i=1; i<=TOTAL_REQUESTS; i++)); do
  process_request $i &
  if (( i % PARALLEL_REQUESTS == 0 )) || (( i == TOTAL_REQUESTS )); then
    wait
  fi
done

# Procesar resultados
COUNTER_200=$(grep -c '^200$' .status_temp)
COUNTER_429=$(grep -c '^429$' .status_temp)
COUNTER_OTHER=$(grep -c '^OTHER$' .status_temp)

# Agregar resumen al final del log
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

