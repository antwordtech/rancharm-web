with open('data.html') as f:
    c = f.read()
before = c

# 1) Header back button navigates through steps instead of jumping straight to marketplace
old_header_btn = '''<button class="icon-btn" onclick="window.location.href='marketplace.html'"><i class="fa-solid fa-chevron-left"></i></button>'''
new_header_btn = '''<button class="icon-btn" onclick="headerBack()"><i class="fa-solid fa-chevron-left"></i></button>'''
if old_header_btn not in c:
    print('HEADER BTN NOT FOUND - check manually')
c = c.replace(old_header_btn, new_header_btn)

# 2) Remove the inline "Back" text link from step2
old_back_link = '''    <div class="step-back" onclick="goToStep(1)" style="margin-top:16px;">Back</div>
'''
if old_back_link not in c:
    print('BACK LINK NOT FOUND - check manually')
c = c.replace(old_back_link, '')

# 3) Add currentStep tracking + headerBack function
old_gotostep = '''  window.goToStep = function(n) {
    [1, 2, 3].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };'''
new_gotostep = '''  let currentStep = 1;
  window.goToStep = function(n) {
    currentStep = n;
    [1, 2, 3].forEach(function(i) {
      document.getElementById('step' + i).style.display = i === n ? 'block' : 'none';
      document.getElementById('dot' + i).classList.toggle('active', i === n);
    });
  };

  window.headerBack = function() {
    if (currentStep === 2) {
      goToStep(1);
    } else {
      window.location.href = 'marketplace.html';
    }
  };'''
if old_gotostep not in c:
    print('GOTOSTEP PATTERN NOT FOUND - check manually')
c = c.replace(old_gotostep, new_gotostep)

# 4) Pass the button into buyBundleClick/buyBundle so we can animate it while purchasing
old_wrapper = '''  window.buyBundleClick = function(btn) {
    const id = btn.dataset.bundleId;
    const price = parseFloat(btn.dataset.bundlePrice);
    buyBundle(id, price);
  };

  async function buyBundle(bundleId, price) {'''
new_wrapper = '''  window.buyBundleClick = function(btn) {
    const id = btn.dataset.bundleId;
    const price = parseFloat(btn.dataset.bundlePrice);
    buyBundle(id, price, btn);
  };

  async function buyBundle(bundleId, price, btn) {
    const originalHtml = btn ? btn.innerHTML : '';
    if (btn) {
      btn.disabled = true;
      btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i>';
    }'''
if old_wrapper not in c:
    print('WRAPPER PATTERN NOT FOUND - check manually')
c = c.replace(old_wrapper, new_wrapper)

# 5) Restore the button if purchase fails (insufficient balance / error), since success navigates away from this view anyway
old_insufficient = '''      } else if (data.error === 'Insufficient points balance') {
        toast('Insufficient points balance', 'error');
      } else {
        toast(data.error || 'Something went wrong. Try again.', 'error');
      }
    } catch (e) {
      toast('Something went wrong. Try again.', 'error');
    }
  };'''
new_insufficient = '''      } else if (data.error === 'Insufficient points balance') {
        toast('Insufficient points balance', 'error');
        if (btn) { btn.disabled = false; btn.innerHTML = originalHtml; }
      } else {
        toast(data.error || 'Something went wrong. Try again.', 'error');
        if (btn) { btn.disabled = false; btn.innerHTML = originalHtml; }
      }
    } catch (e) {
      toast('Something went wrong. Try again.', 'error');
      if (btn) { btn.disabled = false; btn.innerHTML = originalHtml; }
    }
  }'''
if old_insufficient not in c:
    print('INSUFFICIENT PATTERN NOT FOUND - check manually')
c = c.replace(old_insufficient, new_insufficient)

with open('data.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
