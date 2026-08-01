with open('tasks.html') as f:
    lines = f.readlines()

before = ''.join(lines)
target_idx = None
for i, line in enumerate(lines):
    if 'owned-badge">Done</div>' in line and 'claimTask' in line:
        target_idx = i
        break

if target_idx is None:
    print('LINE NOT FOUND - check manually')
else:
    old_line = lines[target_idx]
    new_line = old_line.replace(
        '`<button class="btn-small" onclick="claimTask(this,\'${taskId}\', ${task.pointsReward})">Claim</button>`',
        '(kycApproved ? `<button class="btn-small" onclick="claimTask(this,\'${taskId}\', ${task.pointsReward})">Claim</button>` : `<button class="btn-small" onclick="window.location.href=\'kyc.html\'">Verify</button>`)'
    )
    if new_line == old_line:
        print('REPLACE DID NOT MATCH - check manually')
    else:
        lines[target_idx] = new_line
        print('line replaced')

with open('tasks.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
