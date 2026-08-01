with open('styles.css') as f:
    c = f.read()

old = """html, body { visibility: hidden; }
body {
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  color: var(--text);
  padding-bottom: 24px;
  opacity: 0;
  transition: opacity 0.35s ease;
}
body.ready { visibility: visible; opacity: 1; }"""

new = """body {
  font-family: 'Inter', -apple-system, sans-serif;
  background: var(--bg);
  min-height: 100vh;
  color: var(--text);
  padding-bottom: 24px;
}"""

if old in c:
    c = c.replace(old, new)
    print("body rule fixed")
else:
    print("WARNING: old body rule not found — check styles.css manually")

with open('styles.css', 'w') as f:
    f.write(c)
