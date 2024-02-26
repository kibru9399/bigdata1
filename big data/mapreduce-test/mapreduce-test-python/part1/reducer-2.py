import sys
for line in sys.stdin:
     hour, ip, count = line.split('\t') 
     print('%s\t%s\t%s' % (hour, ip, count))
