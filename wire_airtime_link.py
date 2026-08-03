with open('marketplace.html') as f:
    c = f.read()
before = c

old = '''<a class="nav-tile reveal" style="animation-delay:0.1s" href="#" onclick="useService('Airtime'); return false;"><i class="fa-solid fa-mobile-screen" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Airtime</a>'''
new = '''<a class="nav-tile reveal" style="animation-delay:0.1s" href="airtime.html"><i class="fa-solid fa-mobile-screen" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Airtime</a>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('marketplace.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
