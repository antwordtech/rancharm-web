with open('profile.html') as f:
    lines = f.readlines()

before = ''.join(lines)

# 1) Add hero avatar/tier update right after the email line
for i, line in enumerate(lines):
    if "document.getElementById('profileTier').textContent = animal.name;" in line:
        lines[i] = "    document.getElementById('profileAvatarHero').textContent = initial;\n    document.getElementById('profileTier').textContent = animal.name + ' \\u00b7 Ranch Level';\n"
        break

# 2) Add verified badge + subTier display right after profileKycStatus line
for i, line in enumerate(lines):
    if "document.getElementById('profileKycStatus').textContent" in line:
        insert = [
            "    const subTier = profile.subscriptionTier || 'free';\n",
            "    if (subTier !== 'free') { document.getElementById('profileVerifiedBadge').style.display = 'inline-block'; }\n",
            "    document.getElementById('profileSubTier').textContent = subTier.charAt(0).toUpperCase() + subTier.slice(1);\n"
        ]
        lines[i+1:i+1] = insert
        break

# 3) Remove the now-dead kycTile/kycTileText block
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if "const kycTile = document.getElementById('kycTile');" in line:
        start_idx = i
    if start_idx is not None and line.strip() == '}' and i > start_idx:
        end_idx = i
        break

if start_idx is not None and end_idx is not None:
    del lines[start_idx:end_idx+1]
else:
    print('KYC TILE BLOCK NOT FOUND - check manually')

with open('profile.html', 'w') as f:
    f.writelines(lines)

after = ''.join(lines)
print('OK' if after != before else 'NO CHANGE')
