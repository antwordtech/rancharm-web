with open('my-ranch.html') as f:
    c = f.read()
before = c

old = '} else if (adsToday < adsRequired) {'
new = '} else if (!isPaidSub && adsToday < adsRequired) {'

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
