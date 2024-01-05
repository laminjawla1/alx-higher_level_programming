#!/bin/bash
# Displays the status code of a response
curl -sI "$1" | grep "HTTP" | cut -d " " -f2
