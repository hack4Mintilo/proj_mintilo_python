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

## -- checking for Errors
'''
res2 = requests.get("http://inventwithpython.com/page_that_does_not_exist")
try:
    res2.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))
'''

## -- saving downloaded files to the hard
'''
res = requests.get("http://www.gutenberg.org/cache/epub/1112/pg1112.txt")
try:
    res.raise_for_status()
except Exception as exc:
    print("There was a problem: %s" % (exc))

playFile = open("RomeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
'''


## -- parsing HTML with the BeautifulSoup module
import bs4

res = requests.get("https://www.nostarch.com/")
try:
    res.raise_for_status()
except Exception as e:
    print("Sorry, something went wrong... %s" %(s))

noStarchSoup = bs4.BeautifulSoup(res.text)
type(noStarchSoup)

## -- You can also load an HTML file from your hard drive
exampleFile = open("example.html")
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleSoup)

# element: id-author
elems = exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs

# element: p
pElems = exampleSoup.select('p')

## -- getting data from an element attributes
import bs4

soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
spanElem.get['id']
