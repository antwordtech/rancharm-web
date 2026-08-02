with open('dashboard.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if "document.body.classList.add('ready');" in line:
        target_idx = i
        break

if target_idx is None:
    print('LINE NOT FOUND - check manually')
else:
    insert = "    if (isAdmin(user)) { document.getElementById('adminLink').style.display = 'flex'; }\n\n"
    lines.insert(target_idx, insert)
    print('line inserted')

with open('dashboard.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
