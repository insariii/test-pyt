# 1
t = int(input('введите температуру: '))
print(9/5 * t + 32)

# 2
age = int(input('Сколько вам лет? '))
if age < 18:
    print('Молодой')
elif 18 <= age < 60:
    print('Взрослый')
else:
    print('Пожилой')

# 3
n = int(input())
if n%3==0 and n%5==0:
    print('это число делится на 3 и на 5')

# 4
n = int(input())
if n%7==0 and n%5!=0:
    print('это число делится на 7, но не делится на 5')

# 5
n = int(input())
for i in range(1, n+1):
    if i%3==0:
        continue
    print(i)

# 6
for i in range(1, 101):
    if i > 50:
        break
    if i%2==0:
        print(i)

# 7
for i in range(1, 11):
    if i == 6:
        continue
    print(i)

# 8
n = int(input())
for i in range(1, 21):
    if i == n:
        break
    print(i)

# 9
s = 0
n = int(input())
while n > 0:
    s += n
    n -= 1
print(s)

# 10
k = 0
n = int(input())
while int(n) > 0:
    n /= 10
    k += 1
print(k)

# 11
n = 100
s = 0
while n > 0:
    n -= 1
    if n%2==0:
        s += n
print(s)

# 12
n = 10
while n > 0:
    print(n)
    n -= 1

# 13
maxn = -100000000
n = int(input())
while n != 0:
    maxn = max(maxn, n)
    n = int(input())
print(maxn)

# 14
k = 0
n = int(input())
while n != 0:
    if n > 10:
        k += 1
    n = int(input())
print(k)

# 15
while True:
    n = int(input())
    if n == 0:
        break
    print(n)

# 16
lst = []
for i in range(1, 11):
    lst.append(i)

for a in lst:
    # если И на 3 И на 5 одновременно, то AND
    if a%3==0 or a%5==0:
        print(a)

# 17
for i in range(1, 101):
    if i%3 == 0 or i%5==0:
        continue
    print(i)