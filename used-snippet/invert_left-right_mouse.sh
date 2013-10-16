#!/bin/bash

current=$(xmodmap -pp | head -5 | tail -1 | awk '{print $2}');

if [ "$current" -eq "1" ]
then 
        xmodmap -e "pointer = 3 2 1";
else
        xmodmap -e "pointer = 1 2 3";
fi

#If you want to identify your mouse buttons copy this in a terminal:
xev | grep button
