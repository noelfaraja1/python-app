from urllib import request

url = "https://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)

print(r.getcode())
print(r.read())