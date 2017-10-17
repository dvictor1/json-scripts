#!/usr/bin/python3
# answer to Q3, restoring original JSON file from Q2
# input: out.csv, created with Q2 script (./2.py > out.csv)
# output: out.json
# compare/check: diff data2.json out.json
#
import csv
import json

jsonfile = open('out.json', 'w')

with open('out.csv') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=',')

    jsondata = {}

    jsondata['distributor'] = "ABC"

    jsondata['channels'] = []

    for row in csvdata:
        jsondata['channels'].append({'id': row[0],'playlists': {'playlist_url': row[1]}})

json.dump(jsondata, jsonfile, indent=4, sort_keys=True)
