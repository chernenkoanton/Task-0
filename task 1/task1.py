print ('*****************')
s = list(input('Введіть свій рядок:'))
mas = []

for i in range(len(s)): 
    if '1' in s:
        s.remove('1')
        mas.append('1')
    elif '2' in s:
        s.remove('2')
        mas.append('2')
    elif '3' in s:
        s.remove('3')
        mas.append('3')
    elif '4' in s:
        s.remove('4')
        mas.append('4')
    elif '5' in s:
        s.remove('5')
        mas.append('5')
    elif '6' in s:
        s.remove('6')
        mas.append('6')
    elif '7' in s:
        s.remove('7')
        mas.append('7')
    elif '8' in s:
        s.remove('8')
        mas.append('8')
    elif '9' in s:
       s.remove('9')
       mas.append('9')
    elif '0' in s:
        s.remove('0')
        mas.append('9')


mas = [int(i) for i in mas]
s = ''.join(s)
print ('Масив тільки з числами',mas)
print ('Рядок без чисел:',s)

def cap_both(phrase):
    return ' '.join(map(lambda s: s[:-1]+s[-1].upper(), phrase.title().split()))

print ('Кожне слово починається з великої і кінчається великою:',cap_both(s))
maxnumber = max(mas)

mas.remove(max(mas))

print("Максимальне значення в масиві:", maxnumber)
print ('Масив без максимального числа',mas)


mas2 = []
for i in range(len(mas)):
        step = mas[i] ** i
        mas2.insert(i, step)
print("Масив чисел піднесених до степеню по їх індексу:", mas2)
print ('*****************')
