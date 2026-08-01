# 1) Update ANIMALS array with real lottie URLs
with open('firebase-config.js') as f:
    c = f.read()

old_animals = '''export const ANIMALS = [
  { key: "cock",   name: "Cock",   price: 0,    tier: "Starter",  dailyPoints: 5,   image: null },
  { key: "duck",   name: "Duck",   price: 50,   tier: "Beginner", dailyPoints: 15,  image: null },
  { key: "pig",    name: "Pig",    price: 150,  tier: "Active",   dailyPoints: 35,  image: null },
  { key: "fox",    name: "Fox",    price: 500,  tier: "Advanced", dailyPoints: 100, image: null },
  { key: "monkey", name: "Monkey", price: 1000, tier: "Premium",  dailyPoints: 180, image: null },
  { key: "parrot", name: "Parrot", price: 2000, tier: "VIP",      dailyPoints: 320, image: null },
  { key: "horse",  name: "Horse",  price: 5000, tier: "Elite",    dailyPoints: 700, image: null }
];'''

new_animals = '''export const ANIMALS = [
  { key: "cock",   name: "Cock",   price: 0,    tier: "Starter",  dailyPoints: 5,   image: null, lottie: "https://lottie.host/596eb98d-85c0-4779-b3e1-5e8db56a494f/zj1yYMqMHa.json" },
  { key: "duck",   name: "Duck",   price: 50,   tier: "Beginner", dailyPoints: 15,  image: null, lottie: "https://lottie.host/e1bba21b-0fee-41af-ae55-26291082f468/ZOsTxfZBvR.json" },
  { key: "pig",    name: "Pig",    price: 150,  tier: "Active",   dailyPoints: 35,  image: null, lottie: "https://lottie.host/dc296098-4998-49a6-93f0-d592282e7de4/EthkkTygvZ.json" },
  { key: "fox",    name: "Fox",    price: 500,  tier: "Advanced", dailyPoints: 100, image: null, lottie: "https://lottie.host/41f6f306-fabd-42a7-adb4-0d7038a3c37e/wlbHGxS0ZC.json" },
  { key: "monkey", name: "Monkey", price: 1000, tier: "Premium",  dailyPoints: 180, image: null, lottie: "https://lottie.host/9f0f16f1-2f64-42ca-bf01-912416f6462d/hQeKjJlX8B.json" },
  { key: "parrot", name: "Parrot", price: 2000, tier: "VIP",      dailyPoints: 320, image: null, lottie: "https://lottie.host/7849c0e2-0026-4e21-a353-db246b1a1bcf/HoxniEkE7X.json" },
  { key: "horse",  name: "Horse",  price: 5000, tier: "Elite",    dailyPoints: 700, image: null, lottie: "https://lottie.host/e388d08e-854a-4c29-a88a-7b7a7cbc87b6/PeYW0lHF66.json" }
];'''

before = c
c = c.replace(old_animals, new_animals)
with open('firebase-config.js', 'w') as f:
    f.write(c)
print('firebase-config.js', "OK" if c != before else "NO CHANGE - check manually")

# 2) ranch-store.html: add lottie script + render illustrations in the grid
with open('ranch-store.html') as f:
    c = f.read()
before = c
c = c.replace(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">',
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">\n<script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.4/dist/dotlottie-wc.js" type="module"></script>'
)
c = c.replace(
    '        <div class="animal-avatar">${animal.image ? `<img src="${animal.image}">` : initial}</div>',
    '        <div class="animal-avatar" style="${animal.lottie ? \'background:none;\' : \'\'}">${animal.lottie ? `<dotlottie-wc src="${animal.lottie}" autoplay loop style="width:60px;height:60px;"></dotlottie-wc>` : (animal.image ? `<img src="${animal.image}">` : initial)}</div>'
)
with open('ranch-store.html', 'w') as f:
    f.write(c)
print('ranch-store.html', "OK" if c != before else "NO CHANGE - check manually")

# 3) my-ranch.html: add lottie script + render big illustration
with open('my-ranch.html') as f:
    c = f.read()
before = c
c = c.replace(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">',
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">\n<script src="https://unpkg.com/@lottiefiles/dotlottie-wc@0.9.4/dist/dotlottie-wc.js" type="module"></script>'
)
old_avatar_js = '''    document.getElementById('animalAvatar').innerHTML = currentAnimal.image
      ? `<img src="${currentAnimal.image}">` : currentAnimal.name.charAt(0);'''
new_avatar_js = '''    document.getElementById('animalAvatar').innerHTML = currentAnimal.lottie
      ? `<dotlottie-wc src="${currentAnimal.lottie}" autoplay loop style="width:80px;height:80px;"></dotlottie-wc>`
      : (currentAnimal.image ? `<img src="${currentAnimal.image}">` : currentAnimal.name.charAt(0));
    document.getElementById('animalAvatar').style.background = currentAnimal.lottie ? 'none' : '';'''
c = c.replace(old_avatar_js, new_avatar_js)
with open('my-ranch.html', 'w') as f:
    f.write(c)
print('my-ranch.html', "OK" if c != before else "NO CHANGE - check manually")

print("DONE")
