with open('marketplace.html') as f:
    c = f.read()
before = c

old_ecg = '''<a class="service-row reveal" style="animation-delay:0.2s" href="#" onclick="useService('ECG bill payment'); return false;">'''
new_ecg = '''<a class="service-row reveal" style="animation-delay:0.2s" href="ecg.html">'''
if old_ecg not in c:
    print('ECG PATTERN NOT FOUND - check manually')
c = c.replace(old_ecg, new_ecg)

old_water = '''<a class="service-row reveal" style="animation-delay:0.25s" href="#" onclick="useService('Water bill payment'); return false;">'''
new_water = '''<a class="service-row reveal" style="animation-delay:0.25s" href="water.html">'''
if old_water not in c:
    print('WATER PATTERN NOT FOUND - check manually')
c = c.replace(old_water, new_water)

with open('marketplace.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
