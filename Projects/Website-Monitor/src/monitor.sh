#!/bin/bash
cd /app

# Use environment variable if set, otherwise use defaults
SITES=${SITES:-"https://google.com,https://github.com,https://abcxyz123.com"}

# Split comma-separated string into array
IFS=',' read -ra websites <<< "$SITES"

for website in "${websites[@]}"
do
    response=$(curl -L -o /dev/null -s -w "%{http_code} %{url_effective}" "$website")
    code=$(echo $response | awk '{print $1}')
    final_url=$(echo $response | awk '{print $2}')

    if [[ "$final_url" == *"${website#https://}"* && "$code" =~ ^2 ]]
    then
        echo "[$(date)] STATUS=UP SITE=$website CODE=$code" >> /app/logs/status.log
    else
        echo "[$(date)] STATUS=DOWN SITE=$website CODE=$code REDIRECT=$final_url" >> /app/logs/status.log
    fi
done
