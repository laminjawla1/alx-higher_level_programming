#!/bin/bash
response=$(curl -sI "$1")
echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r'
