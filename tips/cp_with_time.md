```
#!/bin/sh  
# Last modified: 2003年07月05日 星期六 00时09分44秒 [test]  
  
SOURCE=$1  
TARGET=$2  
  
#CP=./fack_cp  
CP=cp  
  
$CP "$SOURCE" "$TARGET" &  
CPID=$!  
  
isalive(){  
    out=`ps -p $1 2> /dev/null`  
    return $?  
}  
  
while [ 1 ]; do {  
    SSIZE=`/bin/ls -l $SOURCE | gawk "{print \\\$5}"`  
    if [ -f $TARGET ]; then  
        TSIZE=`/bin/ls -l $TARGET | gawk "{print \\\$5}"`  
    else  
        TSIZE="0"  
    fi  
    PERCENT=`echo "scale=2; $TSIZE/$SSIZE*100" | bc -l`  
    RATE=`echo "scale=0; 63*$PERCENT/100" | bc -l`  
    BLUE="\\033[3;44m"  
    NORMAIL="\\033[0;39m"  
  
    BAR=$BLUE  
    i=0  
    while [ $i -le 62 ]; do  
        [ $i = $RATE ] && BAR=$BAR"\\033[7;39m"  
        BAR=$BAR" "  
        let i=$i+1  
    done  
    BAR=$BAR$NORMAIL  
    echo -en "\r$BAR ${PERCENT}%"  
    if ! isalive "$CPID"; then echo -en "\n"; exit; fi  
    sleep 1  
}  
done  
```
