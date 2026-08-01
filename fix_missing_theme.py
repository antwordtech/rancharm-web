theme_script = '''<script>
(function(){
  var t = localStorage.getItem('rancharm-theme');
  if (t === 'dark') document.documentElement.classList.add('theme-dark');
  else if (t === 'light') document.documentElement.classList.add('theme-light');
  var meta = document.querySelector('meta[name="theme-color"]');
  if (meta) {
    var isDark = document.documentElement.classList.contains('theme-dark') ||
      (!document.documentElement.classList.contains('theme-light') && window.matchMedia('(prefers-color-scheme: dark)').matches);
    meta.setAttribute('content', isDark ? '#0b1210' : '#0f9d8c');
  }
})();
</script>
'''

# kyc.html: insert right before toast.js
with open('kyc.html') as f:
    c = f.read()
before = c
marker = '<script src="toast.js?v=2"></script>'
if marker in c:
    c = c.replace(marker, theme_script + marker, 1)
else:
    print('kyc.html: MARKER NOT FOUND - check manually')
with open('kyc.html', 'w') as f:
    f.write(c)
print('kyc.html', 'OK' if c != before else 'NO CHANGE')

# index.html: insert right before closing </head>
with open('index.html') as f:
    c = f.read()
before = c
marker2 = '</head>'
if marker2 in c:
    c = c.replace(marker2, theme_script + marker2, 1)
else:
    print('index.html: MARKER NOT FOUND - check manually')
with open('index.html', 'w') as f:
    f.write(c)
print('index.html', 'OK' if c != before else 'NO CHANGE')
