#!/usr/bin/bash

source_file="turbot.py"
output_file=$(echo $source_file | cut -d'.' -f 1)

cp $source_file $output_file
chmod +x $output_file

echo "done!"