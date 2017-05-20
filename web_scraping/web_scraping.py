'''

Reference: Automate the Boring Stuff with Python ... by Al Sweigart

Cited Date: Saturday, 20-May-2017
Cited By: hack4Mintilo (hack4Mintilo@gmail.com)

'''

## -----------------
## 1. webbrowser
## -----------------
'''
import webbrowser

webbrowser.open("https://www.youtube.com/watch?v=COShI9VBxE4")

'''

## ----------------
## 2. requests
## ----------------
import requests

'''
res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")

type(res)
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])
'''

## checking for Errors
'''
res2 = requests.get("http://inventwithpython.com/page_that_does_not_exist")
try:
    res2.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
'''

## saving downloaded files to the hard
res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))

playFile = open("RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
