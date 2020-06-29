import os.path
from helpers.icon import *

current_dir = os.path.dirname(__file__)


class Syntax:

    lang = ""
    line = ""
    lastline = ""
    headline = ""

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
            content = file.read()
            replacewith = "MDIcons"
            array = ["templates", "template2", "template", "Template"]
            for word in array:
                content = content.replace(word, replacewith)
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
        if lang in ["swift", "cpp", "objc"]:
            return IconData.camelcased
        if lang in ["java", "kt", "js", "rb", "py"]:
            return IconData.snakecased
        if lang in ["ts", "go"]:
            return IconData.uppercamelcased

    def fixedIdentifier(self, name):
        if name in ["import", "switch", "repeat", "protocol", "export", "delete"]:
            return name + "_"
        return name

    def generateEnum(self, icon, length):
        case = icon[self.getCase()]
        hex = icon[IconData.hex]

        current = "THIS_LINE"
        last = "LAST_LINE"
        head = "HEAD_LINE"

        if self.line == "" or self.lastline == "":
            template = self.generateClass()
            for line in template.splitlines():
                if current in line:
                    self.line = line
                if last in line:
                    self.lastline = line
                if head in line:
                    self.headline = line
                if self.line != "" and self.lastline != "" and self.headline != "":
                    break
        
        enum = self.line
        replace = current
        if icon[IconData.count] == length:
            enum = self.lastline
            replace = last
        enum = enum.replace(replace, self.fixedIdentifier(case))
        enum = enum.replace("\"\"", "\"" + self.getUnicode(hex) + "\"")
        comment = self.headline.replace(head, icon[0][0].upper())
        return (enum, comment, self.headline + "\n" + self.line + "\n" + self.lastline)
