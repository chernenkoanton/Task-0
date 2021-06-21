import random
a = [random.randint(-100, 100) for x in range(30)]
biggest = max(a)
r.index(biggest_number)
print(a)
print(biggest)
print(a.index(biggest_number)+1)
for i in range(29):
  if a[i]<0 and a[i+1]<0:
    print(a[i],a[i+1])
