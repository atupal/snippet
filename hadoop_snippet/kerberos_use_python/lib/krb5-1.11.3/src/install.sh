#!/bin/bash

prefix=$PWD/build/

make install &&

for LIBRARY in gssapi_krb5 gssrpc k5crypto kadm5clnt_mit kadm5srv_mit \
               kdb5 kdb_ldap krb5 krb5support verto ; do
    [ -e  $prefix/lib/lib$LIBRARY.so.*.* ] && chmod -v 755 $prefix/lib/lib$LIBRARY.so.*.*
done # &&

#mv -v /usr/lib/libkrb5.so.3*        /lib &&
#mv -v /usr/lib/libk5crypto.so.3*    /lib &&
#mv -v /usr/lib/libkrb5support.so.0* /lib &&

#ln -v -sf ../../lib/libkrb5.so.3.3        /usr/lib/libkrb5.so        &&
#ln -v -sf ../../lib/libk5crypto.so.3.1    /usr/lib/libk5crypto.so    &&
#ln -v -sf ../../lib/libkrb5support.so.0.1 /usr/lib/libkrb5support.so &&
#
#mv -v /usr/bin/ksu /bin &&
#chmod -v 755 /bin/ksu   &&
#
#install -v -dm755 /usr/share/doc/krb5-1.11.3 &&
#cp -vfr ../doc/*  /usr/share/doc/krb5-1.11.3 &&
#
#unset LIBRARY

