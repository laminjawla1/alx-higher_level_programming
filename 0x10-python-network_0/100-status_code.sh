#!/bin/bash
# Displays the status code of a response
curl -sLw "%{http_code}" -o /dev/null "$1"
