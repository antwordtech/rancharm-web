with open('my-ranch.html') as f:
    c = f.read()
before = c

old = '''    <button id="feedBtn" onclick="feedAnimal()">Feed Now</button>
  </div>
</div>'''

new = '''    <button id="feedBtn" onclick="feedAnimal()">Feed Now</button>
  </div>

  <div class="feed-card reveal" style="text-align:center;">
    <div style="font-weight:800;font-size:16px;margin-bottom:4px;">Watch Ads for Bonus Points</div>
    <div style="font-size:12px;color:var(--text-dim);margin-bottom:16px;">Watch 5 ads to earn <span id="adsBonusAmount">0</span> bonus points today</div>
    <div class="team-progress-bar" style="margin-bottom:12px;">
      <div class="team-progress-fill" id="adsProgressFill" style="width:0%;"></div>
    </div>
    <div style="font-size:13px;font-weight:700;margin-bottom:16px;" id="adsProgressText">0 / 5 ads watched</div>
    <button id="watchAdBtn" onclick="watchAd()">Watch Ad</button>
  </div>
</div>'''

if old not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('my-ranch.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
