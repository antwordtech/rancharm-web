with open('dashboard.html') as f:
    c = f.read()
before = c

old = '''  window.openDrawer = () => {'''

new = '''  const showcase = document.getElementById('ranchShowcase');
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

if old not in c:
    print('ANCHOR NOT FOUND - check manually')
c = c.replace(old, new, 1)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
