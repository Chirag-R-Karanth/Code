#!/bin/bash

echo "Enter a fruit"
read fruit

case $fruit in
"apple")
    echo "Apple"
    ;;
"banana")
    echo "Banana"
    ;;
"orange")
    echo "Orange"
    ;;
*) ;;
esac
