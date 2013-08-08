#!/bin/bash

./configure CFLAGS=-g --prefix=$PWD/build \
  --enable-curldebug \
  --with-ssl \
  --with-gssapi \
  &&
make
