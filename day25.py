# DAY 25
cardPkey, doorPkey = 2084668, 3704642

def performLoop(value, subject_number):
  return (value * subject_number) % 20201227

n = 1
lsize = 1
while True:
  n = performLoop(n, 7)
  if n == cardPkey:
    break
  lsize+=1

ekey = 1
for _ in range(lsize):
  ekey = performLoop(ekey, doorPkey)

print(ekey)
