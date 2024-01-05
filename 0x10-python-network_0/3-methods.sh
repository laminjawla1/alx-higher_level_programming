#!/bin/bash
# This script curl a site a list all the vailable http request methods
curl -sI "$1" | grep "Allow" | cut -d " " -f2
