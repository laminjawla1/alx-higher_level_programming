#!/bin/bash
# Send a json POST request
curl -sX POST -d $( cat "$2") -H "Content-Type: application/json" "$1"
