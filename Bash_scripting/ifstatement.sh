#!/bin/bash #Shebang optional

echo "enter a number"
read num

if [ $num -gt 0 ];then # the spaces are very important
	echo "$num greater than zero"
elif [ $num -lt 0 ];then
	echo "$num less than 0"
else
	echo "$num is 0"
fi

