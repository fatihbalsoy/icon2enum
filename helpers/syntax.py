import os.path

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
