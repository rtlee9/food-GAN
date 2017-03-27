#!/bin/bash
blacklist="blacklist.txt"
while IFS= read -r file
do
rm imgs/img/$file
done < "$blacklist"
