#!/bin/bash

for file in *.rb; do
    if [ -f "$file" ]; then
        chmod +x "$file"
        echo "Made $file executable"
    fi
done
