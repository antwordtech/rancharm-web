with open('my-ranch.html') as f:
    c = f.read()
before = c

# Add the Popunder script right before </head>
popunder_script = '<script src="https://pl30647815.effectivecpmnetwork.com/88/5c/31/885c31d1a722e54f06035b860b3b1ef0.js"></script>\n</head>'
if '</head>' in c:
    c = c.replace('</head>', popunder_script, 1)
else:
    print('HEAD CLOSE TAG NOT FOUND - check manually')

# Remove the old Smartlink window.open call (Popunder fires automatically on click, no URL needed)
old_open = "    const adWindow = window.open('https://www.effectivecpmnetwork.com/b27gbbgvi?key=45b99abc87be0f94221817c51efc936d', '_blank');\n    if (!adWindow) {\n      toast('Please allow pop-ups for this site to watch ads', 'error');\n      return;\n    }\n"
if old_open not in c:
    print('OLD SMARTLINK OPEN NOT FOUND - check manually')
c = c.replace(old_open, '')

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
