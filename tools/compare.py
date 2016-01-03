import sys
import itertools

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return itertools.izip_longest(fillvalue=fillvalue, *args)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

# Take data from packet.txt dumped by openhantek
dump_data = [tuple([int(x) for x in line.strip().split(' ')][1:3]) for line in open('packet.txt').readlines()]
#print dump_data[:10]

# Take data from packet_from_ws.txt, build concatenating USB data provided by Wireshark
ws_data = list(grouper(itertools.chain(*[[int(x, 16) for x in line.strip().split(':') if x != ''] for line in open('packet_from_ws.txt').readlines()]), 2))
#print ws_data[:10]

print len(dump_data), len(ws_data)

#for item in enumerate(zip(dump_data, ws_data)):
#    print item

assert dump_data == ws_data
