with open('withdraw.html') as f:
    c = f.read()
before = c

# 1) Step2 button: change from submit to "Next"
old_step2_btn = '''      <button id="submitBtn" onclick="submitWithdrawal()">Request Withdrawal</button>
    </div>
  </div>

  <div id="step3" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">
    <i class="fa-solid fa-clock" style="font-size:48px;color:var(--brand);margin-bottom:16px;"></i>
    <div style="font-weight:800;font-size:18px;margin-bottom:8px;">Withdrawal Requested</div>
    <div style="font-size:13px;color:var(--text-dim);margin-bottom:24px;">We'll process your payout shortly.</div>
    <button onclick="window.location.href='dashboard.html'">Back to Dashboard</button>
  </div>
</div>'''

new_step2_btn = '''      <button onclick="goToPhoneNext()">Next</button>
    </div>

    <div id="step3" class="kyc-step" style="display:none;">
      <div class="verified-name-box" style="text-align:left;">
        <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
          <span style="color:var(--text-dim);font-size:13px;">Amount Requested</span>
          <span style="font-weight:700;" id="confirmAmount">-</span>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
          <span style="color:var(--text-dim);font-size:13px;">Network Fee (3%)</span>
          <span style="font-weight:700;" id="confirmNetworkFee">-</span>
        </div>
        <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
          <span style="color:var(--text-dim);font-size:13px;">Rancharm Fee (2%)</span>
          <span style="font-weight:700;" id="confirmRancharmFee">-</span>
        </div>
        <div style="display:flex;justify-content:space-between;padding-top:10px;border-top:1px solid var(--border);">
          <span style="font-weight:700;">You Receive</span>
          <span style="font-weight:800;color:var(--brand-dark);font-size:16px;" id="confirmPayout">-</span>
        </div>
      </div>
      <button id="submitBtn" onclick="submitWithdrawal()" style="margin-top:20px;">Confirm Withdrawal</button>
    </div>
  </div>

  <div id="step4" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">
    <i class="fa-solid fa-clock" style="font-size:48px;color:var(--brand);margin-bottom:16px;"></i>
    <div style="font-weight:800;font-size:18px;margin-bottom:8px;">Withdrawal Requested</div>
    <div style="font-size:13px;color:var(--text-dim);margin-bottom:24px;">We'll process your payout shortly.</div>
    <button onclick="window.location.href='dashboard.html'">Back to Dashboard</button>
  </div>
</div>'''

if old_step2_btn not in c:
    print('STEP2 BTN NOT FOUND - check manually')
c = c.replace(old_step2_btn, new_step2_btn)

# 2) goToStep: handle 3 interactive steps now
old_gotostep = '''  window.goToStep = function(n) {
    currentStep = n;
    [1, 2].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };'''
new_gotostep = '''  window.goToStep = function(n) {
    currentStep = n;
    [1, 2, 3].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };'''
if old_gotostep not in c:
    print('GOTOSTEP NOT FOUND - check manually')
c = c.replace(old_gotostep, new_gotostep)

# 3) headerBack: step back through all 3 steps
old_headerback = '''  window.headerBack = function() {
    if (currentStep === 2) {
      goToStep(1);
    } else {
      window.location.href = 'dashboard.html';
    }
  };'''
new_headerback = '''  window.headerBack = function() {
    if (currentStep > 1 && currentStep < 4) {
      goToStep(currentStep - 1);
    } else {
      window.location.href = 'dashboard.html';
    }
  };'''
if old_headerback not in c:
    print('HEADERBACK NOT FOUND - check manually')
c = c.replace(old_headerback, new_headerback)

# 4) Simplify onAmountInput (fee breakdown moves to step3 confirm screen)
old_amount_input = '''  window.onAmountInput = function() {
    const amount = parseFloat(document.getElementById('withdrawAmount').value);
    const label = document.getElementById('pointsNeeded');
    if (!amount || amount <= 0) { label.textContent = ''; return; }
    const needed = Math.round(amount * 100);
    const networkFee = Math.round(amount * 0.03 * 100) / 100;
    const rancharmFee = Math.round(amount * 0.02 * 100) / 100;
    const payout = Math.round((amount - networkFee - rancharmFee) * 100) / 100;
    label.innerHTML = 'Uses ' + needed.toLocaleString() + ' points &middot; Fee GHS ' + (networkFee + rancharmFee).toFixed(2) +
      ' (Network ' + networkFee.toFixed(2) + ' + Rancharm ' + rancharmFee.toFixed(2) + ') &middot; You receive GHS ' + payout.toFixed(2);
  };'''
new_amount_input = '''  window.onAmountInput = function() {
    const amount = parseFloat(document.getElementById('withdrawAmount').value);
    const label = document.getElementById('pointsNeeded');
    if (!amount || amount <= 0) { label.textContent = ''; return; }
    const needed = Math.round(amount * 100);
    label.textContent = 'Uses ' + needed.toLocaleString() + ' points';
  };

  window.goToPhoneNext = function() {
    const phone = document.getElementById('withdrawPhone').value.trim();
    if (!phone || !detectedNetwork) { toast('Enter your Mobile Money number', 'error'); return; }

    const amount = parseFloat(document.getElementById('withdrawAmount').value);
    const networkFee = Math.round(amount * 0.03 * 100) / 100;
    const rancharmFee = Math.round(amount * 0.02 * 100) / 100;
    const payout = Math.round((amount - networkFee - rancharmFee) * 100) / 100;

    document.getElementById('confirmAmount').textContent = 'GHS ' + amount.toFixed(2);
    document.getElementById('confirmNetworkFee').textContent = 'GHS ' + networkFee.toFixed(2);
    document.getElementById('confirmRancharmFee').textContent = 'GHS ' + rancharmFee.toFixed(2);
    document.getElementById('confirmPayout').textContent = 'GHS ' + payout.toFixed(2);

    goToStep(3);
  };'''
if old_amount_input not in c:
    print('AMOUNT INPUT NOT FOUND - check manually')
c = c.replace(old_amount_input, new_amount_input)

# 5) submitWithdrawal: no longer re-validates phone (already done in step2), targets step4 on success
old_submit = '''  window.submitWithdrawal = async function() {
    const amount = document.getElementById('withdrawAmount').value.trim();
    const phone = document.getElementById('withdrawPhone').value.trim();

    if (!amount || Number(amount) <= 0) { toast('Enter a valid amount', 'error'); return; }
    if (!phone || !detectedNetwork) { toast('Enter your Mobile Money number', 'error'); return; }

    const pointsNeeded = Math.round(Number(amount) * 100);
    if (pointsNeeded > currentPoints) { toast('Insufficient points balance', 'error'); return; }

    const btn = document.getElementById('submitBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting...';

    try {
      const res = await fetch(WORKER_URL + '/request-withdrawal', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          uid: currentUser.uid,
          amountGHS: amount,
          network: detectedNetwork,
          phone: phone
        })
      });
      const data = await res.json();

      if (data.ok) {
        document.getElementById('formView').style.display = 'none';
        document.getElementById('step3').style.display = 'block';
      } else {
        toast(data.error || 'Something went wrong. Try again.', 'error');
        btn.disabled = false;
        btn.innerHTML = 'Request Withdrawal';
      }
    } catch (e) {
      toast('Something went wrong. Try again.', 'error');
      btn.disabled = false;
      btn.innerHTML = 'Request Withdrawal';
    }
  };'''
new_submit = '''  window.submitWithdrawal = async function() {
    const amount = document.getElementById('withdrawAmount').value.trim();
    const phone = document.getElementById('withdrawPhone').value.trim();

    const btn = document.getElementById('submitBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Submitting...';

    try {
      const res = await fetch(WORKER_URL + '/request-withdrawal', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          uid: currentUser.uid,
          amountGHS: amount,
          network: detectedNetwork,
          phone: phone
        })
      });
      const data = await res.json();

      if (data.ok) {
        document.getElementById('formView').style.display = 'none';
        document.getElementById('step4').style.display = 'block';
      } else {
        toast(data.error || 'Something went wrong. Try again.', 'error');
        btn.disabled = false;
        btn.innerHTML = 'Confirm Withdrawal';
      }
    } catch (e) {
      toast('Something went wrong. Try again.', 'error');
      btn.disabled = false;
      btn.innerHTML = 'Confirm Withdrawal';
    }
  };'''
if old_submit not in c:
    print('SUBMIT NOT FOUND - check manually')
c = c.replace(old_submit, new_submit)

with open('withdraw.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
