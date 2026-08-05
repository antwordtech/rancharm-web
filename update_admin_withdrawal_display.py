with open('admin-withdrawals.html') as f:
    c = f.read()
before = c

old = '''        <div class="profile-row"><div class="profile-row-label">Amount</div><div class="profile-row-value">GHS ${w.amountGHS}</div></div>
        <div class="profile-row"><div class="profile-row-label">Network</div><div class="profile-row-value">${w.network}</div></div>'''

new = '''        <div class="profile-row"><div class="profile-row-label">Requested</div><div class="profile-row-value">GHS ${w.amountGHS}</div></div>
        <div class="profile-row"><div class="profile-row-label">Fee (Network+Rancharm)</div><div class="profile-row-value">GHS ${w.totalFee || 0}</div></div>
        <div class="profile-row"><div class="profile-row-label">Pay Out</div><div class="profile-row-value" style="color:var(--brand-dark);font-weight:800;">GHS ${w.payoutAmount || w.amountGHS}</div></div>
        <div class="profile-row"><div class="profile-row-label">Network</div><div class="profile-row-value">${w.network}</div></div>'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('admin-withdrawals.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
