with open('styles.css') as f:
    c = f.read()
before = c

block = """.payment-sheet-backdrop { position: fixed; inset: 0; background: rgba(2,6,23,0.45); backdrop-filter: blur(4px); display: flex; align-items: flex-end; justify-content: center; opacity: 0; pointer-events: none; transition: opacity 0.2s ease; z-index: 120; }
.payment-sheet-backdrop.open { opacity: 1; pointer-events: auto; }
.payment-sheet { background: var(--bg); border-radius: 24px 24px 0 0; padding: 28px 24px 40px; width: 100%; max-width: 480px; transform: translateY(100%); transition: transform 0.3s cubic-bezier(0.4,0,0.2,1); }
.payment-sheet-backdrop.open .payment-sheet { transform: translateY(0); }
.payment-sheet-handle { width: 40px; height: 4px; background: var(--border); border-radius: 999px; margin: 0 auto 20px; }
.payment-step { display: none; }
.payment-step.active { display: block; }
"""

if block not in c:
    print('BLOCK NOT FOUND - check manually (may already be removed)')
c = c.replace(block, '')

with open('styles.css', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
