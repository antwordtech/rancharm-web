with open('profile.html') as f:
    c = f.read()
before = c

old = '''    document.getElementById('profileEmail').textContent = user.email || '...';
    document.getElementById('profilePhone').textContent = profile.phone || '...';
    document.getElementById('profileTier').textContent = animal.name;
    document.getElementById('profileReferrals').textContent = profile.referralCount || 0;
    document.getElementById('profileTeamRank').textContent = getTeamLevel(profile.teamCount || 0).title;

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

new = '''    document.getElementById('profileAvatarHero').textContent = initial;
    document.getElementById('profileEmail').textContent = user.email || '...';
    document.getElementById('profilePhone').textContent = profile.phone || '...';
    document.getElementById('profileTier').textContent = animal.name + ' \\u00b7 Ranch Level';
    document.getElementById('profileReferrals').textContent = profile.referralCount || 0;
    document.getElementById('profileTeamRank').textContent = getTeamLevel(profile.teamCount || 0).title;

    const subTier = profile.subscriptionTier || 'free';
    if (subTier !== 'free') {
      document.getElementById('profileVerifiedBadge').style.display = 'inline-block';
    }
    document.getElementById('profileSubTier').textContent = subTier.charAt(0).toUpperCase() + subTier.slice(1);

    const kycStatus = profile.kycStatus || 'unverified';
    const kycLabels = { unverified: 'Not Verified', pending: 'Pending Review', approved: 'Verified', rejected: 'Rejected' };
    document.getElementById('profileKycStatus').textContent = kycLabels[kycStatus] || 'Not Verified';

    document.body.classList.add('ready');'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('profile.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
