#!/bin/bash

API_KEY="eXpqM2lvN21hb2xrc28wZDA4b2NuOndtbmlRdlRTQ1VOT0FhTUhTWXJWZFpIUk9ZaGFXYk9o"
PARALLEL_REQUESTS=100
TOTAL_REQUESTS=100
STATUS_LOG="status_codes.log"
OUTPUT_FILE="goodimg-parallelreq/reports/ADE-T3_goodimg_report.txt"
TEMP_REPORT="temp_report.txt"

# Ensure the log and output files are empty
> "$STATUS_LOG"
> "$OUTPUT_FILE"
> "$TEMP_REPORT"

process_request() {
  local i=$1
  local request_log="request_${i}_log.tmp"
  echo "Request $i: start" > "$request_log"
  start_time=$(date +%s.%N)
  response=$(curl -X 'POST' \
    'https://api.va.staging.landing.ai/v1/tools/agentic-document-analysis' \
    -H "Authorization: Basic $API_KEY" \
    -H 'accept: application/json' \
    -H 'Content-Type: multipart/form-data' \
    -F 'image=@./goodimg-parallelreq/ag-de/small-img.png;' -s -w "%{http_code}\n" -o /dev/null)
  echo "$response" >> "$STATUS_LOG"
  end_time=$(date +%s.%N)
  elapsed_time=$(echo "$end_time - $start_time" | bc)
  
  echo "Request $i: end Status Code: $response ($elapsed_time seconds)" >> "$request_log"
  cat "$request_log" | tee -a "$OUTPUT_FILE"
  rm "$request_log"  # Clean up temporary log file
}

export -f process_request
export API_KEY
export STATUS_LOG
export OUTPUT_FILE

# Capture the start time of the test
test_start_time=$(date +%s.%N)

for ((i=1; i<=TOTAL_REQUESTS; i++)); do
  (process_request $i) &

  if (( i % PARALLEL_REQUESTS == 0 )) || (( i == TOTAL_REQUESTS )); then
    wait
  fi
done

# Assert no unwanted status codes were received
unwanted_codes=$(awk '!/200|429/' "$STATUS_LOG" | wc -l)
if [ "$unwanted_codes" -gt 0 ]; then
    echo "Test failed: Unwanted status codes detected."
    exit 1
fi

# Capture the end time of the test
test_end_time=$(date +%s.%N)

{
    echo -e "--------------------------------\nADE-T3-GOOD_IMG_TEST-Report:"
    awk '{count[$1]++} END {for (code in count) print "Count of " code " responses: " count[code]}' "$STATUS_LOG"
    test_duration=$(echo "$test_end_time - $test_start_time" | bc)
    echo "Total test duration: $test_duration seconds"
    echo "--------------------------------"
    echo ""
} | tee "$TEMP_REPORT"

cat "$TEMP_REPORT" "$OUTPUT_FILE" > temp && mv temp "$OUTPUT_FILE"
rm "$TEMP_REPORT"