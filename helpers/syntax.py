import os.path
from helpers.icon import *

current_dir = os.path.dirname(__file__)


class Syntax:

    lang = ""
    line = ""
    lastline = ""

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
        with open(current_dir + "/../lang/template." + ext, "r") as file:
            content = file.read()
            replacewith = "MDIcons"
            content = content.replace("template2", replacewith)
            content = content.replace("template", replacewith)
            content = content.replace("Template", replacewith)
            return content

    def getUnicode(self, hex):
        lang = self.getExtension()
        if lang in ["java", "py", "js"]:
            return "\\u" + hex
        if lang == "cpp":
            return "\\" + hex
        return "\\u{" + hex + "}"

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

        if self.line == "" or self.lastline == "":
            template = self.generateClass()
            for line in template.splitlines():
                if "THIS_LINE" in line:
                    self.line = line
                if "LAST_LINE" in line:
                    self.lastline = line
                if self.line != "" and self.lastline != "":
                    break
        
        enum = self.line
        replace = "THIS_LINE"
        if icon[IconData.count] == length:
            enum = self.lastline
            replace = "LAST_LINE"
        enum = enum.replace(replace, self.fixedIdentifier(case))
        enum = enum.replace("\"\"", "\"" + self.getUnicode(hex) + "\"")
        return (enum, self.line + "\n" + self.lastline)
