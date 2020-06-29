import os.path
from helpers.icon import *

current_dir = os.path.dirname(__file__)

def getExtension(lang):
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

def generateClass(lang):
    ext = getExtension(lang)
    with open(current_dir + "/../lang/template." + ext, "r") as file:
        return file.read()

def generateEnum(lang, icon):
    camelcased = icon[IconData.camelcased]
    snakecased = icon[IconData.snakecased]
    uppercamel = icon[IconData.uppercamelcased]
    unicode = icon[IconData.unicode]

    if lang == "swift":
        return "case " + camelcased + " = " + unicode
    if lang == getExtension("c++"):
        return camelcased + " = " + unicode
    if lang in ["java", getExtension("kotlin")]:
        return snakecased + "(" + unicode + ")"
    if lang in [getExtension("javascript"), getExtension("ruby")]:
        return snakecased + ": " + unicode
    if lang in [getExtension("typescript"), "go"]:
        return uppercamel + " = " + unicode
    if lang == getExtension("python"):
        return snakecased + " = " + unicode
    if lang in ["objc"]:
        return "case " + camelcased + ": " + "\n\treturn @" + unicode + ";"
