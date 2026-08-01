files = ["dashboard.html", "ranch-store.html", "my-ranch.html", "tasks.html",
         "referrals.html", "profile.html", "leaderboard.html", "marketplace.html"]

old_footer = '''  <div class="drawer-footer">
    <button class="btn-logout" onclick="logout()"><i class="fa-solid fa-right-from-bracket"></i> Log Out</button>
  </div>
</div>'''

new_footer = '''  <div class="drawer-footer">
    <div class="drawer-link" style="cursor:pointer;" onclick="confirmLogout()">
      <i class="fa-solid fa-right-from-bracket" style="background:rgba(244,63,94,0.1);color:#f43f5e;"></i>
      <span style="color:#f43f5e;">Log Out</span>
    </div>
  </div>
</div>

<div class="logout-modal-backdrop" id="logoutModalBackdrop" onclick="closeLogoutModal(event)">
  <div class="logout-modal" onclick="event.stopPropagation()">
    <div class="logout-modal-icon"><i class="fa-solid fa-right-from-bracket"></i></div>
    <div class="logout-modal-title">Log Out?</div>
    <div class="logout-modal-text">Are you sure you want to log out of Rancharm?</div>
    <div class="logout-modal-actions">
      <button class="btn-outline" onclick="closeLogoutModal()">Cancel</button>
      <button class="btn-danger" onclick="doLogout()">Log Out</button>
    </div>
  </div>
</div>'''

old_js = '''  window.logout = async () => {
    await signOut(auth);
    window.location.href = 'login.html';
  };'''

new_js = '''  window.confirmLogout = () => {
    document.getElementById('logoutModalBackdrop').classList.add('open');
  };
  window.closeLogoutModal = (e) => {
    if (e && e.target !== e.currentTarget) return;
    document.getElementById('logoutModalBackdrop').classList.remove('open');
  };
  window.doLogout = async () => {
    await signOut(auth);
    window.location.href = 'login.html';
  };'''

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c
    if old_footer not in c:
        print(fname, 'FOOTER PATTERN NOT FOUND - check manually')
    c = c.replace(old_footer, new_footer)
    if old_js not in c:
        print(fname, 'JS PATTERN NOT FOUND - check manually')
    c = c.replace(old_js, new_js)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')

print("DONE")
