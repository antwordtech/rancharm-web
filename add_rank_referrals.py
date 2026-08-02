with open('referrals.html') as f:
    c = f.read()
before = c

old_markup = '''  <div class="referral-card reveal">
    <div class="team-progress-wrap" style="margin-bottom:0;">'''

new_markup = '''  <div class="referral-card reveal" style="text-align:center;">
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:4px;">Team Rank</div>
    <div style="font-size:20px;font-weight:800;color:var(--brand-dark);" id="teamRankTitle">Member</div>
    <div style="font-size:12px;color:var(--text-dim);margin-top:4px;" id="teamRankNext"></div>
  </div>

  <div class="referral-card reveal">
    <div class="team-progress-wrap" style="margin-bottom:0;">'''

if old_markup not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

old_import = "import { auth, getUserProfile, ANIMALS } from './firebase-config.js?v=3';"
new_import = "import { auth, getUserProfile, ANIMALS, getTeamLevel } from './firebase-config.js?v=3';"
if old_import not in c:
    print('IMPORT PATTERN NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_js = '''    const teamCount = profile.teamCount || 0;
    const capacity = animal.teamCapacity || 0;'''
new_js = '''    const teamCount = profile.teamCount || 0;
    const capacity = animal.teamCapacity || 0;

    const rank = getTeamLevel(teamCount);
    document.getElementById('teamRankTitle').textContent = rank.title;
    document.getElementById('teamRankNext').textContent = rank.next
      ? 'Reach ' + rank.next + ' team members for the next rank'
      : 'Highest rank achieved!';'''
if old_js not in c:
    print('JS PATTERN NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('referrals.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
