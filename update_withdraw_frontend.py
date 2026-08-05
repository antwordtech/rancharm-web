with open('withdraw.html') as f:
    c = f.read()
before = c

old_check = "const isPaid = profile.subscriptionTier && profile.subscriptionTier !== 'free';"
new_check = "const isPaid = profile.subscriptionTier && profile.subscriptionTier !== 'free' && profile.animalTier && profile.animalTier !== 'cock';"
if old_check not in c:
    print('CHECK NOT FOUND - check manually')
c = c.replace(old_check, new_check)

old_next = '''  window.goToAmountNext = function() {
    const amount = document.getElementById('withdrawAmount').value.trim();
    if (!amount || Number(amount) <= 0) { toast('Enter a valid amount', 'error'); return; }
    const pointsNeeded = Math.round(Number(amount) * 100);
    if (pointsNeeded > currentPoints) { toast('Insufficient points balance', 'error'); return; }
    goToStep(2);
  };'''
new_next = '''  window.goToAmountNext = function() {
    const amount = document.getElementById('withdrawAmount').value.trim();
    if (!amount || Number(amount) < 10) { toast('Minimum withdrawal is GHS 10', 'error'); return; }
    const pointsNeeded = Math.round(Number(amount) * 100);
    if (pointsNeeded > currentPoints) { toast('Insufficient points balance', 'error'); return; }
    goToStep(2);
  };'''
if old_next not in c:
    print('NEXT NOT FOUND - check manually')
c = c.replace(old_next, new_next)

old_amount_input = '''  window.onAmountInput = function() {
    const amount = parseFloat(document.getElementById('withdrawAmount').value);
    const label = document.getElementById('pointsNeeded');
    if (!amount || amount <= 0) { label.textContent = ''; return; }
    const needed = Math.round(amount * 100);
    label.textContent = 'Uses ' + needed.toLocaleString() + ' points';
  };'''
new_amount_input = '''  window.onAmountInput = function() {
    const amount = parseFloat(document.getElementById('withdrawAmount').value);
    const label = document.getElementById('pointsNeeded');
    if (!amount || amount <= 0) { label.textContent = ''; return; }
    const needed = Math.round(amount * 100);
    const networkFee = Math.round(amount * 0.03 * 100) / 100;
    const rancharmFee = Math.round(amount * 0.02 * 100) / 100;
    const payout = Math.round((amount - networkFee - rancharmFee) * 100) / 100;
    label.innerHTML = 'Uses ' + needed.toLocaleString() + ' points &middot; Fee GHS ' + (networkFee + rancharmFee).toFixed(2) +
      ' (Network ' + networkFee.toFixed(2) + ' + Rancharm ' + rancharmFee.toFixed(2) + ') &middot; You receive GHS ' + payout.toFixed(2);
  };'''
if old_amount_input not in c:
    print('AMOUNT INPUT NOT FOUND - check manually')
c = c.replace(old_amount_input, new_amount_input)

with open('withdraw.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
