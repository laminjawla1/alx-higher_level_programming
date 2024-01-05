#!/bin/bash
# Curl a site and print the Content-Length
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
