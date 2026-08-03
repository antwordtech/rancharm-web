with open('data.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if 'buyBundle(\\\\' in line:
        target_idx = i
        break

if target_idx is None:
    print('LINE NOT FOUND - check manually')
else:
    new_line = '          \'<button class="btn-small" data-bundle-id="\' + id + \'" data-bundle-price="\' + price + \'" onclick="buyBundleClick(this)">Buy</button>\';\n'
    lines[target_idx] = new_line
    print('line replaced')

with open('data.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
