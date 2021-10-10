#!/usr/bin/bash

echo "installing turbot..."

source_file="turbot.py"
output_file=$(echo $source_file | cut -d'.' -f 1)

cp $source_file $output_file
if [ $? != 0 ]
then
	echo "failed to copy turbot script"
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

man_page="turbot.1"

sudo cp $man_page /usr/share/man/man1/
if [ $? != 0 ]
then
	echo "failed to copy turbot man page"
	exit $?
fi

sudo mandb
if [ $? != 0 ]
then
	echo "failed to update MAN database"
	exit $?
fi

echo "you have successfully installed turbot!"

