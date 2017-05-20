#! python3
# lucky.py - Opens several Google search results.

'''
Reference: Automate the Boring Stuff with Python ... by Al Sweigart
Cited Date: Saturday, 20-May-2017
Cited By: hack4Mintilo (hack4Mintilo@gmail.com)
'''

import requests, sys, webbrowser, bs4

print("Googling...")  # display text while downloading the Google page
res = requests.get("http://google.com/search?q=" + ''.join(sys.argv[1:]))
res.raise_for_status()
