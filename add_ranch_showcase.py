with open('dashboard.html') as f:
    c = f.read()
before = c

old_markup = '''    <a class="nav-tile reveal" style="animation-delay:0.3s" href="marketplace.html"><i class="fa-solid fa-fire" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Marketplace</a>
  </div>
</div>'''

new_markup = '''    <a class="nav-tile reveal" style="animation-delay:0.3s" href="marketplace.html"><i class="fa-solid fa-fire" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Marketplace</a>
  </div>

  <div class="section-title">Meet the Ranch</div>
  <div class="ranch-showcase" id="ranchShowcase"></div>
</div>'''

if old_markup not in c:
    print('MARKUP NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
