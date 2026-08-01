with open('my-ranch.html') as f:
    c = f.read()
before = c

old = '''    const adsToday = (data.adsWatchedDate === today) ? (data.adsWatchedCount || 0) : 0;
    document.getElementById('adsProgressText').textContent = adsToday + ' / 5 ads watched';
    document.getElementById('adsProgressFill').style.width = Math.min(100, (adsToday / 5) * 100) + '%';

    const watchBtn = document.getElementById('watchAdBtn');
    if (adsToday >= 5) {
      watchBtn.disabled = true;
      watchBtn.innerHTML = 'All Ads Watched Today';
    } else {
      watchBtn.disabled = false;
      watchBtn.innerHTML = 'Watch Ad (' + adsToday + '/5)';
      watchBtn.onclick = window.watchAd;
    }

    if (fedToday) {
      feedBtn.disabled = true;
      feedBtn.innerHTML = 'Already Fed Today';
    } else if (adsToday < 5) {
      feedBtn.disabled = true;
      feedBtn.innerHTML = 'Watch 5 Ads First';
    } else {
      feedBtn.disabled = false;
      feedBtn.innerHTML = 'Feed Now';
      feedBtn.onclick = window.feedAnimal;
    }
  }'''

new = '''    const adsRequired = (tierKey === 'cock') ? 10 : 5;
    const adsToday = (data.adsWatchedDate === today) ? (data.adsWatchedCount || 0) : 0;
    document.getElementById('adsProgressText').textContent = adsToday + ' / ' + adsRequired + ' ads watched';
    document.getElementById('adsProgressFill').style.width = Math.min(100, (adsToday / adsRequired) * 100) + '%';

    const watchBtn = document.getElementById('watchAdBtn');
    if (adsToday >= adsRequired) {
      watchBtn.disabled = true;
      watchBtn.innerHTML = 'All Ads Watched Today';
    } else {
      watchBtn.disabled = false;
      watchBtn.innerHTML = 'Watch Ad (' + adsToday + '/' + adsRequired + ')';
      watchBtn.onclick = window.watchAd;
    }

    if (fedToday) {
      feedBtn.disabled = true;
      feedBtn.innerHTML = 'Already Fed Today';
    } else if (adsToday < adsRequired) {
      feedBtn.disabled = true;
      feedBtn.innerHTML = 'Watch ' + adsRequired + ' Ads First';
    } else {
      feedBtn.disabled = false;
      feedBtn.innerHTML = 'Feed Now';
      feedBtn.onclick = window.feedAnimal;
    }
  }'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
