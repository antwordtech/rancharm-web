with open('profile.html') as f:
    c = f.read()
before = c

old_html = '''    <div class="profile-row">
      <div class="profile-row-label">People Referred</div>
      <div class="profile-row-value" id="profileReferrals">—</div>
    </div>
  </div>

  <a class="nav-tile reveal" href="referrals.html" style="display:block;margin-bottom:24px;">'''

new_html = '''    <div class="profile-row">
      <div class="profile-row-label">People Referred</div>
      <div class="profile-row-value" id="profileReferrals">—</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Verification</div>
      <div class="profile-row-value" id="profileKycStatus">—</div>
    </div>
  </div>

  <a class="nav-tile reveal" id="kycTile" href="kyc.html" style="display:none;margin-bottom:24px;">
    <i class="fa-solid fa-id-card" style="color:var(--brand);margin-right:8px;"></i><span id="kycTileText">Verify Identity</span>
  </a>

  <a class="nav-tile reveal" href="referrals.html" style="display:block;margin-bottom:24px;">'''

if old_html not in c:
    print('HTML PATTERN NOT FOUND - check manually')
c = c.replace(old_html, new_html)

old_js = '''    document.getElementById('profileReferrals').textContent = profile.referralCount || 0;

    document.body.classList.add('ready');'''

new_js = '''    document.getElementById('profileReferrals').textContent = profile.referralCount || 0;

    const kycStatus = profile.kycStatus || 'unverified';
    const kycLabels = { unverified: 'Not Verified', pending: 'Pending Review', approved: 'Verified', rejected: 'Rejected' };
    document.getElementById('profileKycStatus').textContent = kycLabels[kycStatus] || 'Not Verified';

    const kycTile = document.getElementById('kycTile');
    const kycTileText = document.getElementById('kycTileText');
    if (kycStatus === 'approved') {
      kycTile.style.display = 'none';
    } else {
      kycTile.style.display = 'block';
      kycTileText.textContent = kycStatus === 'pending' ? 'View Verification Status' : (kycStatus === 'rejected' ? 'Resubmit Verification' : 'Verify Identity');
    }

    document.body.classList.add('ready');'''

if old_js not in c:
    print('JS PATTERN NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('profile.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
