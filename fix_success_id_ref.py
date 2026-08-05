with open('withdraw.html') as f:
    c = f.read()
before = c

old = "document.getElementById('successView').style.display = 'block';"
new = "document.getElementById('step3').style.display = 'block';"

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('withdraw.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
