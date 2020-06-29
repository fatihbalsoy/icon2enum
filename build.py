from bs4 import BeautifulSoup
import urllib.request
from helpers.syntax import *
from helpers.icon import *
import os.path


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
	for i in icons:
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
		camelcased, snakecased, unicode])
		
	return array
	
	
def generateFile(syntax):
	ext = syntax.getExtension()
	with open("MDIcons." + ext, "w") as file:
		cl = syntax.generateClass()
		icons = getIcons()
		enums = ""
		x = 0
		for icon in icons:
			enum = syntax.generateEnum(icon)
			enums += "\t" + enum + "\n"
			name = icon[IconData.name]
			#print(f'{icon[IconData.name]}\r', end="")
			#print('{}\r'.format(name), end="")
			#print("Progress {:2.1%}".format(x / len(icons)), end="\r")
			x += 1
		print()
		
		final = cl.replace("%s", enums)
		#print(final)
		file.write(final)
		
		
print("Specify the language to be generated:")
print("(swift, java, kotlin, c++, go, and etc.)")
syntax = Syntax(input())
generateFile(syntax)

