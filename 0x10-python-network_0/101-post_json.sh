#!/bin/bash
# Send a json POST request
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
