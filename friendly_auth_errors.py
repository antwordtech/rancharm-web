with open('login.html') as f:
    c = f.read()
before = c

old_import = '  import { createUserWithEmailAndPassword, signInWithEmailAndPassword, signInWithPopup, GoogleAuthProvider, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";'

new_import = old_import + '''

  function getFriendlyAuthError(error) {
    const code = error && error.code ? error.code : '';
    const map = {
      'auth/invalid-credential': 'Incorrect email or password. Please try again.',
      'auth/wrong-password': 'Incorrect email or password. Please try again.',
      'auth/user-not-found': 'No account found with this email.',
      'auth/email-already-in-use': 'An account with this email already exists. Try logging in instead.',
      'auth/weak-password': 'Please choose a stronger password (at least 6 characters).',
      'auth/invalid-email': 'Please enter a valid email address.',
      'auth/too-many-requests': 'Too many attempts. Please wait a moment and try again.',
      'auth/network-request-failed': 'Network error. Please check your internet connection.',
      'auth/popup-closed-by-user': 'Sign-in was cancelled.',
    };
    return map[code] || 'Something went wrong. Please try again.';
  }'''

if old_import not in c:
    print('IMPORT PATTERN NOT FOUND - check manually')
c = c.replace(old_import, new_import)

old_toast = "toast(error.message, 'error');"
new_toast = "toast(getFriendlyAuthError(error), 'error');"
count = c.count(old_toast)
c = c.replace(old_toast, new_toast)

with open('login.html', 'w') as f:
    f.write(c)
print('replaced', count, 'toast calls')
print('OK' if c != before else 'NO CHANGE')
