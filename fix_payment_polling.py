with open('checkout.html') as f:
    c = f.read()
before = c

# 1) Remove the personal phone number placeholder
old_placeholder = 'placeholder="e.g. 0594401046"'
new_placeholder = 'placeholder="Enter your number"'
if old_placeholder not in c:
    print('PLACEHOLDER NOT FOUND - check manually')
c = c.replace(old_placeholder, new_placeholder)

# 2) Add a retry button to the processing step
old_step3 = '''  <div id="step3" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">
    <i class="fa-solid fa-spinner fa-spin" style="font-size:36px;color:var(--brand);margin-bottom:16px;"></i>
    <div style="font-weight:800;font-size:16px;" id="processingText">Confirming your payment...</div>
    <div style="font-size:12px;color:var(--text-dim);margin-top:8px;">This can take a moment. Please don't close this page.</div>
  </div>'''

new_step3 = '''  <div id="step3" class="kyc-step" style="display:none;text-align:center;padding:40px 0;">
    <i class="fa-solid fa-spinner fa-spin" style="font-size:36px;color:var(--brand);margin-bottom:16px;" id="processingIcon"></i>
    <div style="font-weight:800;font-size:16px;" id="processingText">Confirming your payment...</div>
    <div style="font-size:12px;color:var(--text-dim);margin-top:8px;" id="processingHint">This can take a few minutes. Please don't close this page.</div>
    <button id="retryCheckBtn" onclick="retryCheckStatus()" style="display:none;margin-top:20px;width:auto;padding:12px 24px;">Check Again</button>
  </div>'''

if old_step3 not in c:
    print('STEP3 PATTERN NOT FOUND - check manually')
c = c.replace(old_step3, new_step3)

# 3) Extend the polling window and add a proper retry path instead of a dead end
old_poll = '''  function pollStatus() {
    let attempts = 0;
    const maxAttempts = 20;

    const interval = setInterval(async function() {
      attempts++;
      try {
        const res = await fetch(WORKER_URL + '/moolre-status', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ externalref: currentExternalRef })
        });
        const data = await res.json();

        if (data.data && data.data.txstatus === 1) {
          clearInterval(interval);
          await completePurchase();
        } else if (attempts >= maxAttempts) {
          clearInterval(interval);
          document.getElementById('processingText').textContent = 'Payment not confirmed yet. Check back later.';
        }
      } catch (e) {
        // keep trying
      }
    }, 3000);
  }'''

new_poll = '''  function pollStatus() {
    let attempts = 0;
    const maxAttempts = 45;

    document.getElementById('processingIcon').style.display = 'block';
    document.getElementById('processingText').textContent = 'Confirming your payment...';
    document.getElementById('processingHint').style.display = 'block';
    document.getElementById('retryCheckBtn').style.display = 'none';

    const interval = setInterval(async function() {
      attempts++;
      try {
        const res = await fetch(WORKER_URL + '/moolre-status', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ externalref: currentExternalRef })
        });
        const data = await res.json();

        if (data.data && data.data.txstatus === 1) {
          clearInterval(interval);
          await completePurchase();
        } else if (attempts >= maxAttempts) {
          clearInterval(interval);
          document.getElementById('processingIcon').style.display = 'none';
          document.getElementById('processingText').textContent = "Still waiting on confirmation from your network.";
          document.getElementById('processingHint').style.display = 'none';
          document.getElementById('retryCheckBtn').style.display = 'inline-block';
        }
      } catch (e) {
        // keep trying
      }
    }, 4000);
  }

  window.retryCheckStatus = function() {
    pollStatus();
  };'''

if old_poll not in c:
    print('POLL PATTERN NOT FOUND - check manually')
c = c.replace(old_poll, new_poll)

with open('checkout.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
