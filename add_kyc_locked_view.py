with open('withdraw.html') as f:
    c = f.read()
before = c

old_markup = '''  <div id="lockedView" style="display:none;text-align:center;padding:40px 0;">'''
new_markup = '''  <div id="kycLockedView" style="display:none;text-align:center;padding:40px 0;">
    <i class="fa-solid fa-id-card" style="font-size:40px;color:var(--text-dim);margin-bottom:16px;"></i>
    <div style="font-weight:800;font-size:16px;margin-bottom:8px;">Identity Verification Required</div>
    <div style="font-size:13px;color:var(--text-dim);margin-bottom:24px;">Verify your identity before you can withdraw.</div>
    <button onclick="window.location.href='kyc.html'">Verify Identity</button>
  </div>

  <div id="lockedView" style="display:none;text-align:center;padding:40px 0;">'''

if old_markup not in c:
    print('MARKUP NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

old_js = '''    const isPaid = profile.subscriptionTier && profile.subscriptionTier !== 'free' && profile.animalTier && profile.animalTier !== 'cock';
    if (!isPaid) {
      document.getElementById('lockedView').style.display = 'block';
      document.getElementById('formView').style.display = 'none';
    }'''
new_js = '''    const isPaid = profile.subscriptionTier && profile.subscriptionTier !== 'free' && profile.animalTier && profile.animalTier !== 'cock';
    const isKycApproved = profile.kycStatus === 'approved';

    if (!isKycApproved) {
      document.getElementById('kycLockedView').style.display = 'block';
      document.getElementById('formView').style.display = 'none';
    } else if (!isPaid) {
      document.getElementById('lockedView').style.display = 'block';
      document.getElementById('formView').style.display = 'none';
    }'''
if old_js not in c:
    print('JS NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('withdraw.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
