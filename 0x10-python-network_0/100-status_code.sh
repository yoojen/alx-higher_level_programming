#!/bin/bash
#curl site without using pipe
curl -so /dev/null --write-out "%{http_code}" "$1"
