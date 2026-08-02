with open('profile.html') as f:
    c = f.read()
before = c

old_markup = '''    <div class="profile-row">
      <div class="profile-row-label">People Referred</div>
      <div class="profile-row-value" id="profileReferrals">-</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Verification</div>'''

new_markup = '''    <div class="profile-row">
      <div class="profile-row-label">People Referred</div>
      <div class="profile-row-value" id="profileReferrals">-</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Team Rank</div>
      <div class="profile-row-value" id="profileTeamRank">-</div>
    </div>
    <div class="profile-row">
      <div class="profile-row-label">Verification</div>'''

if old_markup not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

old_import = "import { auth, getUserProfile, ANIMALS } from './firebase-config.js?v=3';"
new_import = "import { auth, getUserProfile, ANIMALS, getTeamLevel } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT PATTERN NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_js = "    document.getElementById('profileReferrals').textContent = profile.referralCount || 0;"
new_js = '''    document.getElementById('profileReferrals').textContent = profile.referralCount || 0;
    document.getElementById('profileTeamRank').textContent = getTeamLevel(profile.teamCount || 0).title;'''
if old_js not in c:
    print('JS PATTERN NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('profile.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
