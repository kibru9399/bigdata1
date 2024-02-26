#!/usr/bin/python
from operator import itemgetter
import sys
# After processing all lines, aggregate counts by hour and then select the top 3 IPs for each hour
final_counts = {}
for line in sys.stdin:
    ip_hr, count = line.split('\t')
    ip, hour = ip_hr.split('#')
    #for (ip, hour), count in counts.items():
    if hour not in final_counts:
        final_counts[hour] = []
    final_counts[hour].append((ip + '#' + count))

for hour, ips_counts in final_counts.items():
    print('%s\t%s' % (hour, ips_counts))


