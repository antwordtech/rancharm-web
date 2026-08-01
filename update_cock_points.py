with open('firebase-config.js') as f:
    c = f.read()
before = c

old = 'tier: "Starter",  dailyPoints: 20,'
new = 'tier: "Starter",  dailyPoints: 50,'

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
