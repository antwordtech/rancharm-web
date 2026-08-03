with open('firebase-config.js') as f:
    c = f.read()
before = c

old = '''export const SUBSCRIPTIONS = [
  { key: "free",    name: "Free",    price: 0,   benefits: ["Ads shown", "Basic tasks"] },
  { key: "premium", name: "Premium", price: 20,  benefits: ["Fewer ads", "More tasks", "Better features"] },
  { key: "vip",     name: "VIP",     price: 50,  benefits: ["VIP access", "Special campaigns"] },
  { key: "elite",   name: "Elite",   price: 200, benefits: ["Advanced tools", "Business features"] }
];'''

new = '''export const SUBSCRIPTIONS = [
  { key: "free",    name: "Free",    price: 0,
    benefits: ["Ads shown", "No tasks", "Earn 1% commission on referred users' purchases", "Withdrawals not available", "Standard support"] },
  { key: "premium", name: "Premium", price: 20,
    benefits: ["No ads", "Access to low-tier tasks", "Verified badge", "Withdrawals enabled", "24/7 support", "Earn 5% commission on referred users' purchases", "Earn 5% of withdrawal fee on referred users' withdrawals"] },
  { key: "vip",     name: "VIP",     price: 50,
    benefits: ["No ads", "Access to medium-tier tasks", "Verified badge", "Withdrawals enabled", "24/7 support", "Earn 15% commission on referred users' purchases", "Earn 15% of withdrawal fee on referred users' withdrawals"] },
  { key: "elite",   name: "Elite",   price: 200,
    benefits: ["No ads", "Access to high-tier tasks", "Verified badge", "Withdrawals enabled", "24/7 support", "Earn 30% commission on referred users' purchases", "Earn 30% of withdrawal fee on referred users' withdrawals"] }
];'''

if old not in c:
    print('PATTERN NOT FOUND - check manually')
c = c.replace(old, new)

with open('firebase-config.js', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
