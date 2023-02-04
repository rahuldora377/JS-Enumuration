#!/bin/bash

file="$1"

while read url; do
    gau $url | grep '.js$' | httpx -silent '
done < "$file"
#script.sh filename
