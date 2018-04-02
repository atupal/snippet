#!/bin/sh

while true; do
  #python2 ./twisted_proxy.py > /dev/null
  python2 ./tornado_proxy.py > /dev/null
  sleep 5
done &
