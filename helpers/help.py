from bs4 import BeautifulSoup
import urllib.request

def help(meta_url, help):
	html_page = urllib.request.urlopen(meta_url)
	soup = BeautifulSoup(html_page, "html.parser")
	
	meta = json.loads(str(soup))
	
	for icon in meta:
		version = i["version"]
		i_author = i["author"]
		i_tags = i["tags"]
		i_tags_joined = " / ".join(i_tags).split(" / ")
