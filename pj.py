#!/usr/bin/python
"""
pj.py
2013-05-17
by Matt Donahoe

Pretty-print json from the command line

View a file
$> cat test.json | pj
{
 "foo":1
 "bar":2
}

Read a key
$> cat test.json | pj foo
1

View all keys

cat test.json | pj --keys
[
1,
2
]

"""

import sys
import json
import argparse

parser = argparse.ArgumentParser(description='Parse JSON')

parser.add_argument('--keys_only', action='store_true', default=False,
                   help='return only the keys for the json object')

parser.add_argument('--foreach', action='store', type=str,
                   help='for each item in the json object, return value for this key. Similar to valueForKey in objC')

parser.add_argument('paths', metavar='path', type=str, nargs='*',
                   help='a item to extract from the json')

args = parser.parse_args()


def printout(keys, data):
    if not keys:
        if args.keys_only:
            data = data.keys()
        elif args.foreach:
            data = [x[args.foreach] for x in data if args.foreach in x]
        return json.dumps(data, indent=True, separators=(",",":"))

    key = keys.pop(0)
    return printout(keys, data[key])

def attempt_int(n):
    try: return int(n)
    except: return n

x = json.load(sys.stdin)

for path in args.paths:
    keys = [attempt_int(n) for n in path.split('.')]
    print printout(keys, x)

if not args.paths:
    print printout(None, x)

