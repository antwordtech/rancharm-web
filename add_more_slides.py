with open('dashboard.html') as f:
    c = f.read()
before = c

old_slides_end = '''              <div class="task-title">Build your team</div>
              <div class="task-desc">Invite friends with your referral link and earn Points for every person who joins.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="step-dots" id="howDots">
    <div class="step-dot active" id="howDot1"></div>
    <div class="step-dot" id="howDot2"></div>
    <div class="step-dot" id="howDot3"></div>
    <div class="step-dot" id="howDot4"></div>
  </div>
</div>'''

new_slides_end = '''              <div class="task-title">Build your team</div>
              <div class="task-desc">Invite friends with your referral link and earn Points for every person who joins.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;"><i class="fa-solid fa-store"></i></div>
            <div>
              <div class="task-title">Ranch Store</div>
              <div class="task-desc">Upgrade to a bigger animal anytime, from Duck all the way up to Horse, for even bigger daily earnings.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;"><i class="fa-solid fa-list-check"></i></div>
            <div>
              <div class="task-title">Complete Tasks</div>
              <div class="task-desc">Finish simple tasks around the app for extra bonus Points on top of feeding.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;"><i class="fa-solid fa-fire"></i></div>
            <div>
              <div class="task-title">Marketplace</div>
              <div class="task-desc">Spend your Points on real things: Airtime, Data, TV bills, and Social Booster orders.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;"><i class="fa-solid fa-crown"></i></div>
            <div>
              <div class="task-title">Go Premium</div>
              <div class="task-desc">Subscribe to remove ads and unlock real cash withdrawals to your Mobile Money.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="step-dots" id="howDots">
    <div class="step-dot active" id="howDot1"></div>
    <div class="step-dot" id="howDot2"></div>
    <div class="step-dot" id="howDot3"></div>
    <div class="step-dot" id="howDot4"></div>
    <div class="step-dot" id="howDot5"></div>
    <div class="step-dot" id="howDot6"></div>
    <div class="step-dot" id="howDot7"></div>
    <div class="step-dot" id="howDot8"></div>
  </div>
</div>'''

if old_slides_end not in c:
    print('SLIDES PATTERN NOT FOUND - check manually')
c = c.replace(old_slides_end, new_slides_end)

# Update JS to cycle through 8 slides instead of 4
old_js = '''  let howIndex = 0;
  setInterval(function() {
    howIndex = (howIndex + 1) % 4;
    document.getElementById('howTrack').style.transform = 'translateX(-' + (howIndex * 100) + '%)';
    [1, 2, 3, 4].forEach(function(i) {
      document.getElementById('howDot' + i).classList.toggle('active', i === howIndex + 1);
    });
  }, 5000);'''

new_js = '''  let howIndex = 0;
  setInterval(function() {
    howIndex = (howIndex + 1) % 8;
    document.getElementById('howTrack').style.transform = 'translateX(-' + (howIndex * 100) + '%)';
    [1, 2, 3, 4, 5, 6, 7, 8].forEach(function(i) {
      document.getElementById('howDot' + i).classList.toggle('active', i === howIndex + 1);
    });
  }, 5000);'''

if old_js not in c:
    print('JS PATTERN NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
