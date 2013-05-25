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


def printout(keys, data):
    if not keys:
        if 'keys' in switches:
            data = data.keys()
        return json.dumps(data, indent=True)

    key = keys.pop(0)
    return printout(keys, data[key])

def attempt_int(n):
    try: return int(n)
    except: return n

x = json.load(sys.stdin)
args = []
switches = []
for arg in sys.argv[1:]:
    if arg.startswith('--'):
        switches.append(arg[2:])
    else:
        args.append(arg)


for arg in args:
    keys = [attempt_int(n) for n in arg.split('.')]
    print printout(keys, x)
if not args:
    print printout(None, x)
