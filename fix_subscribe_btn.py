with open('subscription.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if 'Subscribe</button' in line:
        target_idx = i
        break

if target_idx is None:
    print('LINE NOT FOUND - check manually')
else:
    new_line = "        (isCurrent ? '<div class=\"current-badge\">Current Plan</div>' : '<button class=\"btn-small\" data-sub-key=\"' + sub.key + '\" onclick=\"subscribeClick(this)\">Subscribe</button>');\n"
    lines[target_idx] = new_line
    print('line replaced')

with open('subscription.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
