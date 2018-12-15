#!/usr/bin/env bash

docker build -t version.2 .

docker run --rm -e OPENWEATHER_API_KEY="$1" -e CITY_NAME="$2" version.2
