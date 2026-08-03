with open('marketplace.html') as f:
    c = f.read()
before = c

old = '''<a class="nav-tile reveal" style="animation-delay:0.25s" href="utility.html"><i class="fa-solid fa-tv" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>TV</a>'''
new = old + '''
    <a class="nav-tile reveal" style="animation-delay:0.3s" href="booster.html"><i class="fa-solid fa-rocket" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Booster</a>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('marketplace.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
