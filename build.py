from bs4 import BeautifulSoup
import urllib.request
from enum import IntEnum

class IconData(IntEnum):
	name, hex, version, uppercamelcased, camelcased, snakecased, unicode = 0, 1, 2, 3, 4, 5, 6

html_page = urllib.request.urlopen("http://cdn.materialdesignicons.com/5.3.45/")
soup = BeautifulSoup(html_page, "html.parser")
def getIcons():
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
		
	return array
			
def generateEnum(lang, icon):
	camelcased = icon[IconData.camelcased]
	snakecased = icon[IconData.snakecased]
	uppercamel = icon[IconData.uppercamelcased]
	unicode = icon[IconData.unicode]
	 
	if lang == "swift":
		return "case " + camelcased + " = " + unicode
	if lang in ["c++", "cpp"]:
		return camelcased + " = " + unicode
	if lang in ["java", "kotlin", "kt"]:
		return snakecased + "(" + unicode + ")"
	if lang in ["javascript", "js", "ruby", "rb"]:
		return snakecased + ": " + unicode
	if lang in ["typescript", "ts", "go"]:
		return uppercamelcased + " = " + unicode
	if lang in ["python", "py"]:
		return snakecased + " = " + unicode
	if lang in ["objc"]:
		return "case " + camelcased + ": " + "\n\treturn @"+ unicode +";"
			
def generateClass(lang):
	if lang == "swift":
		return """
import Foundation

enum MDIcon: String {

%s
}"""
	if lang in ["c++", "cpp"]:
		return """
		enum MDIcon {
			%s
		};"""
	if lang in ["java"]:#, "kotlin", "kt"]:
		return """
		public enum MDIcon {
	    %s
	 
	    private String hex;
	 
	    MDIcon(String iconHex) {
	        this.hex = iconHex;
	    }
	 
	    public String getHex() {
	        return hex;
	    }
		}"""
	if lang in ["javascript", "js"]:#, "ruby", "rb"]:
		return """
		var MDIcon = {
	    %s
		};
		"""
	if lang in ["typescript", "ts"]:#, "go"]:
		return """
		enum MDIcon {
	    %s
		};
		"""
	if lang in ["python", "py"]:
		return """
		from enum import Enum
		class MDIcon(Enum):
	    %s
		"""
#	if lang in ["objc"]:
#		return "case " + camelcased + ": " + "\n\treturn @"+ unicode +";"

def generateFile(lang):
	with open("MDIcons.txt", "w") as file:
		cl = generateClass(lang)
		icons = getIcons()
		enums = ""
		for icon in icons:
			enum = generateEnum(lang, icon)
			enums += "\t" + enum + "\n"
		
		final = cl.replace("%s", enums)
		print(final)
		file.write(final)

generateFile("swift")
#text/javascript
#    for link in soup.findAll('a'):
#        if link.get('class') == ["yt-simple-endpoint", "inline-block", "style-scope", "ytd-thumbnail"]:
#            href = str(link.get('href'))
#            if "&index=" in href and "&t=" in href:
#                l = href.split("&")[0]
#                myfile.write(l)
#                myfile.write("\n")
                
