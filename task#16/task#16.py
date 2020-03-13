import sys
import re
pattern = r"\b(cat)\b"
for line in sys.stdin:
    line = line.rstrip()
    if len(re.findall(pattern, line)) >= 1:
        print(line)