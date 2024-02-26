import re
import sys

# Initialize a dictionary to hold the counts for each IP and hour
counts = {}

# Compile the regular expression pattern to extract IP, hour, and path
pat = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*\[(?P<datetime>\d+/[a-zA-Z]+/\d+:(?P<hour>\d+):\d+:\d+).*?"\w+ (?P<subdir>.*?) ')

for line in sys.stdin:
    match = pat.search(line)
    if match:
        ip = match.group('ip')
        hour = match.group('hour')
        key = (ip, hour)
        counts[key] = counts.get(key, 0) + 1
for (ip, hour), count in counts.items():
    print '%s\t%s'(ip + '#' + hour, count)
