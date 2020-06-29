from bs4 import BeautifulSoup
import urllib.request
from enum import IntEnum
from helpers.syntax import *
import os.path


class IconData(IntEnum):
    name, hex, version, uppercamelcased, camelcased, snakecased, unicode = 0, 1, 2, 3, 4, 5, 6


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


def generateFile(lang):
    ext = getExtension(lang)
    with open("MDIcons." + ext, "w") as file:
        cl = generateClass(lang)
        icons = getIcons()
        enums = ""
        for icon in icons:
            enum = generateEnum(getExtension(lang), icon)
            enums += "\t" + enum + "\n"

        final = cl.replace("%s", enums)
        print(final)
        file.write(final)


print("Specify the language to be generated:")
print("(swift, java, kotlin, c++, go, and etc.)")
generateFile(input())
