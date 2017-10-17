#!/usr/bin/python3
# answer to Q2
# input: data2.json (modified original json file with two channels
# output 'CHANNEL_ID' and 'CHANNEL_URL' fields to stdout formatted as CSV with ',' delimiter
#
import json

with open('out.json') as input_json:
    jsondata = json.load(input_json)

for channel in jsondata['channels']:
    print(channel['id'],',',channel['playlists']['playlist_url'], sep='')
