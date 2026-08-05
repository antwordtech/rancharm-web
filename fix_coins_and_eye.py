with open('dashboard.html') as f:
    c = f.read()
before = c

# 1) Persist eye-icon state
old_eye = '''  let balanceHidden = false;
  let lastCoins = 0;
  window.toggleBalanceVisibility = () => {
    balanceHidden = !balanceHidden;
    document.getElementById('coinsDisplay').textContent = balanceHidden ? '••••' : lastCoins.toLocaleString();
    document.getElementById('eyeIcon').className = balanceHidden ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye';
  };'''

new_eye = '''  let balanceHidden = localStorage.getItem('rancharm-balance-hidden') === 'true';
  let lastCoins = 0;
  window.toggleBalanceVisibility = () => {
    balanceHidden = !balanceHidden;
    localStorage.setItem('rancharm-balance-hidden', balanceHidden);
    document.getElementById('coinsDisplay').textContent = balanceHidden ? '••••' : lastCoins.toLocaleString();
    document.getElementById('eyeIcon').className = balanceHidden ? 'fa-solid fa-eye-slash' : 'fa-solid fa-eye';
  };'''

if old_eye not in c:
    print('EYE PATTERN NOT FOUND - check manually')
c = c.replace(old_eye, new_eye)

# 2) Derive Coins/Points from the single real points value instead of the dead wallet.coins field
old_lastcoins = '    lastCoins = wallet.coins;'
new_lastcoins = '''    const walletCoins = Math.floor((wallet.points || 0) / 1000);
    const walletRemainderPoints = (wallet.points || 0) % 1000;
    lastCoins = walletCoins;'''
if old_lastcoins not in c:
    print('LASTCOINS NOT FOUND - check manually')
c = c.replace(old_lastcoins, new_lastcoins)

old_animate = '''    animateNumber('pointsDisplay', wallet.points);
    animateNumber('coinsDisplay', wallet.coins);'''
new_animate = '''    animateNumber('pointsDisplay', walletRemainderPoints);
    if (!balanceHidden) {
      animateNumber('coinsDisplay', walletCoins);
    } else {
      document.getElementById('coinsDisplay').textContent = '••••';
      document.getElementById('eyeIcon').className = 'fa-solid fa-eye-slash';
    }'''
if old_animate not in c:
    print('ANIMATE NOT FOUND - check manually')
c = c.replace(old_animate, new_animate)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
