with open('firebase-config.js') as f:
    c = f.read()
before = c

old = '''export async function submitKYC(user, { fullName, idType, idNumber, idFile, selfieFile }) {
  const idRef = ref(storage, `kyc/${user.uid}/id-photo.jpg`);
  await uploadBytes(idRef, idFile);
  const idPhotoUrl = await getDownloadURL(idRef);

  const selfieRef = ref(storage, `kyc/${user.uid}/selfie.jpg`);
  await uploadBytes(selfieRef, selfieFile);
  const selfiePhotoUrl = await getDownloadURL(selfieRef);

  await setDoc(doc(db, "kyc", user.uid), {
    fullName,
    idType,
    idNumber,
    idPhotoUrl,
    selfiePhotoUrl,
    status: "pending",
    submittedAt: Date.now()
  });

  await updateDoc(doc(db, "users", user.uid), { kycStatus: "pending" });
}'''

new = '''export async function submitKYC(user, { mobileMoneyNumber, registeredName, idType, idFile, selfieFile }) {
  const idRef = ref(storage, `kyc/${user.uid}/id-photo.jpg`);
  await uploadBytes(idRef, idFile);
  const idPhotoUrl = await getDownloadURL(idRef);

  const selfieRef = ref(storage, `kyc/${user.uid}/selfie.jpg`);
  await uploadBytes(selfieRef, selfieFile);
  const selfiePhotoUrl = await getDownloadURL(selfieRef);

  await setDoc(doc(db, "kyc", user.uid), {
    mobileMoneyNumber,
    registeredName,
    idType,
    idPhotoUrl,
    selfiePhotoUrl,
    status: "pending",
    submittedAt: Date.now()
  });

  await updateDoc(doc(db, "users", user.uid), { kycStatus: "pending" });
}'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
