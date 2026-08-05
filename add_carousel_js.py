with open('dashboard.html') as f:
    c = f.read()
before = c

old = '''  window.openDrawer = () => {'''

new = '''  let howIndex = 0;
  setInterval(function() {
    howIndex = (howIndex + 1) % 4;
    document.getElementById('howTrack').style.transform = 'translateX(-' + (howIndex * 100) + '%)';
    [1, 2, 3, 4].forEach(function(i) {
      document.getElementById('howDot' + i).classList.toggle('active', i === howIndex + 1);
    });
  }, 5000);

  window.openDrawer = () => {'''

if old not in c:
    print('ANCHOR NOT FOUND - check manually')
c = c.replace(old, new, 1)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
