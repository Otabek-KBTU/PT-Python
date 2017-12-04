import vk
session = vk.Session(access_token ='5422355d35941a74a970f9bb80441debc01d8dae8901213ccd8de058338e9aa65f14f635f92fce39e64fe')
api = vk.API(session)
l = api.friends.get()
print(l)
r = api.status.set(text='')
print(r)
l = api.wall.get()
print(l)