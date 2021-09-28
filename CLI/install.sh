#!/usr/bin/bash

echo "installing turBOT..."

source_file="turbot.py"
output_file=$(echo $source_file | cut -d'.' -f 1)

cp $source_file $output_file
if [ $? != 0 ]
then
	echo "failed to copy turBOT script"
	exit $?
fi

chmod +x $output_file
if [ $? != 0 ]
then
	echo "failed to set binary as executable"
	exit $?
fi

sudo mv $output_file /usr/bin
if [ $? != 0 ]
then
	echo "failed to install binary to /usr/bin"
	exit $?
fi

echo "you have successfully installed turBOT!"

