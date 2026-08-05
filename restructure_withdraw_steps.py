with open('withdraw.html') as f:
    c = f.read()
before = c

old_markup = '''  <div id="formView">
    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Amount (GHS)</label>
    <input type="number" id="withdrawAmount" placeholder="e.g. 20" oninput="onAmountInput()">
    <div style="font-size:12px;color:var(--text-dim);margin:-8px 0 16px 4px;min-height:16px;" id="pointsNeeded"></div>

    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Mobile Money Number</label>
    <input type="tel" id="withdrawPhone" placeholder="Enter your number" oninput="onPhoneInput()">
    <div style="font-size:12px;color:var(--brand-dark);font-weight:700;margin:-8px 0 16px 4px;min-height:16px;" id="networkLabel"></div>

    <button id="submitBtn" onclick="submitWithdrawal()">Request Withdrawal</button>
  </div>

  <div id="successView" style="display:none;text-align:center;padding:40px 0;">'''

new_markup = '''  <div id="formView">
    <div class="step-dots">
      <div class="step-dot active" id="dot1"></div>
      <div class="step-dot" id="dot2"></div>
      <div class="step-dot" id="dot3"></div>
    </div>

    <div id="step1" class="kyc-step">
      <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Amount (GHS)</label>
      <input type="number" id="withdrawAmount" placeholder="e.g. 20" oninput="onAmountInput()">
      <div style="font-size:12px;color:var(--text-dim);margin:-8px 0 16px 4px;min-height:16px;" id="pointsNeeded"></div>
      <button id="nextBtn" onclick="goToAmountNext()">Next</button>
    </div>

    <div id="step2" class="kyc-step" style="display:none;">
      <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;">Mobile Money Number</label>
      <input type="tel" id="withdrawPhone" placeholder="Enter your number" oninput="onPhoneInput()">
      <div style="font-size:12px;color:var(--brand-dark);font-weight:700;margin:-8px 0 16px 4px;min-height:16px;" id="networkLabel"></div>
      <button id="submitBtn" onclick="submitWithdrawal()">Request Withdrawal</button>
    </div>
  </div>

  <div id="step3" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">'''

if old_markup not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

# The old successView id is no longer used as a separate sibling; rename its remaining references
c = c.replace('id="successView"', 'id="step3View"')

with open('withdraw.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
