with open('my-ranch.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if 'window.watchAd = () => {' in line:
        target_idx = i
        break

if target_idx is None:
    print('LINE NOT FOUND - check manually')
else:
    insert = "    window.open('https://www.effectivecpmnetwork.com/b27gbbgvi?key=45b99abc87be0f94221817c51efc936d', '_blank');\n"
    lines.insert(target_idx + 1, insert)
    print('line inserted')

with open('my-ranch.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
