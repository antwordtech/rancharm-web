with open('index.html') as f:
    c = f.read()
before = c

old_body = '<body class="ready" style="padding-bottom:40px;">\n\n<div class="page" style="padding-top:32px;">'

new_body = '''<body style="padding-bottom:40px;">
<div class="page-loader page-loader-app" id="pageLoader" style="background:var(--bg);">
  <dotlottie-wc src="https://lottie.host/455b3c68-8f9a-4345-b369-2fd3162bc953/Qc4CNAKTcR.json" style="width:90px;height:90px;" autoplay loop></dotlottie-wc>
</div>

<div class="page" style="padding-top:32px;">'''

if old_body not in c:
    print('BODY PATTERN NOT FOUND - check manually')
c = c.replace(old_body, new_body)

old_closing = '''</script>
</body>
</html>'''

new_closing = '''
  import { auth } from './firebase-config.js?v=3';
  import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";

  onAuthStateChanged(auth, (user) => {
    if (user) {
      window.location.href = 'login.html';
    } else {
      document.body.classList.add('ready');
    }
  });
</script>
</body>
</html>'''

if old_closing not in c:
    print('CLOSING PATTERN NOT FOUND - check manually')
c = c.replace(old_closing, new_closing)

with open('index.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
