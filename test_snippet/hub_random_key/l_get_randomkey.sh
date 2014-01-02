#!/usr/bin/env bash

referer="http://bksjw.hust.edu.cn/frames/body_left.jsp"
cookie="JSESSIONID=0000EJCMHH481RfSFqjvQj0nICn:167ihblo9"
url="http://bksjw.hust.edu.cn/aam/score/QueryScoreByStudent_readyToQuery.action?cdbh=225"


getkey(){
  curl $url --cookie $cookie --referer $referer 2>/dev/null |
                                          grep "key1\|key2" |
                   awk '{split($4, a, "\""); printf(a[2] " ")}'
                   echo ""
};


for i in `seq 99999`; do
  getkey || true
done
