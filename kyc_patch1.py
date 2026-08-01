with open('kyc.html') as f:
    c = f.read()
before = c

# 1) Header back button now steps back through the flow
c = c.replace(
    '<button class="icon-btn" onclick="window.location.href=\'profile.html\'"><i class="fa-solid fa-chevron-left"></i></button>\n    <div class="topbar-logo">Ranch<span>arm</span></div>',
    '<button class="icon-btn" onclick="headerBack()"><i class="fa-solid fa-chevron-left"></i></button>\n    <div class="topbar-logo">Ranch<span>arm</span></div>'
)

# 2) Remove the bottom text "Back" links on steps 2 and 3
c = c.replace('      <div class="step-back" onclick="goToStep(1)" style="margin-bottom:16px;">Back</div>\n', '')
c = c.replace('      <div class="step-back" onclick="goToStep(2)" style="margin-bottom:16px;">Back</div>\n', '')

# 3) Remove the "Next" button on step 2 (auto-advances instead)
c = c.replace('      <button id="step2NextBtn" onclick="goToStep(3)" disabled style="opacity:0.5;">Next</button>\n', '')

# 4) Replace Verify button + input with auto-verify-on-type version
old_step1_input = '''        <input type="tel" id="momoNumber" placeholder="e.g. 233246912184">
        <button id="verifyBtn" onclick="verifyNumber()">Verify Number</button>
        <div id="verifiedNameBox" class="verified-name-box" style="display:none;margin-top:16px;margin-bottom:0;">'''

new_step1_input = '''        <input type="tel" id="momoNumber" placeholder="e.g. 233246912184" oninput="onMomoInput()">
        <div id="verifyStatus" style="font-size:12px;color:var(--text-dim);margin:-8px 0 14px 4px;min-height:16px;"></div>
        <div id="verifiedNameBox" class="verified-name-box" style="display:none;margin-bottom:0;">'''

if old_step1_input not in c:
    print('STEP1 INPUT PATTERN NOT FOUND - check manually')
c = c.replace(old_step1_input, new_step1_input)

with open('kyc.html', 'w') as f:
    f.write(c)
print('markup patch OK' if c != before else 'NO CHANGE')
