#!/usr/bin/python
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
