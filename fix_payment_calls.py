with open('checkout.html') as f:
    c = f.read()
before = c

# Add a shared variable to remember the detected network across both calls
old_var = """  let currentExternalRef = null;
  let currentStep = 1;"""
new_var = """  let currentExternalRef = null;
  let currentStep = 1;
  let detectedNetwork = null;"""
if old_var not in c:
    print('VAR PATTERN NOT FOUND - check manually')
c = c.replace(old_var, new_var)

# Fix initiatePayment: detect network instead of requiring a UI pick
old_initiate = """  window.initiatePayment = async function() {
    const phone = document.getElementById('payPhone').value.trim();
    if (!phone || !selectedNetwork) { toast('Enter your number and select a network', 'error'); return; }

    const btn = document.getElementById('payBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';

    currentExternalRef = tierType + '-' + tierKey + '-' + currentUser.uid.slice(0, 6) + '-' + Date.now();

    try {
      const res = await fetch(WORKER_URL + '/moolre-collect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phone: phone, amount: String(itemPrice), channel: selectedNetwork, externalref: currentExternalRef })
      });"""

new_initiate = """  window.initiatePayment = async function() {
    const phone = document.getElementById('payPhone').value.trim();
    if (!phone) { toast('Enter your Mobile Money number', 'error'); return; }

    detectedNetwork = detectNetwork(phone);
    if (!detectedNetwork) { toast('Could not detect your network from this number', 'error'); return; }

    const btn = document.getElementById('payBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';

    currentExternalRef = tierType + '-' + tierKey + '-' + currentUser.uid.slice(0, 6) + '-' + Date.now();

    try {
      const res = await fetch(WORKER_URL + '/moolre-collect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phone: phone, amount: String(itemPrice), channel: detectedNetwork, externalref: currentExternalRef })
      });"""

if old_initiate not in c:
    print('INITIATE PATTERN NOT FOUND - check manually')
c = c.replace(old_initiate, new_initiate)

# Fix submitOtp: use detectedNetwork, and auto-retry once when Moolre says "verification successful" but hasn't sent the payment prompt yet
old_otp = """  window.submitOtp = async function() {
    const phone = document.getElementById('payPhone').value.trim();
    const otp = document.getElementById('otpInput').value.trim();
    if (!otp) { toast('Enter the OTP code', 'error'); return; }

    const btn = document.getElementById('otpBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Confirming...';

    try {
      const res = await fetch(WORKER_URL + '/moolre-collect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phone: phone, amount: String(itemPrice), channel: selectedNetwork, externalref: currentExternalRef, otpcode: otp })
      });
      const data = await res.json();

      if (data.code === 'TR099') {
        goToStep(3);
        pollStatus();
      } else {
        toast(data.message || 'Incorrect OTP. Try again.', 'error');
      }
    } catch (e) {
      toast('Something went wrong. Try again.', 'error');
    } finally {
      btn.disabled = false;
      btn.innerHTML = 'Confirm';
    }
  };"""

new_otp = """  window.submitOtp = async function(isRetry) {
    const phone = document.getElementById('payPhone').value.trim();
    const otp = document.getElementById('otpInput').value.trim();
    if (!otp) { toast('Enter the OTP code', 'error'); return; }

    const btn = document.getElementById('otpBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Confirming...';

    try {
      const res = await fetch(WORKER_URL + '/moolre-collect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ phone: phone, amount: String(itemPrice), channel: detectedNetwork, externalref: currentExternalRef, otpcode: otp })
      });
      const data = await res.json();

      if (data.code === 'TR099') {
        goToStep(3);
        pollStatus();
      } else if (data.message && data.message.toLowerCase().indexOf('verification successful') !== -1 && !isRetry) {
        await submitOtp(true);
        return;
      } else {
        toast(data.message || 'Incorrect OTP. Try again.', 'error');
      }
    } catch (e) {
      toast('Something went wrong. Try again.', 'error');
    } finally {
      btn.disabled = false;
      btn.innerHTML = 'Confirm';
    }
  };"""

if old_otp not in c:
    print('OTP PATTERN NOT FOUND - check manually')
c = c.replace(old_otp, new_otp)

with open('checkout.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
