import requests
import json
import tokens

getFollowers = requests.get(
    "https://api.vk.com/method/users.getFollowers?user_id=66748&count=2&fields=photo_50&access_token=" + tokens.token + "&v=5.130")

str_get = json.loads(getFollowers.text)

# print(str_get["response"]["items"][1]['first_name'], str_get["response"]["items"][1]['last_name'])
for i in str_get["response"]["items"]:
    print(i['first_name'], i['last_name'])