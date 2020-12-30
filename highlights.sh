#!/bin/bash
# A simple script that converts the "My Clippings.txt" file provided by Kindle into
# a more easily manipulated format and then executes python script

awk '{ gsub(/\xef\xbb\xbf/,""); print }' My\ Clippings.txt > clippings
python3 highlights.py
