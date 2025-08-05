num=int(input())
cat=[[] for _ in range(num)]

for j in range (num):
  string=list(input())
  letter,capital,space,number=0,0,0,0
  
  for c in string:
    a=ord(c)
    if a == 32:
      space += 1
    elif 65 <= a <= 90:
      capital += 1
    elif 97 <= a <= 122:
      letter += 1
    elif 48 <= a <= 57:
      number += 1

  cat[j] = [letter, capital, number, space, '\n']

for result in cat:
  print(*result)