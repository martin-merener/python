
import requests

url_base = 'https://xkcd.com/353/'
r = requests.get(url_base)

#print(dir(r)) # attributes and methods for an object
#print(help(r)) # more details

#print(r.text) # we get the source of the website in html
#print(r.status_code)
#print(r.header)
print(r.ok) # true, if the status_code does not represent an error

# Suppose we want to download content (an image) from the website


url_image = 'https://imgs.xkcd.com/comics/python.png'
r = requests.get(url_image)
#print(r.content) 

with open('comic.png', 'wb') as f: # write bytes
	f.write(r.content) # it's going to write a file