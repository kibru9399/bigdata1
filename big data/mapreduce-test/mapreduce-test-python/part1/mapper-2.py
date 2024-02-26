import sys
from operator import itemgetter
# Sort the IPs in each hour by count and select the top 3
for line in sys.stdin:
    hour, ips_counts = line.split('\t') 
    ips_counts = ips_counts.split(',')
    ips_counts[0] = ips_counts[0][1:]
    ips_counts[-1] = ips_counts[-1][:-1]
    l = []
    for ip_cnt in ips_counts:
        ip, cnt = ip_cnt.split('#')
        l.append((ip, int(cnt)))
    ips_counts = l
    top_ips = sorted(ips_counts, key=lambda x: x[1], reverse=True)[:3]
    for ip, count in top_ips:
        print('%s\t%s\t%s' % (hour, ip, count)) 