# templates

import fileinput, re

field_pat = re.compile(r'\[(.+?)\]')

scope = {}

def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code,scope))
    except SyntaxError:
        return ''


lines = []
for line in fileinput.input():
    lines.append(line)
text = ''.join(lines)

print (filed_pat.sub(replacement, text))
