from urllib.request import urlopen

City = input("Were do you want the weather for?")

link ='https://wttr.in/'+City+'?A'
wget = urlopen(link)

webtext = wget.read()
print(webtext.decode('utf-8'))