with open('my-ranch.html') as f:
    c = f.read()
before = c

old = 'toast(`+${currentAnimal.dailyPoints} points earned!`, \'success\');'
new = 'toast(`+${earnedPoints} points earned!` + (rankBonus > 0 ? ` (${rankBonus}% team bonus)` : \'\'), \'success\');'

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
