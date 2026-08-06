with open('admin-dashboard.html') as f:
    c = f.read()
before = c

old = '''      <div id="taskSubCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
  </div>
</div>'''

new = '''      <div id="taskSubCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
    <a class="nav-tile reveal" style="animation-delay:0.2s" href="admin-users.html">
      <i class="fa-solid fa-users" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>
      Manage Users
      <div id="userTotalCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
  </div>
</div>'''

if old not in c:
    print('MARKUP NOT FOUND - check manually')
c = c.replace(old, new)

old_js = '''    document.getElementById('taskSubCount').textContent = pendingTaskSubsSnap.size + ' pending';

    document.body.classList.add('ready');'''

new_js = '''    document.getElementById('taskSubCount').textContent = pendingTaskSubsSnap.size + ' pending';

    const allUsersSnap = await getDocs(collection(db, "users"));
    document.getElementById('userTotalCount').textContent = allUsersSnap.size + ' total';

    document.body.classList.add('ready');'''

if old_js not in c:
    print('JS NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('admin-dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
