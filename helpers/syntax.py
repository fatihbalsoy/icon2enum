import os.path
from helpers.icon import *

current_dir = os.path.dirname(__file__)

class Syntax:

	lang = ""
	
	def __init__(self, lang):
		self.lang = lang
		
	def getExtension(self):
		lang = self.lang
		if lang == "c++":
			return "cpp"
		if lang == "kotlin":
			return "kt"
		if lang == "javascript":
			return "js"
		if lang == "ruby":
			return "rb"
		if lang == "typescript":
			return "ts"
		if lang == "python":
			return "py"
		return lang
		
	def generateClass(self):
		lang = self.lang
		ext = self.getExtension()
		with open(current_dir + "/../lang/template." + ext, "r") as file:
			return file.read()
			
	def getUnicode(self, hex):
		lang = self.lang
		if lang is "swift":
			return "\\u{" + hex + "}"
		if lang is "java":
			return "\\u" + hex
			
	def generateEnum(self, icon):
		lang = self.getExtension()
		camelcased = icon[IconData.camelcased]
		snakecased = icon[IconData.snakecased]
		uppercamel = icon[IconData.uppercamelcased]
		unicode = icon[IconData.unicode]
		
		if lang == "swift":
			return "case " + camelcased + " = " + unicode
		if lang == "cpp":
			return camelcased + " = " + unicode
		if lang in ["java", "kt"]:
			return snakecased + "(" + unicode + ")"
		if lang in ["js", "rb"]:
			return snakecased + ": " + unicode
		if lang in ["ts", "go"]:
			return uppercamel + " = " + unicode
		if lang == "py":
			return snakecased + " = " + unicode
		if lang == "objc":
			return "case " + camelcased + ": " + "\n\treturn @" + unicode + ";"

