with open('admin-dashboard.html') as f:
    c = f.read()
before = c

old = '''    <a class="nav-tile reveal" style="animation-delay:0.1s" href="admin-withdrawals.html">
      <i class="fa-solid fa-arrow-up-from-bracket" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>
      Withdrawals
      <div id="withdrawalCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
  </div>'''

new = '''    <a class="nav-tile reveal" style="animation-delay:0.1s" href="admin-withdrawals.html">
      <i class="fa-solid fa-arrow-up-from-bracket" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>
      Withdrawals
      <div id="withdrawalCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
    <a class="nav-tile reveal" style="animation-delay:0.15s" href="admin-task-submissions.html">
      <i class="fa-solid fa-clipboard-check" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>
      Task Submissions
      <div id="taskSubCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
  </div>'''

if old not in c:
    print('MARKUP NOT FOUND - check manually')
c = c.replace(old, new)

old_js = '''    document.getElementById('withdrawalCount').textContent = pendingWithdrawalsSnap.size + ' pending';

    document.body.classList.add('ready');'''

new_js = '''    document.getElementById('withdrawalCount').textContent = pendingWithdrawalsSnap.size + ' pending';

    const pendingTaskSubsSnap = await getDocs(query(collection(db, "taskSubmissions"), where("status", "==", "pending")));
    document.getElementById('taskSubCount').textContent = pendingTaskSubsSnap.size + ' pending';

    document.body.classList.add('ready');'''

if old_js not in c:
    print('JS NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('admin-dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
