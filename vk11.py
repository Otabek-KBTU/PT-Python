import requests 
url = 'https://api.vk.com/method/users.get?user_ids=373666991&fields=bdate,blacklisted,status,occupation'

response = requests.get(url)
data = response.json()
status = data['response'][0]['status']
university_name = data['response'][0]['occupation']['name']
uid = data['response'][0]['uid']

url = 'https://api.vk.com/method/wall.get?owner_id=%d' % uid 
print(url)
response = requests.get(url)
data = response.json()
likes_count = data["response"]
post_count = data["response"][0]
posts = data["response"][1:]
print(post_count)
for post in posts:
	text = post['text']
	print(text)