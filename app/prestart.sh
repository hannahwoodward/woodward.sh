#! /usr/bin/env bash

# Railway does not support git lfs out the box,
# so re-clone repo here to retrieve resources stored in git lfs
git clone https://github.com/hannahwoodward/woodward.sh.git tmp
mv tmp/app/static/uploads static/uploads
rm -rf tmp
