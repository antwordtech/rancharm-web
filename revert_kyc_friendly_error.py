with open('kyc.html') as f:
    c = f.read()
before = c

old = '''    } catch (error) {
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

new = '''    } catch (error) {
      btn.innerHTML = original;
      btn.classList.remove('btn-loading');
      console.error('KYC submit error:', error);
      toast('Submission failed. Please try again.', 'error');
    }
  };'''

if old not in c:
    print('CATCH NOT FOUND - check manually')
c = c.replace(old, new)

with open('kyc.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
