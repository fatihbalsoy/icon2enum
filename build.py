from bs4 import BeautifulSoup
import urllib.request
from helpers.syntax import *
from helpers.icon import *
from packages.progressbar import *
import os.path
import time


current_dir = os.path.dirname(__file__)
html_page = urllib.request.urlopen(
    "http://cdn.materialdesignicons.com/5.3.45/")
soup = BeautifulSoup(html_page, "html.parser")


def getIcons():
	script = soup.findAll('script')[0]
	icons0 = str(script).split("var icons = [")
	icons1 = icons0[1].split("]")[0]
	icons = icons1.split("},{")
	
	array = []
	count = 0
	for i in icons:
		count += 1
		cleaned = i.replace("{", "")
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
		array.append([name, hex, version, uppercamelcased,
		camelcased, snakecased, unicode, count])
		
	return array
	
	
def generateFile(syntax):
	ext = syntax.getExtension()
	with open("MDIcons." + ext, "w") as file:
		cl = syntax.generateClass()
		icons = getIcons()
		replacing = ""
		enums = ""
		firstChar = ""
		for icon in progressBar(icons, prefix = 'Progress:', suffix = 'Complete', length = 50):
			enum = syntax.generateEnum(icon, len(icons))
			if firstChar.lower() != icon[0][0]:
				enums += enum[1] + "\n"
				firstChar = icon[0][0]
			enums += enum[0] + "\n"
			replacing = enum[2]
			time.sleep(0.00001)
		
		final = cl.replace(replacing, enums)
		file.write(final)
		
		
print("Specify the language to be generated:")
print("(swift, java, kotlin, c++, go, and etc.)")
syntax = Syntax(input().lower())
generateFile(syntax)

