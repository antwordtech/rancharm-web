with open('data.html') as f:
    c = f.read()
before = c

old_markup = '''  <div id="searchView">
    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Phone Number</label>
    <input type="tel" id="dataPhone" placeholder="Enter your number" oninput="onPhoneInput()">
    <div style="font-size:12px;color:var(--brand-dark);font-weight:700;margin:-8px 0 16px 4px;min-height:16px;" id="networkLabel"></div>

    <button id="findBtn" onclick="findBundles()">Find Bundles</button>

    <div id="bundleList" style="margin-top:20px;"></div>
  </div>

  <div id="successView" style="display:none;text-align:center;padding:40px 0;">
    <i class="fa-solid fa-circle-check" style="font-size:48px;color:var(--brand);margin-bottom:16px;"></i>
    <div style="font-weight:800;font-size:18px;margin-bottom:8px;">Data Sent!</div>
    <div style="font-size:13px;color:var(--text-dim);margin-bottom:24px;" id="successText">Delivered successfully.</div>
    <button onclick="window.location.href='marketplace.html'">Back to Marketplace</button>
  </div>
</div>'''

new_markup = '''  <div class="step-dots">
    <div class="step-dot active" id="dot1"></div>
    <div class="step-dot" id="dot2"></div>
    <div class="step-dot" id="dot3"></div>
  </div>

  <div id="step1" class="kyc-step">
    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Phone Number</label>
    <input type="tel" id="dataPhone" placeholder="Enter your number" oninput="onPhoneInput()">
    <div style="font-size:12px;color:var(--brand-dark);font-weight:700;margin:-8px 0 16px 4px;min-height:16px;" id="networkLabel"></div>

    <button id="findBtn" onclick="findBundles()">Find Bundles</button>
  </div>

  <div id="step2" class="kyc-step" style="display:none;">
    <div id="bundleList"></div>
    <div class="step-back" onclick="goToStep(1)" style="margin-top:16px;">Back</div>
  </div>

  <div id="step3" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">
    <i class="fa-solid fa-circle-check" style="font-size:48px;color:var(--brand);margin-bottom:16px;"></i>
    <div style="font-weight:800;font-size:18px;margin-bottom:8px;">Data Sent!</div>
    <div style="font-size:13px;color:var(--text-dim);margin-bottom:24px;" id="successText">Delivered successfully.</div>
    <button onclick="window.location.href='marketplace.html'">Back to Marketplace</button>
  </div>
</div>'''

if old_markup not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

# Add goToStep helper and wire findBundles/buyBundle to transition steps
old_js_start = "  window.onPhoneInput = function() {"
new_js_start = '''  window.goToStep = function(n) {
    [1, 2, 3].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };

  window.onPhoneInput = function() {'''

if old_js_start not in c:
    print('JS START PATTERN NOT FOUND - check manually')
c = c.replace(old_js_start, new_js_start)

old_find_tail = '''      list.innerHTML = '';
      bundles.forEach(function(b, i) {'''
new_find_tail = '''      list.innerHTML = '';
      goToStep(2);
      bundles.forEach(function(b, i) {'''
if old_find_tail not in c:
    print('FIND TAIL PATTERN NOT FOUND - check manually')
c = c.replace(old_find_tail, new_find_tail)

old_buy_success = '''        document.getElementById('successText').textContent = 'Data bundle sent to ' + currentPhone + '.';
        document.getElementById('searchView').style.display = 'none';
        document.getElementById('successView').style.display = 'block';'''
new_buy_success = '''        document.getElementById('successText').textContent = 'Data bundle sent to ' + currentPhone + '.';
        goToStep(3);'''
if old_buy_success not in c:
    print('BUY SUCCESS PATTERN NOT FOUND - check manually')
c = c.replace(old_buy_success, new_buy_success)

with open('data.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
