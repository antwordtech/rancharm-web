import re

loader_files = ["login.html","complete-profile.html","ranch-store.html","my-ranch.html","tasks.html","referrals.html","profile.html"]
drawer_files = ["ranch-store.html","my-ranch.html","tasks.html","referrals.html","profile.html"]

loader_div = '<div class="page-loader" id="pageLoader"><i class="fa-solid fa-spinner fa-spin" style="font-size:32px;color:var(--brand);"></i></div>'
meta_theme = '<meta name="theme-color" content="#ffffff" id="metaTheme">'

for fname in loader_files:
    with open(fname) as f:
        c = f.read()
    before = c
    c = c.replace('<body>\n', '<body>\n' + loader_div + '\n', 1)
    c = re.sub(r'(<meta name="viewport"[^>]*>\n)', r'\1' + meta_theme + '\n', c, count=1)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, "OK" if c != before else "NO CHANGE - check manually")

old_script = '''<script>
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

new_script = '''<script>
function syncThemeColor(){
  var meta = document.getElementById('metaTheme');
  if (!meta) return;
  var isDark = document.documentElement.classList.contains('theme-dark') ||
    (!document.documentElement.classList.contains('theme-light') && window.matchMedia('(prefers-color-scheme: dark)').matches);
  meta.setAttribute('content', isDark ? '#0b1210' : '#ffffff');
}
(function(){
  var t = localStorage.getItem('rancharm-theme');
  if (t === 'dark') document.documentElement.classList.add('theme-dark');
  else if (t === 'light') document.documentElement.classList.add('theme-light');
  syncThemeColor();
})();
window.toggleTheme = function() {
  var html = document.documentElement;
  var isDark = html.classList.contains('theme-dark');
  html.classList.remove('theme-dark','theme-light');
  if (isDark) { html.classList.add('theme-light'); localStorage.setItem('rancharm-theme','light'); }
  else { html.classList.add('theme-dark'); localStorage.setItem('rancharm-theme','dark'); }
  syncThemeSwitch();
  syncThemeColor();
};
function syncThemeSwitch(){
  var sw = document.getElementById('themeSwitch');
  if (!sw) return;
  var isDark = document.documentElement.classList.contains('theme-dark') ||
    (!document.documentElement.classList.contains('theme-light') && window.matchMedia('(prefers-color-scheme: dark)').matches);
  sw.classList.toggle('on', isDark);
}
document.addEventListener('DOMContentLoaded', function(){ syncThemeSwitch(); syncThemeColor(); });
</script>'''

for fname in drawer_files:
    with open(fname) as f:
        c = f.read()
    before = c
    c = c.replace(old_script, new_script)
    c = c.replace('<i class="fa-solid fa-store"></i>Ranch Store', '<i class="fa-solid fa-store"></i>Store')
    c = c.replace('  <div class="drawer-section-label">More</div>\n', '')
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, "drawer updated" if c != before else "NO CHANGE - check manually")

minimal_script = '''<script>
(function(){
  var t = localStorage.getItem('rancharm-theme');
  if (t === 'dark') document.documentElement.classList.add('theme-dark');
  else if (t === 'light') document.documentElement.classList.add('theme-light');
  var meta = document.getElementById('metaTheme');
  if (meta) {
    var isDark = document.documentElement.classList.contains('theme-dark') ||
      (!document.documentElement.classList.contains('theme-light') && window.matchMedia('(prefers-color-scheme: dark)').matches);
    meta.setAttribute('content', isDark ? '#0b1210' : '#ffffff');
  }
})();
</script>'''

for fname in ["login.html","complete-profile.html"]:
    with open(fname) as f:
        c = f.read()
    before = c
    c = c.replace('<script src="toast.js?v=2"></script>', minimal_script + '\n<script src="toast.js?v=2"></script>')
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, "theme init added" if c != before else "NO CHANGE - check manually")

print("DONE")
