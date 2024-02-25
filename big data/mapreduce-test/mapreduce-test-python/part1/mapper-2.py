import sys
from operator import itemgetter
d_hr = {}
for line in sys.stdin:
    hr, ips = line.split('\t')
    ips = ips.split(',')[1:-1]
    d_ips  = {}
    for ip in ips:
        try: 
            d_ips[ip] = d_ips.get(ip, 0) + 1
        except:
            pass
    try:
        sorted_d_ips = sorted(d_ips.items(), key=itemgetter(1), revers=True)
        d_hr[hr] = sorted_d_ips
    except:
        pass
for hr, ips in d_hr:
     print '%s\t%s' % (hr, ips[:3])
