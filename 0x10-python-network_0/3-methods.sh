#!/bin/bash
# This script curl a site a list all the vailable http request methods
curl -sL "$1" -X OPTIONS
