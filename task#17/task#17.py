import re
import sys
pattern = r"\b(\w{1})(\w{1})(\w*)\b"
repl = 'argh'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern,r'\2\1\3', line))
    print(re.findall(pattern, line))
