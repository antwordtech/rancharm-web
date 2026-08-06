with open('tasks.html') as f:
    c = f.read()
before = c

old = "if (task.link) { linkBtn.href = task.link; linkBtn.style.display = 'block'; } else { linkBtn.style.display = 'none'; }"
new = "if (task.link) { var normalizedLink = /^https?:\\/\\//i.test(task.link) ? task.link : 'https://' + task.link; linkBtn.href = normalizedLink; linkBtn.style.display = 'block'; } else { linkBtn.style.display = 'none'; }"

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('tasks.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
