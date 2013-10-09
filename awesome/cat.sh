#!/usr/bin/env bash

# output some message to stderr
cat 1 > &2 << EOF
    ...
    some text
    ...
EOF
