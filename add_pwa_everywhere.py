import glob

pwa_tags = '''<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="icon-512.png">
<script>
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/sw.js').catch(function(){});
  });
}
</script>
'''

files = glob.glob('*.html')
count_ok = 0
count_skip = 0

for fname in files:
    with open(fname) as f:
        c = f.read()
    before = c

    if 'rel="manifest"' in c:
        count_skip += 1
        continue

    if '</head>' in c:
        c = c.replace('</head>', pwa_tags + '</head>', 1)
    else:
        print(fname, 'NO HEAD CLOSE TAG - skipped')
        continue

    with open(fname, 'w') as f:
        f.write(c)
    count_ok += 1

print('Updated:', count_ok, 'files')
print('Already had manifest (skipped):', count_skip, 'files')
