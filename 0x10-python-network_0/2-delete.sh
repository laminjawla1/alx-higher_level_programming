#!/bin/bash
# This script sends a delete request to a site provide
curl -sL "$1" -X DELETE
