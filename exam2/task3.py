from lxml import etree
import re
import requests


url = "https://twitter.com/googlefacts"
data = requests.get(url).text

parser = etree.HTMLParser()
tree = etree.fromstring(data, parser)

for post in tree.iter("p"):
    if "tweet-text" in str(post.attrib):
        print(post.text)
