with open('my-ranch.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if "window.open('https://www.effectivecpmnetwork.com" in line:
        target_idx = i
        break

if target_idx is None:
    print('LINE NOT FOUND - check manually')
else:
    del lines[target_idx]
    print('line removed')

with open('my-ranch.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
