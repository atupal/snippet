#!/bin/bash

./configure \
  --prefix=$PWD/build \
  --enable-curldebug \
  --with-ssl \
  --with-gssapi \
  &&
make
