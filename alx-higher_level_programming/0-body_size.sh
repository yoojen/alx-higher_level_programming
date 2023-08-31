#!/bin/bash
#get the byte size of http response header
curl -s "$1" | wc -c
