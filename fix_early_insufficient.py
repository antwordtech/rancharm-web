with open('data.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if 'pointsCost > currentPoints' in line:
        target_idx = i
        break

if target_idx is None:
    print('LINE NOT FOUND - check manually')
else:
    lines[target_idx] = "    if (pointsCost > currentPoints) { toast('Insufficient points balance', 'error'); if (btn) { btn.disabled = false; btn.innerHTML = originalHtml; } return; }\n"
    print('line replaced')

with open('data.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
