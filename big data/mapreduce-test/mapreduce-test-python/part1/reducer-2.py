import sys
for line in sys.stdin:
     hr, ips = line.split('\t')
     print '%s\t%s' % (hr, ips)
