with open('kyc.html') as f:
    c = f.read()
before = c

old_btn = '''      <button id="submitBtn" onclick="submitForm()">Submit for Review</button>
    </div>
  </div>
</div>'''

new_btn = '''      <button id="submitBtn" onclick="submitForm()">Submit for Review</button>
      <div id="debugErrorBox" style="display:none;margin-top:16px;padding:14px;background:rgba(244,63,94,0.08);border:1px solid #f43f5e;border-radius:14px;font-size:12px;color:#f43f5e;word-break:break-word;"></div>
    </div>
  </div>
</div>'''

if old_btn not in c:
    print('BTN NOT FOUND - check manually')
c = c.replace(old_btn, new_btn)

old_catch = '''    } catch (error) {
      btn.innerHTML = original;
      btn.classList.remove('btn-loading');
      toast(error.message || 'Upload failed. Try again.', 'error');
    }
  };'''

new_catch = '''    } catch (error) {
      btn.innerHTML = original;
      btn.classList.remove('btn-loading');
      const debugMsg = 'Code: ' + (error.code || 'none') + ' | Message: ' + (error.message || 'unknown');
      toast('Upload failed. See details below.', 'error');
      const box = document.getElementById('debugErrorBox');
      box.style.display = 'block';
      box.textContent = debugMsg;
      console.error('KYC submit error:', error);
    }
  };'''

if old_catch not in c:
    print('CATCH NOT FOUND - check manually')
c = c.replace(old_catch, new_catch)

with open('kyc.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
