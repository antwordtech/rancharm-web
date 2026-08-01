with open('firebase-config.js') as f:
    c = f.read()
before = c

replacements = [
    ('dailyPoints: 5,', 'dailyPoints: 20,'),
    ('dailyPoints: 15,', 'dailyPoints: 100,'),
    ('dailyPoints: 35,', 'dailyPoints: 300,'),
    ('dailyPoints: 100,', 'dailyPoints: 1000,'),
    ('dailyPoints: 180,', 'dailyPoints: 2000,'),
    ('dailyPoints: 320,', 'dailyPoints: 4000,'),
    ('dailyPoints: 700,', 'dailyPoints: 10000,'),
]

for old, new in replacements:
    if old not in c:
        print('MISSING:', old)
    c = c.replace(old, new, 1)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
