with open('my-ranch.html') as f:
    c = f.read()
before = c

old = '<script src="https://pl30647815.effectivecpmnetwork.com/88/5c/31/885c31d1a722e54f06035b860b3b1ef0.js"></script>\n</head>'
new = '</head>'

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
