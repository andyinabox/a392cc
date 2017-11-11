#!/bin/bash

# this will delete all .m4a files in the source folder
# run `confert_m4a` first!

# import dotenv file
source .env

read -p "Are you sure you want to remove all m4a files? <y/N> " prompt
if [[ $prompt =~ [yY](es)* ]]; then
  rm $PHONE_MUSIC_PATH*/*/*.m4a
fi