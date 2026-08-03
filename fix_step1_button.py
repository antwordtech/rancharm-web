with open('airtime.html') as f:
    c = f.read()
before = c

old = '<button id="continueBtn" onclick="goToStep(2)" style="margin-top:16px;">Continue</button>'
new = '<button id="payBtn" onclick="initiatePayment()" style="margin-top:16px;">Pay Now</button>'

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('airtime.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
