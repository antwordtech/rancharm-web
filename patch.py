files = ["ranch-store.html", "my-ranch.html", "tasks.html", "referrals.html", "profile.html"]

head_insert = '''<link rel="stylesheet" href="styles.css?v=2">
<script>
(function(){
  var t = localStorage.getItem('rancharm-theme');
  if (t === 'dark') document.documentElement.classList.add('theme-dark');
  else if (t === 'light') document.documentElement.classList.add('theme-light');
})();
window.toggleTheme = function() {
  var html = document.documentElement;
  var isDark = html.classList.contains('theme-dark');
  html.classList.remove('theme-dark','theme-light');
  if (isDark) { html.classList.add('theme-light'); localStorage.setItem('rancharm-theme','light'); }
  else { html.classList.add('theme-dark'); localStorage.setItem('rancharm-theme','dark'); }
  syncThemeSwitch();
};
function syncThemeSwitch(){
  var sw = document.getElementById('themeSwitch');
  if (!sw) return;
  var isDark = document.documentElement.classList.contains('theme-dark') ||
    (!document.documentElement.classList.contains('theme-light') && window.matchMedia('(prefers-color-scheme: dark)').matches);
  sw.classList.toggle('on', isDark);
}
document.addEventListener('DOMContentLoaded', syncThemeSwitch);
</script>'''

old_toggle = """  window.openDrawer = () => {
    document.getElementById('drawerBackdrop').classList.add('open');
    document.getElementById('drawerPanel').classList.add('open');
  };
  window.closeDrawer = () => {
    document.getElementById('drawerBackdrop').classList.remove('open');
    document.getElementById('drawerPanel').classList.remove('open');
  };"""

new_toggle = """  window.openDrawer = () => {
    document.getElementById('drawerBackdrop').classList.add('open');
    document.getElementById('drawerPanel').classList.add('open');
    document.body.classList.add('drawer-open');
  };
  window.closeDrawer = () => {
    document.getElementById('drawerBackdrop').classList.remove('open');
    document.getElementById('drawerPanel').classList.remove('open');
    document.body.classList.remove('drawer-open');
  };"""

old_footer = """  <div class="drawer-footer">
    <button class="btn-danger" onclick="logout()"><i class="fa-solid fa-right-from-bracket"></i> Log Out</button>
  </div>"""

new_footer = """  <div class="drawer-section-label">More</div>
  <div class="drawer-link" style="cursor:pointer;" onclick="toggleTheme()">
    <i class="fa-solid fa-moon"></i>
    <span style="flex:1;">Dark Mode</span>
    <span class="theme-switch" id="themeSwitch"><span class="theme-switch-knob"></span></span>
  </div>
  <a class="drawer-link" href="#" onclick="toast('Withdrawals coming soon'); return false;"><i class="fa-solid fa-arrow-up-from-bracket"></i>Withdraw</a>
  <div class="drawer-footer">
    <button class="btn-logout" onclick="logout()"><i class="fa-solid fa-right-from-bracket"></i> Log Out</button>
  </div>"""

for fname in files:
    with open(fname) as f:
        content = f.read()

    before = content
    content = content.replace('<link rel="stylesheet" href="styles.css?v=2">', head_insert)
    content = content.replace(old_toggle, new_toggle)
    content = content.replace(old_footer, new_footer)
    content = content.replace("' — Ranch Level'", "' · Ranch Level'")
    content = content.replace("Rancharm — ", "Rancharm ")

    with open(fname, 'w') as f:
        f.write(content)

    print(fname, "changed" if content != before else "NO CHANGE (check manually)")
