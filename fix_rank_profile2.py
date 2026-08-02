with open('profile.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if 'People Referred' in line and 'profile-row-label' in line:
        target_idx = i
        break

if target_idx is None:
    print('ANCHOR LINE NOT FOUND - check manually')
else:
    # lines[target_idx] is the "People Referred" label line
    # lines[target_idx+1] is the value div, lines[target_idx+2] is the closing </div>
    insert = [
        '    </div>\n',
        '    <div class="profile-row">\n',
        '      <div class="profile-row-label">Team Rank</div>\n',
        '      <div class="profile-row-value" id="profileTeamRank">-</div>\n'
    ]
    close_idx = target_idx + 2
    lines[close_idx:close_idx] = insert
    print('markup inserted')

with open('profile.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
