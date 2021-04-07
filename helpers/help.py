from bs4 import BeautifulSoup
import urllib.request
import json

def help(meta_url, help):
	html_page = urllib.request.urlopen(meta_url)
	soup = BeautifulSoup(html_page, "html.parser")
	
	meta = json.loads(str(soup))
	
	for icon in meta:
		version = icon["version"]
		i_author = icon["author"]
		i_tags = icon["tags"]
		i_tags_joined = " / ".join(i_tags).split(" / ")
