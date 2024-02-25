#!/usr/bin/python
from operator import itemgetter
import sys

dict_hr_ip = {}

for line in sys.stdin:
    line = line.strip()
    hr_ip, num = line.split('\t')
    hr_ip = hr_ip.split(']')
    hr, ip = hr_ip[0][1:], hr_ip[1]
    try:
        num = int(num)
        dict_hr_ip[hr] = dict_hr_ip.get(hr, ',') + str(ip) + ','

    except ValueError:
        pass


#sorted_dict_ip_count = sorted(dict_ip_count.items(), key=itemgetter(0))
for hr, ip in dict_hr_ip:
    print '%s\t%s' % (hr, ip)
