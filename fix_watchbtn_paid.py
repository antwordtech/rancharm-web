with open('my-ranch.html') as f:
    c = f.read()
before = c

old = '''    const watchBtn = document.getElementById('watchAdBtn');
    if (adsToday >= adsRequired) {
      watchBtn.disabled = true;
      watchBtn.innerHTML = 'All Ads Watched Today';
    } else {
      watchBtn.disabled = false;
      watchBtn.innerHTML = 'Watch Ad (' + adsToday + '/' + adsRequired + ')';
      watchBtn.onclick = window.watchAd;
    }'''

new = '''    const watchBtn = document.getElementById('watchAdBtn');
    if (isPaidSub) {
      watchBtn.disabled = true;
      watchBtn.innerHTML = 'Ads Removed';
    } else if (adsToday >= adsRequired) {
      watchBtn.disabled = true;
      watchBtn.innerHTML = 'All Ads Watched Today';
    } else {
      watchBtn.disabled = false;
      watchBtn.innerHTML = 'Watch Ad (' + adsToday + '/' + adsRequired + ')';
      watchBtn.onclick = window.watchAd;
    }'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
