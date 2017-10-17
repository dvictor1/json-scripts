#!/usr/bin/python3
# answer to Q1
# input: data1.json (original json file with a single channel
# output 'CHANNEL_ID' and 'CHANNEL_URL' fields to stdout formatted as CSV with ',' delimiter
#
import json

with open('data1.json') as input_json:
    jsondata = json.load(input_json)

    print(jsondata['channels']['id'],',',jsondata['channels']['playlists']['playlist_url'], sep='')
