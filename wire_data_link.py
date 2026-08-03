with open('marketplace.html') as f:
    c = f.read()
before = c

old = '''<a class="nav-tile reveal" style="animation-delay:0.05s" href="#" onclick="useService('Data bundles'); return false;"><i class="fa-solid fa-wifi" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Data</a>'''
new = '''<a class="nav-tile reveal" style="animation-delay:0.05s" href="data.html"><i class="fa-solid fa-wifi" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Data</a>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('marketplace.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
