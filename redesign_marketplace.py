with open('marketplace.html') as f:
    c = f.read()
before = c

old = '''  <div class="nav-grid">
    <a class="nav-tile reveal" style="animation-delay:0.05s" href="data.html"><i class="fa-solid fa-wifi" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Data</a>
    <a class="nav-tile reveal" style="animation-delay:0.1s" href="airtime.html"><i class="fa-solid fa-mobile-screen" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Airtime</a>
    <a class="nav-tile reveal" style="animation-delay:0.15s" href="#" onclick="useService('ECG bill payment'); return false;"><i class="fa-solid fa-bolt" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>ECG</a>
    <a class="nav-tile reveal" style="animation-delay:0.2s" href="#" onclick="useService('Water bill payment'); return false;"><i class="fa-solid fa-droplet" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Water</a>
    <a class="nav-tile reveal" style="animation-delay:0.25s" href="utility.html"><i class="fa-solid fa-tv" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>TV</a>
    <a class="nav-tile reveal" style="animation-delay:0.3s" href="booster.html"><i class="fa-solid fa-rocket" style="color:var(--brand);display:block;font-size:20px;margin-bottom:8px;"></i>Booster</a>
  </div>'''

new = '''  <div class="service-list">
    <a class="service-row reveal" style="animation-delay:0.05s" href="airtime.html">
      <div class="service-icon-circle"><i class="fa-solid fa-mobile-screen"></i></div>
      <div>
        <div class="service-row-title">Airtime</div>
        <div class="service-row-desc">Top up any network instantly</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row reveal" style="animation-delay:0.1s" href="data.html">
      <div class="service-icon-circle"><i class="fa-solid fa-wifi"></i></div>
      <div>
        <div class="service-row-title">Data</div>
        <div class="service-row-desc">Bundles for MTN, Telecel, and AT</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row reveal" style="animation-delay:0.15s" href="utility.html">
      <div class="service-icon-circle"><i class="fa-solid fa-tv"></i></div>
      <div>
        <div class="service-row-title">TV Subscriptions</div>
        <div class="service-row-desc">Pay your DSTV or GOtv bill</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row reveal" style="animation-delay:0.2s" href="#" onclick="useService('ECG bill payment'); return false;">
      <div class="service-icon-circle"><i class="fa-solid fa-bolt"></i></div>
      <div>
        <div class="service-row-title">ECG Electricity</div>
        <div class="service-row-desc">Top up your prepaid meter</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row reveal" style="animation-delay:0.25s" href="#" onclick="useService('Water bill payment'); return false;">
      <div class="service-icon-circle"><i class="fa-solid fa-droplet"></i></div>
      <div>
        <div class="service-row-title">Ghana Water</div>
        <div class="service-row-desc">Pay your water bill</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row reveal" style="animation-delay:0.3s" href="booster.html">
      <div class="service-icon-circle"><i class="fa-solid fa-rocket"></i></div>
      <div>
        <div class="service-row-title">Social Booster</div>
        <div class="service-row-desc">Followers, likes &amp; views for socials</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
  </div>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('marketplace.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
