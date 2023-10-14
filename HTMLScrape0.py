# HTMLScrape0.py
# HTML scraper draft 0
# Learning about html scraping for Data Retrieval from google search.
# First exercise
# Reference: https://realpython.com/python-web-scraping-practical-introduction/

from urllib.request import urlopen
import re

# url = "http://olympus.realpython.org/profiles/aphrodite"
# url = "http://olympus.realpython.org/profiles/poseidon"
url = "http://olympus.realpython.org/profiles/dionysus"

page = urlopen(url)
# print(page)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)

# title_index = html.find("<title>")
# print(title_index)

# start_index = title_index + len("<title>")
# print(start_index)

# end_index = html.find("</title>")
# print(end_index)

# title = html[start_index:end_index]
# print(title)

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
