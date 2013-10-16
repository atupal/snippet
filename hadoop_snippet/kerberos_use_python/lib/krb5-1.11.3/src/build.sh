#!/bin/bash

./configure $@ \
            CFLAGS=" -g -O0 " \
            CPPFLAGS="-I/usr/include/et -I/usr/include/ss" \
            --prefix=$PWD/build                                  \
            --sysconfdir=$PWD/build/etc                              \
            --localstatedir=$PWD/build/var/lib                       \
            --with-system-et                               \
            --with-system-ss                               \
            --enable-dns-for-realm &&
make

#Command Explanations
#
#sed -e ...: First sed fixes Python detection and second one fixes build with Tcl 8.6.
#
#--enable-dns-for-realm: This switch allows realms to be resolved using the DNS server.
#
#--with-system-et: This switch causes the build to use the system-installed versions of the error-table support software.
#
#--with-system-ss: This switch causes the build to use the system-installed versions of the subsystem command-line interface software.
#
#--localstatedir=/var/lib: This parameter is used so that the Kerberos variable run-time data is located in /var/lib instead of /usr/var.
#
#mv -v /usr/bin/ksu /bin: Moves the ksu program to the /bin directory so that it is available when the /usr filesystem is not mounted.
#
#--with-ldap: Use this switch if you want to compile OpenLDAP database backend module.
