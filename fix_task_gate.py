with open('tasks.html') as f:
    c = f.read()
before = c

old = '''          ${done ? '<div class="owned-badge">Done</div>' : (kycApproved ? `<button class="btn-small" onclick="claimTask(this,'${taskId}', ${task.pointsReward})">Claim</button>` : `<button class="btn-small" onclick="window.location.href='kyc.html'">Verify</button>`)}'''

new = '''          ${done ? '<div class="owned-badge">Done</div>' : `<button class="btn-small" onclick="claimTask(this,'${taskId}', ${task.pointsReward})">Claim</button>`}'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('tasks.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
