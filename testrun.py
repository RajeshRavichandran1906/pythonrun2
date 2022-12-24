import os



url = os.getenv("url")


if(url is None):
    url = "Local"
print(url)


for x in range(1, 101):
    print(x, end = ' ')
print("Hellllllooooooo")
