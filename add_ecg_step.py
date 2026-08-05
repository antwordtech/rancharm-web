with open('ecg.html') as f:
    c = f.read()
before = c

# 1) Add a 4th dot
old_dots = '''    <div class="step-dot active" id="dot1"></div>
    <div class="step-dot" id="dot2"></div>
    <div class="step-dot" id="dot3"></div>'''
new_dots = '''    <div class="step-dot active" id="dot1"></div>
    <div class="step-dot" id="dot2"></div>
    <div class="step-dot" id="dot3"></div>
    <div class="step-dot" id="dot4"></div>'''
if old_dots not in c:
    print('DOTS NOT FOUND - check manually')
c = c.replace(old_dots, new_dots)

# 2) Move meterList out of step1 into its own new step2; renumber step2->step3, step3->step4
old_step1 = '''  <div id="step1" class="kyc-step">
    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Phone Number</label>
    <input type="tel" id="ecgPhone" placeholder="Enter your number">
    <button id="findBtn" onclick="findMeters()" style="margin-top:16px;">Find Meters</button>
    <div id="meterList" style="margin-top:20px;"></div>
  </div>

  <div id="step2" class="kyc-step" style="display:none;">
    <div class="verified-name-box" style="margin-bottom:20px;">
      <div style="font-size:11px;color:var(--text-dim);margin-bottom:4px;">Meter</div>
      <div class="verified-name-value" id="selectedMeterName">-</div>
      <div style="font-size:12px;color:var(--text-dim);margin-top:6px;" id="selectedMeterBalance"></div>
    </div>

    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Amount (GHS)</label>
    <input type="number" id="ecgAmount" placeholder="e.g. 20" oninput="onAmountInput()">
    <div style="font-size:12px;color:var(--text-dim);margin:-8px 0 16px 4px;min-height:16px;" id="costLabel"></div>

    <button id="payBtn" onclick="payEcg()">Top Up Meter</button>
  </div>

  <div id="step3" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">'''

new_step1 = '''  <div id="step1" class="kyc-step">
    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Phone Number</label>
    <input type="tel" id="ecgPhone" placeholder="Enter your number">
    <button id="findBtn" onclick="findMeters()" style="margin-top:16px;">Find Meters</button>
  </div>

  <div id="step2" class="kyc-step" style="display:none;">
    <div id="meterList"></div>
  </div>

  <div id="step3" class="kyc-step" style="display:none;">
    <div class="verified-name-box" style="margin-bottom:20px;">
      <div style="font-size:11px;color:var(--text-dim);margin-bottom:4px;">Meter</div>
      <div class="verified-name-value" id="selectedMeterName">-</div>
      <div style="font-size:12px;color:var(--text-dim);margin-top:6px;" id="selectedMeterBalance"></div>
    </div>

    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Amount (GHS)</label>
    <input type="number" id="ecgAmount" placeholder="e.g. 20" oninput="onAmountInput()">
    <div style="font-size:12px;color:var(--text-dim);margin:-8px 0 16px 4px;min-height:16px;" id="costLabel"></div>

    <button id="payBtn" onclick="payEcg()">Top Up Meter</button>
  </div>

  <div id="step4" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">'''

if old_step1 not in c:
    print('STEP1 NOT FOUND - check manually')
c = c.replace(old_step1, new_step1)

# 3) Update JS: goToStep handles 4 steps, headerBack, findMeters transitions to step2, selectMeterClick moves to step3
old_gotostep = '''  window.goToStep = function(n) {
    currentStep = n;
    [1, 2, 3].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };

  window.headerBack = function() {
    if (currentStep > 1 && currentStep < 3) {
      goToStep(currentStep - 1);
    } else {
      window.location.href = 'marketplace.html';
    }
  };'''

new_gotostep = '''  window.goToStep = function(n) {
    currentStep = n;
    [1, 2, 3, 4].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };

  window.headerBack = function() {
    if (currentStep > 1 && currentStep < 4) {
      goToStep(currentStep - 1);
    } else {
      window.location.href = 'marketplace.html';
    }
  };'''

if old_gotostep not in c:
    print('GOTOSTEP NOT FOUND - check manually')
c = c.replace(old_gotostep, new_gotostep)

old_find_tail = '''      list.innerHTML = '';
      meters.forEach(function(m, i) {'''
new_find_tail = '''      list.innerHTML = '';
      goToStep(2);
      meters.forEach(function(m, i) {'''
if old_find_tail not in c:
    print('FIND TAIL NOT FOUND - check manually')
c = c.replace(old_find_tail, new_find_tail)

old_select = '''  window.selectMeterClick = function(btn) {
    selectedMeter = btn.dataset.meter;
    document.getElementById('selectedMeterName').textContent = btn.dataset.name + ' (' + selectedMeter + ')';
    document.getElementById('selectedMeterBalance').textContent = 'Current balance: GHS ' + btn.dataset.balance;
    goToStep(2);
  };'''
new_select = '''  window.selectMeterClick = function(btn) {
    selectedMeter = btn.dataset.meter;
    document.getElementById('selectedMeterName').textContent = btn.dataset.name + ' (' + selectedMeter + ')';
    document.getElementById('selectedMeterBalance').textContent = 'Current balance: GHS ' + btn.dataset.balance;
    goToStep(3);
  };'''
if old_select not in c:
    print('SELECT NOT FOUND - check manually')
c = c.replace(old_select, new_select)

# 4) payEcg success now targets step4
old_success = "document.getElementById('successText').textContent = 'GHS ' + amount + ' credited to meter ' + selectedMeter + '.';\n        goToStep(3);"
new_success = "document.getElementById('successText').textContent = 'GHS ' + amount + ' credited to meter ' + selectedMeter + '.';\n        goToStep(4);"
if old_success not in c:
    print('SUCCESS GOTO NOT FOUND - check manually')
c = c.replace(old_success, new_success)

with open('ecg.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
