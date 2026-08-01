with open('firebase-config.js') as f:
    c = f.read()
before = c

# Duck (tier: "Bronze") should be 100, currently wrongly 1000
old_duck = 'tier: "Bronze",   dailyPoints: 1000,'
new_duck = 'tier: "Bronze",   dailyPoints: 100,'
if old_duck not in c:
    print('DUCK PATTERN NOT FOUND - check manually')
c = c.replace(old_duck, new_duck)

# Fox (tier: "Gold") should be 1000, currently wrongly 100
old_fox = 'tier: "Gold",     dailyPoints: 100,'
new_fox = 'tier: "Gold",     dailyPoints: 1000,'
if old_fox not in c:
    print('FOX PATTERN NOT FOUND - check manually')
c = c.replace(old_fox, new_fox)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
