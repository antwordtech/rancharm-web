with open('booster.html') as f:
    c = f.read()
before = c

old = '''  <div class="step-dots">
    <div class="step-dot active" id="dot1"></div>
    <div class="step-dot" id="dot2"></div>
    <div class="step-dot" id="dot3"></div>
  </div>

  <div id="step1" class="kyc-step">'''

new = '''  <div style="display:flex;background:var(--card);border-radius:14px;padding:4px;margin-bottom:20px;border:1px solid var(--border);">
    <button id="tabNewOrder" onclick="switchTab('new')" style="flex:1;background:var(--brand);color:#fff;border:none;border-radius:10px;padding:10px;font-weight:700;font-size:13px;">New Order</button>
    <button id="tabMyOrders" onclick="switchTab('orders')" style="flex:1;background:transparent;color:var(--text-dim);border:none;border-radius:10px;padding:10px;font-weight:700;font-size:13px;">My Orders</button>
  </div>

  <div id="newOrderView">
    <div class="step-dots">
      <div class="step-dot active" id="dot1"></div>
      <div class="step-dot" id="dot2"></div>
      <div class="step-dot" id="dot3"></div>
    </div>

    <div id="step1" class="kyc-step">'''

if old not in c:
    print('OLD ANCHOR NOT FOUND - check manually')
c = c.replace(old, new)

with open('booster.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
