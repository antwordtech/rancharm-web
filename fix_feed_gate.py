with open('my-ranch.html') as f:
    c = f.read()
before = c

old = '''    const feedBtn = document.getElementById('feedBtn');
    const kycApproved = (data.kycStatus || 'unverified') === 'approved';

    if (!kycApproved) {
      feedBtn.disabled = false;
      feedBtn.innerHTML = 'Verify Identity to Earn';
      feedBtn.onclick = () => { window.location.href = 'kyc.html'; };
    } else {
      const today = new Date().toISOString().split('T')[0];
      const fedToday = data.lastFedDate === today;
      feedBtn.disabled = fedToday;
      feedBtn.innerHTML = fedToday ? 'Already Fed Today' : 'Feed Now';
      feedBtn.onclick = window.feedAnimal;
    }
  }'''

new = '''    const feedBtn = document.getElementById('feedBtn');
    const today = new Date().toISOString().split('T')[0];
    const fedToday = data.lastFedDate === today;
    feedBtn.disabled = fedToday;
    feedBtn.innerHTML = fedToday ? 'Already Fed Today' : 'Feed Now';
    feedBtn.onclick = window.feedAnimal;
  }'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
