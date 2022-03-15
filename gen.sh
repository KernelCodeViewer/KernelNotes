#!/usr/bin/env bash

VERSION=$1
FILE=$2
LINE=$3
NOTE=$4

usage()
{
	echo "Usage: $0  <version> <file> <line> <note>"
	echo ""
	echo "For Example:"
	echo "    $0  v5.10 kernel/watchdog.c 703  \"blabla\""
}

if [ $# -ne 4 ];
then
	usage
	exit
fi

file=${VERSION}/${FILE}.json

if [ ! -f ${file} ]; then
	echo "Create" $file
	mkdir -p  `dirname $file`
	./addNotes.py --line $LINE --create  --file $VERSION/$FILE --note "$NOTE"
else
	echo "Update" $file
	./addNotes.py --line $LINE --file $VERSION/$FILE  --note "$NOTE"
	mv $file.new $file
fi
