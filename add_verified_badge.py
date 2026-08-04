with open('dashboard.html') as f:
    c = f.read()
before = c

old = '''    <div class="drawer-avatar" id="drawerAvatar">?</div>
    <div>
      <div class="drawer-email" id="drawerEmail">...</div>
      <div class="drawer-tier" id="drawerTier">...</div>
    </div>'''

new = '''    <div class="drawer-avatar" id="drawerAvatar">?</div>
    <div>
      <div class="drawer-email-row">
        <div class="drawer-email" id="drawerEmail">...</div>
        <i class="fa-solid fa-circle-check verified-badge-icon" id="verifiedBadge" style="display:none;" title="Verified"></i>
      </div>
      <div class="drawer-tier" id="drawerTier">...</div>
    </div>'''

if old not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

old_js = "document.getElementById('drawerEmail').textContent = user.email || '...';"
new_js = '''document.getElementById('drawerEmail').textContent = user.email || '...';
    if (profile.subscriptionTier && profile.subscriptionTier !== 'free') {
      document.getElementById('verifiedBadge').style.display = 'inline-block';
    }'''
if old_js not in c:
    print('JS PATTERN NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
