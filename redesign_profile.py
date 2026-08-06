with open('profile.html') as f:
    c = f.read()
before = c

# 1) Fix the stale Withdraw drawer link
old_withdraw = '''<a class="drawer-link" href="#" onclick="toast('Withdrawals coming soon'); return false;"><i class="fa-solid fa-arrow-up-from-bracket"></i>Withdraw</a>'''
new_withdraw = '''<a class="drawer-link" href="withdraw.html"><i class="fa-solid fa-arrow-up-from-bracket"></i>Withdraw</a>'''
if old_withdraw not in c:
    print('WITHDRAW LINK NOT FOUND - check manually')
c = c.replace(old_withdraw, new_withdraw)

# 2) Replace the whole .page body: card list -> hero + clean service-row list
old_page = '''<div class="page">
  <div class="section-title" style="margin-top:0">Profile</div>

  <div class="profile-card reveal">
    <div class="profile-row">
      <div class="profile-row-label">Email</div>
      <div class="profile-row-value" id="profileEmail">...</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Phone</div>
      <div class="profile-row-value" id="profilePhone">...</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Ranch Level</div>
      <div class="profile-row-value" id="profileTier">...</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">People Referred</div>
      <div class="profile-row-value" id="profileReferrals">...</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Team Rank</div>
      <div class="profile-row-value" id="profileTeamRank">-</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Verification</div>
      <div class="profile-row-value" id="profileKycStatus">...</div>
    </div>
  </div>

  <a class="nav-tile reveal" id="kycTile" href="kyc.html" style="display:none;margin-bottom:24px;">
    <i class="fa-solid fa-id-card" style="color:var(--brand);margin-right:8px;"></i><span id="kycTileText">Verify Identity</span>
  </a>

  <a class="nav-tile reveal" href="referrals.html" style="display:block;margin-bottom:24px;">
    <i class="fa-solid fa-user-group" style="color:var(--brand);margin-right:8px;"></i>View Referral Link
  </a>

  <button class="btn-danger reveal" onclick="logout()">Log Out</button>
</div>'''

new_page = '''<div class="page">
  <div style="text-align:center;padding:20px 0 28px;">
    <div style="width:72px;height:72px;border-radius:50%;background:linear-gradient(135deg, var(--brand), var(--brand-dark));color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px;margin:0 auto 14px;box-shadow:0 8px 20px rgba(15,157,140,0.3);" id="profileAvatarHero">?</div>
    <div style="font-weight:800;font-size:17px;display:flex;align-items:center;justify-content:center;gap:6px;">
      <span id="profileEmail">-</span>
      <i class="fa-solid fa-circle-check verified-badge-icon" id="profileVerifiedBadge" style="display:none;"></i>
    </div>
    <div class="drawer-tier" style="margin-top:6px;font-size:13px;" id="profileTier">-</div>
  </div>

  <div class="service-list">
    <div class="service-row" style="cursor:default;">
      <div class="service-icon-circle"><i class="fa-solid fa-phone"></i></div>
      <div>
        <div class="service-row-title">Phone Number</div>
        <div class="service-row-desc" id="profilePhone">-</div>
      </div>
    </div>
    <div class="service-row" style="cursor:default;">
      <div class="service-icon-circle"><i class="fa-solid fa-user-group"></i></div>
      <div>
        <div class="service-row-title">People Referred</div>
        <div class="service-row-desc" id="profileReferrals">-</div>
      </div>
    </div>
    <div class="service-row" style="cursor:default;">
      <div class="service-icon-circle"><i class="fa-solid fa-trophy"></i></div>
      <div>
        <div class="service-row-title">Team Rank</div>
        <div class="service-row-desc" id="profileTeamRank">-</div>
      </div>
    </div>
    <a class="service-row" id="kycRow" href="kyc.html">
      <div class="service-icon-circle"><i class="fa-solid fa-id-card"></i></div>
      <div>
        <div class="service-row-title">Identity Verification</div>
        <div class="service-row-desc" id="profileKycStatus">-</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row" href="referrals.html">
      <div class="service-icon-circle"><i class="fa-solid fa-link"></i></div>
      <div>
        <div class="service-row-title">Referral Link</div>
        <div class="service-row-desc">Share and earn</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row" href="subscription.html">
      <div class="service-icon-circle"><i class="fa-solid fa-crown"></i></div>
      <div>
        <div class="service-row-title">Subscription</div>
        <div class="service-row-desc" id="profileSubTier">Free</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
    <a class="service-row" href="withdraw.html">
      <div class="service-icon-circle"><i class="fa-solid fa-arrow-up-from-bracket"></i></div>
      <div>
        <div class="service-row-title">Withdraw</div>
        <div class="service-row-desc">Cash out your points</div>
      </div>
      <i class="fa-solid fa-chevron-right service-row-chevron"></i>
    </a>
  </div>
</div>'''

if old_page not in c:
    print('PAGE BODY NOT FOUND - check manually')
c = c.replace(old_page, new_page)

with open('profile.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
