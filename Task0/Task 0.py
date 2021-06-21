import random
p = [random.randint(-100, 100) for x in range(30)]
biggest = max(p)
r.index(biggest_number)
print(p)
print(biggest)
print(p.index(biggest_number)+1)
for i in range(29):
  if p[i]<0 and p[i+1]<0:
    print(p[i],p[i+1])
