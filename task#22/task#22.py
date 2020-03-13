import requests
import json

client_id = 'my_id'
client_secret = 'my_secret_key'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
artists = dict()
for line in range(15):
    line = input()
    line = line.rstrip()
    r = requests.get("https://api.artsy.net/api/artists/" + line, headers=headers, timeout=5)
    r.encoding = 'utf-8'
    j = json.loads(r.text)
    artists[j['sortable_name']]=j['birthday']

list_d = list(artists.items())
list_d.sort(key=lambda i:i[1])
for item in list_d:
    print(item[0])