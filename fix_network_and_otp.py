with open('checkout.html') as f:
    c = f.read()
before = c

# 1) Remove the network-picker markup entirely
old_markup = """    <label style="font-size:12px;font-weight:700;color:var(--text-dim);display:block;margin-bottom:6px;margin-top:16px;">Network</label>
    <div class="id-type-grid">
      <div class="id-type-option" data-value="13" onclick="selectNetwork(this)">
        <div class="id-type-option-name">MTN</div>
      </div>
      <div class="id-type-option" data-value="6" onclick="selectNetwork(this)">
        <div class="id-type-option-name">Telecel</div>
      </div>
      <div class="id-type-option" data-value="7" onclick="selectNetwork(this)">
        <div class="id-type-option-name">AT</div>
      </div>
    </div>

    <button id="payBtn" onclick="initiatePayment()" style="margin-top:20px;" disabled>Pay Now</button>"""

new_markup = """    <button id="payBtn" onclick="initiatePayment()" style="margin-top:20px;">Pay Now</button>"""

if old_markup not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

# 2) Remove selectedNetwork variable, add detectNetwork function
old_vars = """  let currentUser = null;
  let selectedNetwork = null;
  let itemPrice = 0;"""

new_vars = """  let currentUser = null;
  let itemPrice = 0;

  function detectNetwork(phone) {
    let n = phone.replace(/\\s+/g, '');
    if (n.startsWith('+233')) n = '0' + n.slice(4);
    else if (n.startsWith('233')) n = '0' + n.slice(3);
    const prefix = n.slice(0, 3);
    const mtn = ['024', '025', '053', '054', '055', '059'];
    const telecel = ['020', '050'];
    const at = ['026', '027', '056', '057'];
    if (mtn.includes(prefix)) return '13';
    if (telecel.includes(prefix)) return '6';
    if (at.includes(prefix)) return '7';
    return null;
  }"""

if old_vars not in c:
    print('VARS PATTERN NOT FOUND - check manually')
c = c.replace(old_vars, new_vars)

# 3) Remove selectNetwork function (no longer needed)
old_select_fn = """  window.selectNetwork = function(el) {
    document.querySelectorAll('.id-type-option').forEach(function(o) { o.classList.remove('selected'); });
    el.classList.add('selected');
    selectedNetwork = el.dataset.value;
    document.getElementById('payBtn').disabled = false;
  };

"""
if old_select_fn not in c:
    print('SELECT FUNCTION NOT FOUND - check manually')
c = c.replace(old_select_fn, '')

with open('checkout.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
