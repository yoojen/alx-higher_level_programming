#!/bin/bash
#show allow
curl -s "$1" -X OPTIONS | grep "Allow:" | cut -c 8-
