# --- my-ranch.html: gate Feed Now behind KYC approval ---
with open('my-ranch.html') as f:
    c = f.read()
before = c

old = '''    const today = new Date().toISOString().split('T')[0];
    const fedToday = data.lastFedDate === today;
    const feedBtn = document.getElementById('feedBtn');
    feedBtn.disabled = fedToday;
    feedBtn.innerHTML = fedToday ? 'Already Fed Today' : 'Feed Now';
  }'''

new = '''    const feedBtn = document.getElementById('feedBtn');
    const kycApproved = (data.kycStatus || 'unverified') === 'approved';

    if (!kycApproved) {
      feedBtn.disabled = false;
      feedBtn.innerHTML = 'Verify Identity to Earn';
      feedBtn.onclick = () => { window.location.href = 'kyc.html'; };
    } else {
      const today = new Date().toISOString().split('T')[0];
      const fedToday = data.lastFedDate === today;
      feedBtn.disabled = fedToday;
      feedBtn.innerHTML = fedToday ? 'Already Fed Today' : 'Feed Now';
      feedBtn.onclick = window.feedAnimal;
    }
  }'''

if old not in c:
    print('my-ranch.html: PATTERN NOT FOUND - check manually')
c = c.replace(old, new)
with open('my-ranch.html', 'w') as f:
    f.write(c)
print('my-ranch.html', 'OK' if c != before else 'NO CHANGE')

# --- tasks.html: gate Claim behind KYC approval ---
with open('tasks.html') as f:
    c = f.read()
before = c

old_var = '''  let currentUid = null;
  let completedTasks = [];'''
new_var = '''  let currentUid = null;
  let completedTasks = [];
  let kycApproved = false;'''
if old_var not in c:
    print('tasks.html: VAR PATTERN NOT FOUND - check manually')
c = c.replace(old_var, new_var)

old_set = '''    currentUid = user.uid;
    completedTasks = profile.completedTasks || [];'''
new_set = '''    currentUid = user.uid;
    completedTasks = profile.completedTasks || [];
    kycApproved = (profile.kycStatus || 'unverified') === 'approved';'''
if old_set not in c:
    print('tasks.html: SET PATTERN NOT FOUND - check manually')
c = c.replace(old_set, new_set)

old_btn = '''          \${done ? '<div class=\"owned-badge\">Done</div>' : \`<button class=\"btn-small\" onclick=\"claimTask(this,'\${taskId}', \${task.pointsReward})\">Claim</button>\`}'''
new_btn = '''          \${done ? '<div class=\"owned-badge\">Done</div>' : (kycApproved ? \`<button class=\"btn-small\" onclick=\"claimTask(this,'\${taskId}', \${task.pointsReward})\">Claim</button>\` : \`<button class=\"btn-small\" onclick=\"window.location.href='kyc.html'\">Verify</button>\`)}'''
if old_btn not in c:
    print('tasks.html: BUTTON PATTERN NOT FOUND - check manually')
c = c.replace(old_btn, new_btn)

with open('tasks.html', 'w') as f:
    f.write(c)
print('tasks.html', 'OK' if c != before else 'NO CHANGE')
