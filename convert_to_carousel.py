with open('dashboard.html') as f:
    c = f.read()
before = c

old = '''  <div class="section-title" style="margin-top:24px;">How Rancharm Works</div>

  <div class="task-card reveal" style="margin-bottom:12px;">
    <div style="display:flex;align-items:center;gap:14px;">
      <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">1</div>
      <div>
        <div class="task-title">Get your free Cock</div>
        <div class="task-desc">Sign up and receive your first Ranch animal, free with no payment needed.</div>
      </div>
    </div>
  </div>

  <div class="task-card reveal" style="margin-bottom:12px;animation-delay:0.05s;">
    <div style="display:flex;align-items:center;gap:14px;">
      <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">2</div>
      <div>
        <div class="task-title">Feed your animal daily</div>
        <div class="task-desc">Every animal earns Points each day you feed it, the bigger the animal, the bigger the reward.</div>
      </div>
    </div>
  </div>

  <div class="task-card reveal" style="margin-bottom:12px;animation-delay:0.1s;">
    <div style="display:flex;align-items:center;gap:14px;">
      <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">3</div>
      <div>
        <div class="task-title">Upgrade your Ranch Level</div>
        <div class="task-desc">Buy a higher-tier animal in the Ranch Store to unlock bigger daily earnings.</div>
      </div>
    </div>
  </div>

  <div class="task-card reveal" style="margin-bottom:12px;animation-delay:0.15s;">
    <div style="display:flex;align-items:center;gap:14px;">
      <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">4</div>
      <div>
        <div class="task-title">Build your team</div>
        <div class="task-desc">Invite friends with your referral link and earn Points for every person who joins.</div>
      </div>
    </div>
  </div>
</div>'''

new = '''  <div class="section-title" style="margin-top:24px;">How Rancharm Works</div>

  <div class="how-carousel">
    <div class="how-track" id="howTrack">
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">1</div>
            <div>
              <div class="task-title">Get your free Cock</div>
              <div class="task-desc">Sign up and receive your first Ranch animal, free with no payment needed.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">2</div>
            <div>
              <div class="task-title">Feed your animal daily</div>
              <div class="task-desc">Every animal earns Points each day you feed it, the bigger the animal, the bigger the reward.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">3</div>
            <div>
              <div class="task-title">Upgrade your Ranch Level</div>
              <div class="task-desc">Buy a higher-tier animal in the Ranch Store to unlock bigger daily earnings.</div>
            </div>
          </div>
        </div>
      </div>
      <div class="how-slide">
        <div class="task-card" style="margin-bottom:0;">
          <div style="display:flex;align-items:center;gap:14px;">
            <div class="drawer-avatar" style="width:38px;height:38px;font-size:15px;flex-shrink:0;">4</div>
            <div>
              <div class="task-title">Build your team</div>
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

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('dashboard.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
