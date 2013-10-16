#!/bin/bash

for i in {1901..2012}
do
  cd /home/yukangle/data/ncdc
  wget -r -np -nH .cut-dirs=3 -R index.html "http://ftp3.ncdc.noaa.gov/pub/data/noaa/$i/"
  cd pub/data/noaa/$i/
  cp *.gz /home/yukangle/data/ncdc/files
  cd /home/yukangle/data/ncdc
  rm -r pub/
done
