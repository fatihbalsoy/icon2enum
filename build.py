from bs4 import BeautifulSoup
import urllib.request
import json
from helpers.syntax import *
from helpers.icon import *
from packages.progressbar import *
import os.path
import time


current_dir = os.path.dirname(__file__)
url = "http://cdn.materialdesignicons.com/"
github = "https://raw.githubusercontent.com/Templarian/MaterialDesign/master/meta.json"
latest = "5.3.45"
data_version = latest

def createIcon(name, hex, version, count):
	uppercamelcased = ''.join(word.title() for word in name.split('-'))
	camelcased = uppercamelcased[0].lower() + uppercamelcased[1:]
	snakecased = '_'.join(word.title() for word in name.split('-'))
	snakecased = snakecased.upper()
	
	unicode = "\"\\u{" + hex + "}\""
	return [name, hex, version, uppercamelcased, camelcased, snakecased, unicode, count]
	
def getIcons():
	if data_version != "master":
		script = soup.findAll('script')[0]
		icons0 = str(script).split("var icons = [")
		icons1 = icons0[1].split("]")[0]
		icons = icons1.split("},{")
	else:
		icons = meta
		
	array = []
	count = 0
	for i in icons:
		count += 1
		
		if data_version != "master":
			cleaned = i.replace("{", "")
			cleaned = cleaned.replace("}", "")
			keys = cleaned.split("\"")
			
			name = keys[1]
			hex = keys[3]
			version = keys[5]
		else:
			name = i["name"]
			hex = i["codepoint"]
			version = i["version"]
			
		array.append(createIcon(name, hex, version, count))
	array.append(createIcon("blank", "F68C", "", count + 1))
	
	return array
	
	
def generateFile(syntax):
	ext = syntax.getExtension()
	filename = "MDIcons"
	suffix = str("+" + data_version) if data_version != latest else ""
	finalname = filename + suffix + "." + ext
	
	source_ext = ".json" if data_version == "master" else ".html"
	with open("source" + source_ext, "w") as page:
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
	data_version = input_version
	
page_url = url + data_version if not data_version == "master" else github

html_page = urllib.request.urlopen(page_url)
soup = BeautifulSoup(html_page, "html.parser")
if data_version == "master":
	meta = json.loads(str(soup))
	
generateFile(syntax)

