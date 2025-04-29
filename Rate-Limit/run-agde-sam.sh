#!/bin/bash

API_KEY=M2JxcTRoaW1rdHgyaHpubzZrcGRnOnlmekFzYUxZM05QSTIyaWRpa2xJN0JFaHNOUFV0emxq
PARALLEL_REQUESTS=200
TOTAL_REQUESTS=200

PROMPT="apple"
MODEL="florence2sam2"
IMAGE_FILE="/Users/luisaaristizabal/Documents/API-s-/Rate-Limit/apple.jpg"

# Contadores
COUNTER_200=0
COUNTER_429=0
COUNTER_OTHER=0

process_request() {
  local i=$1
  start_time=$(date +%s.%N)

  response=$(curl -X 'POST' \
    'https://api.va.staging.landing.ai/v1/tools/text-to-instance-segmentation' \
    -H "Authorization: Basic $API_KEY" \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F "image=@$IMAGE_FILE" \
    -F "prompt=$PROMPT" \
    -F "model=$MODEL" \
    -s -w "\nHTTP_STATUS:%{http_code}")

  status_code=$(echo "$response" | grep "HTTP_STATUS" | cut -d':' -f2)
  body=$(echo "$response" | sed '/HTTP_STATUS/d')

  end_time=$(date +%s.%N)
  elapsed_time=$(echo "$end_time - $start_time" | bc)

  echo "Request $i:"
  echo "Status Code: $status_code"
  echo "Elapsed Time: ${elapsed_time}s"
  echo "Response Body: $body"
  echo "------------------------------"

  if [[ "$status_code" == "200" ]]; then
    echo "200" >> .status_temp
  elif [[ "$status_code" == "429" ]]; then
    echo "429" >> .status_temp
  else
    echo "OTHER" >> .status_temp
  fi
}

rm -f .status_temp

for ((i=1; i<=TOTAL_REQUESTS; i++)); do
  process_request $i &
  if (( i % PARALLEL_REQUESTS == 0 )) || (( i == TOTAL_REQUESTS )); then
    wait
  fi
done

wait

COUNTER_200=$(grep -c '^200$' .status_temp)
COUNTER_429=$(grep -c '^429$' .status_temp)
COUNTER_OTHER=$(grep -c '^OTHER$' .status_temp)

echo ""
echo "===== SUMMARY ====="
echo "Total 200 responses: $COUNTER_200"
echo "Total 429 responses: $COUNTER_429"
echo "Total other responses: $COUNTER_OTHER"
echo "==================="

rm -f .status_temp

echo "✅ Requests completed."
