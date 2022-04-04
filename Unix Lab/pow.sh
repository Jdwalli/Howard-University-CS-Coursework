#!/bin/bash

if [ $# -eq 2 ] 
then 
    echo $(( $1**$2 ))
else 
    echo "Invalid arguments"
fi
