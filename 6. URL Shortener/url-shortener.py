# import pyshorteners
import pyshorteners

url = input("Input the link you want to shorten: ")
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

print(short_url)