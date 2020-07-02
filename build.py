from bs4 import BeautifulSoup
import urllib.request
from helpers.syntax import *
from helpers.icon import *
from packages.progressbar import *
import os.path
import time


current_dir = os.path.dirname(__file__)
url = "http://cdn.materialdesignicons.com/"
latest = "5.3.45"
version = latest

def createIcon(name, hex, version, count):
	uppercamelcased = ''.join(word.title() for word in name.split('-'))
	camelcased = uppercamelcased[0].lower() + uppercamelcased[1:]
	snakecased = '_'.join(word.title() for word in name.split('-'))
	snakecased = snakecased.upper()
	
	unicode = "\"\\u{" + hex + "}\""
	return [name, hex, version, uppercamelcased, camelcased, snakecased, unicode, count]

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
		
		array.append(createIcon(name, hex, version, count))
	array.append(createIcon("blank", "F68C", "", count + 1))
		
	return array
	
	
def generateFile(syntax):
	ext = syntax.getExtension()
	filename = "MDIcons"
	suffix = str("+" + version) if version != latest else ""
	finalname = filename + suffix + "." + ext
	with open("source.txt", "w") as page:
		page.write(str(soup))
	with open(finalname, "w") as file:
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
			#time.sleep(0.00001)
		
		final = cl.replace(replacing, enums)
		file.write(final)
		print("Generated " + str(len(icons)) + " Material Design Icons in " + finalname)
		
		
print("Specify the language to be generated:")
print("(swift, java, kotlin, c++, go, and etc.)")
syntax = Syntax(input().lower())
print("Specify version of data set:")
print("(Keep blank for latest version)")
input_version = input()
if input_version != "":
	version = input_version
	
html_page = urllib.request.urlopen(url + version)
soup = BeautifulSoup(html_page, "html.parser")

generateFile(syntax)

