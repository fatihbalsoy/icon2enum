from bs4 import BeautifulSoup
import urllib.request
from helpers.syntax import *
from helpers.icon import *
import os.path


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
