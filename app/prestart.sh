#! /usr/bin/env bash

# Railway does not support git lfs out the box,
# so download retrieve resources stored in git lfs
rm -rf static/uploads tmp
mkdir tmp
cd tmp
wget https://github.com/hannahwoodward/woodward.sh/archive/refs/heads/main.zip
unzip main.zip
cd ..
mv tmp/*/app/static/uploads static/uploads
rm -rf tmp
