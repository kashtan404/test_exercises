#!/usr/bin/env bash

docker build -t version.1 .

docker run --rm -e OPENWEATHER_API_KEY="$1" -e CITY_NAME="$2" version.1
