import requests
import sys
url = 'http://numbersapi.com/'
gets = requests.get(url).text
for line in sys.stdin:
    line = line.rstrip()
    gets = requests.get(url + line + '/math?json=true', timeout=5)
    gets = gets.json()
    if gets['found'] == False:
        print('Boring')
    else:
        print('Interesting')
