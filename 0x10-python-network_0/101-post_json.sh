#!/bin/bash
#  send post requst with json file
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
