with open('marketplace.html') as f:
    c = f.read()
before = c

# 1) Title text
c = c.replace('<title>Rancharm Marketplace</title>', '<title>Rancharm Marketplace</title>')

# 2) Replace the page body (subscription list) with a utility services grid
old_page = '''<div class="page">
  <div class="section-title" style="margin-top:0">Marketplace</div>
  <div id="subsList">
    <div class="skeleton" style="height:140px;margin-bottom:14px;"></div>
    <div class="skeleton" style="height:140px;margin-bottom:14px;"></div>
  </div>
</div>'''

new_page = '''<div class="page">
  <div class="section-title" style="margin-top:0">Marketplace</div>
  <div class="referral-earn-note reveal">
    <i class="fa-solid fa-circle-info" style="margin-right:6px;color:var(--brand);"></i>
    Buy data, airtime, and pay bills using your Ranch Coins.
  </div>
  <div class="nav-grid">
    <a class="nav-tile reveal" style="animation-delay:0.05s" href="#" onclick="useService('Data bundles'); return false;"><i class="fa-solid fa-wifi" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Data</a>
    <a class="nav-tile reveal" style="animation-delay:0.1s" href="#" onclick="useService('Airtime'); return false;"><i class="fa-solid fa-mobile-screen" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Airtime</a>
    <a class="nav-tile reveal" style="animation-delay:0.15s" href="#" onclick="useService('ECG bill payment'); return false;"><i class="fa-solid fa-bolt" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>ECG</a>
    <a class="nav-tile reveal" style="animation-delay:0.2s" href="#" onclick="useService('Water bill payment'); return false;"><i class="fa-solid fa-droplet" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Water</a>
  </div>
</div>'''

if old_page not in c:
    print('PAGE PATTERN NOT FOUND - check manually')
c = c.replace(old_page, new_page)

# 3) Simplify the import (drop SUBSCRIPTIONS, keep ANIMALS for drawer tier display)
c = c.replace(
    "import { auth, getUserProfile, ANIMALS, SUBSCRIPTIONS } from './firebase-config.js?v=3';",
    "import { auth, getUserProfile, ANIMALS } from './firebase-config.js?v=3';"
)

# 4) Replace the render/subscribe logic with a simple useService toast
old_logic = '''    renderSubscriptions(profile.subscriptionTier || 'free');
    document.body.classList.add('ready');
  });

  function renderSubscriptions(currentSub) {
    const list = document.getElementById('subsList');
    list.innerHTML = '';

    SUBSCRIPTIONS.forEach((sub, i) => {
      const isCurrent = sub.key === currentSub;
      const benefitsHtml = sub.benefits.map(b =>
        `<div class="benefit-row"><i class="fa-solid fa-circle-check"></i> ${b}</div>`
      ).join('');

      const card = document.createElement('div');
      card.className = 'animal-detail-card reveal' + (isCurrent ? ' sub-card-current' : '');
      card.style.animationDelay = (i * 0.05) + 's';
      card.innerHTML = `
        <div class="animal-detail-top">
          <div>
            <div class="animal-detail-name">${sub.name}</div>
          </div>
        </div>
        <div class="animal-detail-price">${sub.price === 0 ? 'Free' : 'GHS ' + sub.price.toLocaleString() + '/month'}</div>
        <div class="animal-benefits">${benefitsHtml}</div>
        ${isCurrent ? '<div class="current-badge">Current Plan</div>' : `<button onclick="subscribe('${sub.key}')">Subscribe</button>`}
      `;
      list.appendChild(card);
    });
  }

  window.subscribe = (key) => {
    toast('Subscription payments coming later (deposit on hold for now)');
  };'''

new_logic = '''    document.body.classList.add('ready');
  });

  window.useService = (name) => {
    toast(name + ' coming soon');
  };'''

if old_logic not in c:
    print('LOGIC PATTERN NOT FOUND - check manually')
c = c.replace(old_logic, new_logic)

with open('marketplace.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
