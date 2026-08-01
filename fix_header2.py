whatsapp_url = "https://whatsapp.com/channel/0029VbDYtgnDuMRX0yFQVo1h"
whatsapp_icon = f'<a class="icon-btn" href="{whatsapp_url}" target="_blank" rel="noopener" style="text-decoration:none;"><i class="fa-brands fa-whatsapp"></i></a>'

# Dashboard: currently WhatsApp left, hamburger right -> swap back
old_dashboard = whatsapp_icon + '''
    <div class="topbar-logo">Ranch<span>arm</span></div>
    <button class="icon-btn" onclick="openDrawer()"><i class="fa-solid fa-bars"></i></button>'''
new_dashboard = '''<button class="icon-btn" onclick="openDrawer()"><i class="fa-solid fa-bars"></i></button>
    <div class="topbar-logo">Ranch<span>arm</span></div>
    ''' + whatsapp_icon

with open('dashboard.html') as f:
    c = f.read()
before = c
if old_dashboard not in c:
    print('dashboard.html: PATTERN NOT FOUND - check manually')
c = c.replace(old_dashboard, new_dashboard)
with open('dashboard.html', 'w') as f:
    f.write(c)
print('dashboard.html', 'OK' if c != before else 'NO CHANGE')

# Other pages: currently WhatsApp left, back-arrow right -> swap back
old_back = whatsapp_icon + '''
    <div class="topbar-logo">Ranch<span>arm</span></div>
    <button class="icon-btn" onclick="window.location.href='dashboard.html'"><i class="fa-solid fa-chevron-left"></i></button>'''
new_back = '''<button class="icon-btn" onclick="window.location.href='dashboard.html'"><i class="fa-solid fa-chevron-left"></i></button>
    <div class="topbar-logo">Ranch<span>arm</span></div>
    ''' + whatsapp_icon

other_files = ["ranch-store.html", "my-ranch.html", "tasks.html", "referrals.html", "profile.html", "leaderboard.html", "marketplace.html"]
for fname in other_files:
    with open(fname) as f:
        c = f.read()
    before = c
    if old_back not in c:
        print(fname, 'PATTERN NOT FOUND - check manually')
    c = c.replace(old_back, new_back)
    with open(fname, 'w') as f:
        f.write(c)
    print(fname, 'OK' if c != before else 'NO CHANGE')

print("DONE")
