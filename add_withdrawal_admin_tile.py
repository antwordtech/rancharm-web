with open('admin-dashboard.html') as f:
    c = f.read()
before = c

old = '''    <a class="nav-tile reveal" style="animation-delay:0.05s" href="admin-tasks.html">
      <i class="fa-solid fa-list-check" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>
      Manage Tasks
      <div id="taskCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
  </div>'''

new = '''    <a class="nav-tile reveal" style="animation-delay:0.05s" href="admin-tasks.html">
      <i class="fa-solid fa-list-check" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>
      Manage Tasks
      <div id="taskCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
    <a class="nav-tile reveal" style="animation-delay:0.1s" href="admin-withdrawals.html">
      <i class="fa-solid fa-arrow-up-from-bracket" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>
      Withdrawals
      <div id="withdrawalCount" style="font-size:11px;color:var(--text-dim);margin-top:4px;">Loading...</div>
    </a>
  </div>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('admin-dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
