#! python3

import pyperclip
import re
text = pyperclip.paste()

emailRegex = re.compiler'r\@\$[.com]')