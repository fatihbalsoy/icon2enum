from bs4 import BeautifulSoup
import urllib.request
from enum import IntEnum

class IconData(IntEnum):
	name, hex, version, uppercamelcased, camelcased, snakecased, unicode = 0, 1, 2, 3, 4, 5, 6

html_page = urllib.request.urlopen("http://cdn.materialdesignicons.com/5.3.45/")
soup = BeautifulSoup(html_page, "html.parser")
def getIcons():
	with open("urls.txt", "a") as myfile:
		script = soup.findAll('script')[0]
		icons0 = str(script).split("var icons = [")
		icons1 = icons0[1].split("]")[0]
		icons = icons1.split("},{")
		
		array = []
		for icon in icons:
			cleaned = icon.replace("{", "")
			cleaned = cleaned.replace("}", "")
			keys = cleaned.split("\"")
			
			name = keys[1]
			hex = keys[3]
			version = keys[5]
			
			uppercamelcased = ''.join(word.title() for word in name.split('-'))
			camelcased = uppercamelcased[0].lower() + uppercamelcased[1:]
			snakecased = '_'.join(word.title() for word in name.split('-'))
			snakecased = snakecased.upper()
			
			unicode = "\"\\u{" + hex + "}\""
			array.append([name, hex, version, uppercamelcased, camelcased, snakecased, unicode])
			
			#print("case", camelcased, "=", unicode) # swift
			#print(camelcased, "=", unicode) # c++
			#print(snakecased + "(" + unicode + ")") # java, kotlin
			#print(snakecased, ":", unicode) # javascript, ruby
			#print(uppercamelcased, "=", unicode) # typescript, go
			#print(snakecased, "=", unicode) # python
			#print("case", camelcased + ":", "\n\treturn @"+ unicode +";") # Obj-C
	return array
			
def generateEnum(lang):
	#print(getIcons()[0][IconData.name])
	if lang == "swift":
		
			
generateEnum("swift")
#text/javascript
#    for link in soup.findAll('a'):
#        if link.get('class') == ["yt-simple-endpoint", "inline-block", "style-scope", "ytd-thumbnail"]:
#            href = str(link.get('href'))
#            if "&index=" in href and "&t=" in href:
#                l = href.split("&")[0]
#                myfile.write(l)
#                myfile.write("\n")
                
