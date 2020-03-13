import requests
import re
url = input()
test = input()
try:
    a = requests.get(url)
    pattern = r'<a[\s\w\W]*href="(http[\w\W]+)"[\s\w\W]*?>'
    check = []
    answer = 'No'
    for item in re.findall(pattern, a.text):
        check.append(item)
    if(len(check)>0):
        for item in check:
            try:
                for url in re.findall(pattern, requests.get(item).text):
                    if url in test:
                        answer = "Yes"
            except:
                pass
    print(answer)
except:
    print('No')

