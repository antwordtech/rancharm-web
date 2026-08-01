with open('firebase-config.js') as f:
    c = f.read()
before = c

old = 'const currentCount = referrerData.referralCount || 0;'
new = 'const currentCount = referrerData.teamCount || 0;'
if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
