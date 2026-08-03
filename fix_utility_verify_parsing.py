with open('utility.html') as f:
    c = f.read()
before = c

old = '''      if (data.account_name) {
        document.getElementById('accountName').textContent = data.account_name;
        document.getElementById('payAmount').value = data.amount_due || '';
        onAmountInput();
        goToStep(2);
      } else {
        toast(data.message || 'Could not verify this account', 'error');
      }'''

new = '''      const info = data.data || data;
      if (info.account_name) {
        document.getElementById('accountName').textContent = info.account_name;
        document.getElementById('payAmount').value = info.amount_due || '';
        onAmountInput();
        goToStep(2);
      } else {
        toast(data.message || 'Could not verify this account', 'error');
      }'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('utility.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
