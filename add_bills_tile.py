with open('marketplace.html') as f:
    c = f.read()
before = c

old = '''<a class="nav-tile reveal" style="animation-delay:0.2s" href="#" onclick="useService('Water bill payment'); return false;"><i class="fa-solid fa-droplet" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Water</a>'''
new = old + '''
    <a class="nav-tile reveal" style="animation-delay:0.25s" href="utility.html"><i class="fa-solid fa-tv" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>TV / Internet</a>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('marketplace.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
