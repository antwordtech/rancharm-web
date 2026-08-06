with open('admin-tasks.html') as f:
    c = f.read()
before = c

old_markup = '''    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:10px;margin-top:16px;">What Should Users Submit?</label>
    <label style="display:flex;align-items:center;gap:10px;margin-bottom:12px;font-size:14px;font-weight:600;">
      <input type="checkbox" id="requireAnswer" style="width:20px;height:20px;">
      Require a written answer
    </label>
    <label style="display:flex;align-items:center;gap:10px;margin-bottom:16px;font-size:14px;font-weight:600;">
      <input type="checkbox" id="requireLink" style="width:20px;height:20px;">
      Require a proof link
    </label>

    <button onclick="goToStep(5)" style="margin-top:8px;">Next</button>
  </div>'''

new_markup = '''    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:10px;margin-top:16px;">What Should Users Submit?</label>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--border);">
      <span style="font-size:14px;font-weight:600;">Require a written answer</span>
      <span class="theme-switch" id="answerSwitch" onclick="toggleReq('answer')"><span class="theme-switch-knob"></span></span>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-bottom:1px solid var(--border);">
      <span style="font-size:14px;font-weight:600;">Require a proof link</span>
      <span class="theme-switch" id="linkSwitch" onclick="toggleReq('link')"><span class="theme-switch-knob"></span></span>
    </div>
    <div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;">
      <span style="font-size:14px;font-weight:600;">Require a photo upload</span>
      <span class="theme-switch" id="photoSwitch" onclick="toggleReq('photo')"><span class="theme-switch-knob"></span></span>
    </div>

    <button onclick="goToStep(5)" style="margin-top:16px;">Next</button>
  </div>'''

if old_markup not in c:
    print('MARKUP NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

old_vars = '''  let selectedTier = 'free';'''
new_vars = '''  let selectedTier = 'free';
  let reqAnswerVal = false;
  let reqLinkVal = false;
  let reqPhotoVal = false;

  window.toggleReq = function(type) {
    if (type === 'answer') { reqAnswerVal = !reqAnswerVal; document.getElementById('answerSwitch').classList.toggle('on', reqAnswerVal); }
    if (type === 'link') { reqLinkVal = !reqLinkVal; document.getElementById('linkSwitch').classList.toggle('on', reqLinkVal); }
    if (type === 'photo') { reqPhotoVal = !reqPhotoVal; document.getElementById('photoSwitch').classList.toggle('on', reqPhotoVal); }
  };'''
if old_vars not in c:
    print('VARS NOT FOUND - check manually')
c = c.replace(old_vars, new_vars)

old_review = '''    const reqAnswer = document.getElementById('requireAnswer').checked;
    const reqLink = document.getElementById('requireLink').checked;

    document.getElementById('reviewTitle').textContent = title || 'Untitled Task';
    document.getElementById('reviewDesc').textContent = desc || 'No description';

    const tierLabel = { free: 'Everyone', premium: 'Premium+', vip: 'VIP+', elite: 'Elite Only' }[selectedTier];
    const reqParts = [];
    if (reqAnswer) reqParts.push('Answer required');
    if (reqLink) reqParts.push('Link required');
    const reqText = reqParts.length ? reqParts.join(' & ') : 'No submission needed';'''

new_review = '''    document.getElementById('reviewTitle').textContent = title || 'Untitled Task';
    document.getElementById('reviewDesc').textContent = desc || 'No description';

    const tierLabel = { free: 'Everyone', premium: 'Premium+', vip: 'VIP+', elite: 'Elite Only' }[selectedTier];
    const reqParts = [];
    if (reqAnswerVal) reqParts.push('Answer');
    if (reqLinkVal) reqParts.push('Link');
    if (reqPhotoVal) reqParts.push('Photo');
    const reqText = reqParts.length ? reqParts.join(' + ') + ' required' : 'No submission needed';'''

if old_review not in c:
    print('REVIEW NOT FOUND - check manually')
c = c.replace(old_review, new_review)

old_publish = '''    const requireAnswer = document.getElementById('requireAnswer').checked;
    const requireLink = document.getElementById('requireLink').checked;

    if (!title || !pointsReward) { toast('Title and points reward are required', 'error'); return; }'''
new_publish = '''    if (!title || !pointsReward) { toast('Title and points reward are required', 'error'); return; }'''
if old_publish not in c:
    print('PUBLISH VARS NOT FOUND - check manually')
c = c.replace(old_publish, new_publish)

old_setdoc = '''        requireAnswer: requireAnswer,
        requireLink: requireLink,
        active: true,'''
new_setdoc = '''        requireAnswer: reqAnswerVal,
        requireLink: reqLinkVal,
        requirePhoto: reqPhotoVal,
        active: true,'''
if old_setdoc not in c:
    print('SETDOC NOT FOUND - check manually')
c = c.replace(old_setdoc, new_setdoc)

with open('admin-tasks.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
