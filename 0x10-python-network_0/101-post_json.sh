#!/bin/bash
# Send a json POST request
curl -s -X POST -d $( cat $"2") "$1"
