#!/bin/bash

file="$1"

while read url; do
    gau $url |  httpx -silent | grep '.js$'
done < "$file"
#script.sh filename
