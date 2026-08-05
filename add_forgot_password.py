with open('login.html') as f:
    c = f.read()
before = c

# 1) Markup: add link + new forgotBlock
old_markup = '''      <input type="password" id="loginPassword" placeholder="Password">
      <button id="loginBtn" onclick="doLogin()">Log In</button>
      <div class="divider">or</div>
      <button class="btn-outline" id="googleBtn" onclick="googleLogin()"><i class="fa-brands fa-google"></i> Continue with Google</button>
      <div class="toggle-text">Don't have an account? <span onclick="switchMode('signup')" class="link">Sign up</span></div>
    </div>'''

new_markup = '''      <input type="password" id="loginPassword" placeholder="Password">
      <div style="text-align:right;margin:-10px 0 14px;">
        <span onclick="switchMode('forgot')" class="link" style="font-size:12px;">Forgot Password?</span>
      </div>
      <button id="loginBtn" onclick="doLogin()">Log In</button>
      <div class="divider">or</div>
      <button class="btn-outline" id="googleBtn" onclick="googleLogin()"><i class="fa-brands fa-google"></i> Continue with Google</button>
      <div class="toggle-text">Don't have an account? <span onclick="switchMode('signup')" class="link">Sign up</span></div>
    </div>

    <!-- FORGOT PASSWORD MODE -->
    <div id="forgotBlock" style="display:none">
      <div class="tagline" style="margin-bottom:16px;">Enter your email and we'll send you a reset link.</div>
      <input type="email" id="forgotEmail" placeholder="Email address">
      <button id="forgotBtn" onclick="doForgotPassword()">Send Reset Link</button>
      <div class="toggle-text">Remembered your password? <span onclick="switchMode('login')" class="link">Log in</span></div>
    </div>'''

if old_markup not in c:
    print('MARKUP NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

# 2) switchMode: handle forgot mode
old_switch = '''  window.switchMode = (mode) => {
    document.getElementById('loginBlock').style.display = mode === 'login' ? 'block' : 'none';
    document.getElementById('signupStep1').style.display = mode === 'signup' ? 'block' : 'none';
    document.getElementById('signupStep2').style.display = 'none';
  };'''

new_switch = '''  window.switchMode = (mode) => {
    document.getElementById('loginBlock').style.display = mode === 'login' ? 'block' : 'none';
    document.getElementById('signupStep1').style.display = mode === 'signup' ? 'block' : 'none';
    document.getElementById('signupStep2').style.display = 'none';
    document.getElementById('forgotBlock').style.display = mode === 'forgot' ? 'block' : 'none';
  };

  window.doForgotPassword = async () => {
    const email = document.getElementById('forgotEmail').value.trim();
    if (!email) { toast('Enter your email address', 'error'); return; }

    const btn = document.getElementById('forgotBtn');
    btn.disabled = true;
    btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';

    try {
      await sendPasswordResetEmail(auth, email);
      toast('Reset link sent! Check your email.', 'success');
      switchMode('login');
    } catch (error) {
      toast(getFriendlyAuthError(error), 'error');
    } finally {
      btn.disabled = false;
      btn.innerHTML = 'Send Reset Link';
    }
  };'''

if old_switch not in c:
    print('SWITCH NOT FOUND - check manually')
c = c.replace(old_switch, new_switch)

# 3) Import sendPasswordResetEmail
old_import = 'import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";'
new_import = 'import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider, onAuthStateChanged, sendPasswordResetEmail } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";'
if old_import not in c:
    print('IMPORT NOT FOUND - check manually')
c = c.replace(old_import, new_import)

with open('login.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
