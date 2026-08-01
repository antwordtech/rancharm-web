with open('kyc.html') as f:
    c = f.read()
before = c

# Track current step + header back navigates between steps
old_gotostep = '''  window.goToStep = (n) => {
    [1, 2, 3].forEach(i => {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };'''

new_gotostep = '''  let currentStep = 1;
  window.goToStep = (n) => {
    currentStep = n;
    [1, 2, 3].forEach(i => {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };
  window.headerBack = () => {
    if (currentStep > 1) {
      goToStep(currentStep - 1);
    } else {
      window.location.href = 'profile.html';
    }
  };'''

if old_gotostep not in c:
    print('GOTOSTEP PATTERN NOT FOUND - check manually')
c = c.replace(old_gotostep, new_gotostep)

# Replace verifyNumber (button-driven) with auto-verify-on-input version
old_verify = '''  window.verifyNumber = async () => {
    const number = document.getElementById('momoNumber').value.trim();
    if (!number) { toast('Enter your Mobile Money number', 'error'); return; }
    const btn = document.getElementById('verifyBtn');
    const original = btn.innerHTML;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Verifying...';
    btn.classList.add('btn-loading');
    try {
      const res = await fetch(WORKER_URL + '/verify-sim?phone=' + encodeURIComponent(number));
      const data = await res.json();
      if (!res.ok || !data.ok) { throw new Error(data.error || 'Could not verify this number'); }
      verifiedName = data.registered_name;
      document.getElementById('verifiedNameValue').textContent = verifiedName;
      document.getElementById('verifiedNameBox').style.display = 'block';
      document.getElementById('step1NextBtn').disabled = false;
      document.getElementById('step1NextBtn').style.opacity = '1';
      toast('Number verified!', 'success');
    } catch (error) {
      toast(error.message, 'error');
    } finally {
      btn.innerHTML = original;
      btn.classList.remove('btn-loading');
    }
  };'''

new_verify = '''  let verifyTimer = null;
  window.onMomoInput = () => {
    clearTimeout(verifyTimer);
    document.getElementById('verifiedNameBox').style.display = 'none';
    document.getElementById('step1NextBtn').disabled = true;
    document.getElementById('step1NextBtn').style.opacity = '0.5';
    document.getElementById('verifyStatus').textContent = '';
    const val = document.getElementById('momoNumber').value.trim();
    if (val.length < 9) return;
    verifyTimer = setTimeout(verifyNumber, 700);
  };

  async function verifyNumber() {
    const number = document.getElementById('momoNumber').value.trim();
    if (!number) return;
    const statusEl = document.getElementById('verifyStatus');
    statusEl.innerHTML = '<i class="fa-solid fa-spinner fa-spin" style="color:var(--brand);"></i> Verifying...';
    try {
      const res = await fetch(WORKER_URL + '/verify-sim?phone=' + encodeURIComponent(number));
      const data = await res.json();
      if (!res.ok || !data.ok) { throw new Error(data.error || 'Could not verify this number'); }
      verifiedName = data.registered_name;
      document.getElementById('verifiedNameValue').textContent = verifiedName;
      document.getElementById('verifiedNameBox').style.display = 'block';
      document.getElementById('step1NextBtn').disabled = false;
      document.getElementById('step1NextBtn').style.opacity = '1';
      statusEl.innerHTML = '<i class="fa-solid fa-circle-check" style="color:var(--brand);"></i> Verified';
    } catch (error) {
      statusEl.innerHTML = '<span style="color:#f43f5e;">' + error.message + '</span>';
    }
  }'''

if old_verify not in c:
    print('VERIFY PATTERN NOT FOUND - check manually')
c = c.replace(old_verify, new_verify)

# Auto-advance to step 3 once an ID type is picked
old_select = '''  window.selectIdType = (el) => {
    document.querySelectorAll('.id-type-option').forEach(o => o.classList.remove('selected'));
    el.classList.add('selected');
    selectedIdType = el.dataset.value;
    document.getElementById('step2NextBtn').disabled = false;
    document.getElementById('step2NextBtn').style.opacity = '1';
  };'''

new_select = '''  window.selectIdType = (el) => {
    document.querySelectorAll('.id-type-option').forEach(o => o.classList.remove('selected'));
    el.classList.add('selected');
    selectedIdType = el.dataset.value;
    setTimeout(() => goToStep(3), 350);
  };'''

if old_select not in c:
    print('SELECT PATTERN NOT FOUND - check manually')
c = c.replace(old_select, new_select)

with open('kyc.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
