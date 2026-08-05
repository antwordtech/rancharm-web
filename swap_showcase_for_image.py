with open('dashboard.html') as f:
    c = f.read()
before = c

old_markup = '''  <div class="section-title">Meet the Ranch</div>
  <div class="ranch-showcase" id="ranchShowcase"></div>
</div>'''

new_markup = '''  <img src="ranch-illustration.png" style="width:100%;border-radius:20px;margin-top:16px;" alt="Rancharm Farm">
</div>'''

if old_markup not in c:
    print('MARKUP NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

old_js = '''  const showcase = document.getElementById('ranchShowcase');
  ANIMALS.forEach(function(animal, i) {
    const item = document.createElement('div');
    item.className = 'ranch-showcase-item reveal';
    item.style.animationDelay = (i * 0.05) + 's';
    const animHtml = animal.lottie
      ? '<dotlottie-wc src="' + animal.lottie + '" autoplay loop style="width:64px;height:64px;"></dotlottie-wc>'
      : '<div style="width:64px;height:64px;border-radius:50%;background:var(--brand);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;">' + animal.name.charAt(0) + '</div>';
    item.innerHTML =
      '<div class="ranch-showcase-anim" style="animation-delay:' + (i * 0.4) + 's;">' + animHtml + '</div>' +
      '<div class="ranch-showcase-name">' + animal.name + '</div>';
    showcase.appendChild(item);
  });

  window.openDrawer = () => {'''

new_js = '''  window.openDrawer = () => {'''

if old_js not in c:
    print('JS NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
