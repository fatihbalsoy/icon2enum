import os.path
from helpers.icon import *

current_dir = os.path.dirname(__file__)


class Syntax:

	lang = ""
	line = ""
	lastline = ""
	alphaline = ""
	
	def __init__(self, lang):
		self.lang = lang
		
	def getExtension(self):
		lang = self.lang
		languages = {
		"c++": "cpp",
		"kotlin": "kt",
		"javascript": "js",
		"ruby": "rb",
		"typescript": "ts",
		"python": "py"
		}
		if lang not in languages:
			return lang
		return languages[lang]
		
	def generateClass(self):
		lang = self.lang
		ext = self.getExtension()
		with open(current_dir + "/../templates/template." + ext, "r") as file:
			head = [next(file) for _ in range(3)]
			content = file.read()
			replacewith = "MDIcons"
			array = ["templates", "template2", "template", "Template"]
			for word in array:
				content = content.replace(word, replacewith)
			return "".join(head) + content
			
	def getUnicode(self, hex):
		lang = self.getExtension()
		if lang == "swift":
			return "\\u{" + hex + "}"
		if lang == "cpp":
			return "\\" + hex
		return "\\u" + hex
		
	def getCase(self):
		lang = self.getExtension()
		if lang in ["swift", "cpp", "objc", "dart"]:
			return IconData.camelcased
		if lang in ["java", "kt", "js", "rb", "py"]:
			return IconData.snakecased
		if lang in ["ts", "go"]:
			return IconData.uppercamelcased
		return IconData.camelcased
		
	def fixedIdentifier(self, name):
		if name in ["import", "switch", "repeat", "protocol", "export", "delete", "null", "sync", "factory"]:
			return name + "_"
		return name
		
	def generateEnum(self, icon, length):
		case = icon[self.getCase()]
		hex = icon[IconData.hex]
		
		current = "THIS_LINE"
		last = "LAST_LINE"
		alpha = "ALPHA_LINE"
		
		if self.line == "" or self.lastline == "":
			template = self.generateClass()
			for line in template.splitlines():
				if current in line:
					self.line = line
				if last in line:
					self.lastline = line
				if alpha in line:
					self.alphaline = line
				if self.line != "" and self.lastline != "" and self.alphaline != "":
					break
					
		enum = self.line
		replace = current
		if icon[IconData.count] == length:
			enum = self.lastline
			replace = last
		enum = enum.replace(replace, self.fixedIdentifier(case))
		enum = enum.replace("\"\"", "\"" + self.getUnicode(hex) + "\"")
		comment = self.alphaline.replace(alpha, icon[0][0].upper())
		return (enum, comment, self.alphaline + "\n" + self.line + "\n" + self.lastline)

