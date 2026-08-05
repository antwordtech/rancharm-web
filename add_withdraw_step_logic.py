with open('withdraw.html') as f:
    c = f.read()
before = c

# Header back button now steps through the flow
old_header = '''<button class="icon-btn" onclick="window.location.href='dashboard.html'"><i class="fa-solid fa-chevron-left"></i></button>'''
new_header = '''<button class="icon-btn" onclick="headerBack()"><i class="fa-solid fa-chevron-left"></i></button>'''
if old_header not in c:
    print('HEADER PATTERN NOT FOUND - check manually')
c = c.replace(old_header, new_header)

# Add step tracking + goToStep + headerBack + goToAmountNext right before onPhoneInput
old_anchor = '  window.onPhoneInput = function() {'
new_anchor = '''  let currentStep = 1;
  window.goToStep = function(n) {
    currentStep = n;
    [1, 2].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };

  window.headerBack = function() {
    if (currentStep === 2) {
      goToStep(1);
    } else {
      window.location.href = 'dashboard.html';
    }
  };

  window.goToAmountNext = function() {
    const amount = document.getElementById('withdrawAmount').value.trim();
    if (!amount || Number(amount) <= 0) { toast('Enter a valid amount', 'error'); return; }
    const pointsNeeded = Math.round(Number(amount) * 100);
    if (pointsNeeded > currentPoints) { toast('Insufficient points balance', 'error'); return; }
    goToStep(2);
  };

  window.onPhoneInput = function() {'''

if old_anchor not in c:
    print('ANCHOR NOT FOUND - check manually')
c = c.replace(old_anchor, new_anchor)

with open('withdraw.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
