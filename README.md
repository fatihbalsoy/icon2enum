# icon2enum
Automatically fetches Material Design Icons and creates an enum of unicode strings for the specified programming language.

## Supported languages

- Swift
- Kotlin
- Typescript
- C++
- Dart
- JavaScript 
- Python
- Ruby
- Java

Feel free to send a pull request to add your favorite language to this list!
Just create a template in the `templates` folder and make minor modifications in `helpers/syntax.py` like specifying the extension and enum style (camelcase or snakecase).

## Usage

Install beautifulsoup4 using pip3
```bash
pip3 install beautifulsoup4
```

Run icon2enum using python3
```bash
python3 build.py
```

You will be presented with three options:
```bash
Select one or more options:
f. Download fonts
g. Generate language specific file
h. Output hex codepoints
```

Selecting any of the three will have the same set of questions:
```bash
Specify version of data set:
(Latest, master, 7.1.96, and etc.)
master 
# Only the master branch works for all options.
# Picking versions is only available for the "Download (F)onts" option.

Specify the language to be generated:
(swift, java, kotlin, c++, go, and etc.)
# Required. This is asked only when "(G)enerate language files" is selected.

Filter tags, separated by commas:
# Optional, examples: device, transportation, network
account # This will generate a file with icons tagged as 'account'

Filter authors, separated by commas:
# Optional, examples: google, templarian
```

You can find tags and authors to add to the filter on the Community Material Icons website:

Tags: https://pictogrammers.com/library/mdi/

Authors: https://pictogrammers.com/docs/contribute/contributors/

## Output directory

The files are generated into the following folders:
```
build                                                   
├── fonts
│   ├─ mdi-7.1.96.ttf
│   ├─ mdi-master.ttf
├── hex
│   ├─ hex-master.json
├── lang
│   ├─ MDIcons+master.swift
├── source
    ├─ source.json
```

## Using the MDIcons enum

After downloading the font and generating files with icon2enum, you can simply drag the files into your project and call them like so:

### Swift
```swift
let headphoneIcon: String = MDIcons.headphones // variable is set to "\u{F02CB}"
let iconLabel: UILabel = UILabel()
iconLabel.font = UIFont("Material Design Icons", ...)
iconLabel.text = headphoneIcon
```

### Kotlin
```kotlin
val headphoneIcon = MDIcons.valueOf("HEADPHONES")
```

### C++
```cpp
MDIcons icons;
std::string headphoneIcon = icons.headphones;
```

### TypeScript
```ts
const headphoneIcon = MDIcons.Headphones
```

