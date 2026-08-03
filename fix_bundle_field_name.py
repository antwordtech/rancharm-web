with open('data.html') as f:
    c = f.read()
before = c

old = "const name = b.name || b.title || b.description || 'Bundle';"
new = "const name = b.display || b.name || b.title || b.description || 'Bundle';"

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('data.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
