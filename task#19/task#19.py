import re
import requests

a = input().strip()

text = requests.get(a).text
answer = []
pattern = r"<a[^>]*?href[ =]*?[\"'](\w[\w\W]*?)[\"'][\s\w\W]*?>"
pattern2 = r'[\w\W]*?([^/:]+)[:/]*[\w\W]*?'
url = re.findall(pattern, text)
for item in url:
    url2 = re.findall(pattern2, item)
    if item[0:4] == 'http' or item[0:4] == 'www.' or item[0:3] == 'ftp':
        if len(url2) > 1:
            if url2[1] not in answer:
                answer.append(url2[1])
        else:
            if url2[0] not in answer:
                answer.append(url2[0])
    else:
        if url2[0] not in answer:
            answer.append(url2[0])
answer.sort()
for item in answer:
    print(item)