#1
import random
name = input("Введіть своє им'я: ")
age = int(input("Скільки вам років: "))
print("Привіт, ", name + "! Тобі ", age)
# 2
age = int(input("Скільки вам років: "))
if age < 18:
    print("Вхід заборонено!")

# 3
a = 0
rnum = random.randint(1, 10)
answer = 0
while a < 3:
    a += 1
    answer = int(input("Вгадайте число від 1 до 10: "))
    if answer == rnum:
        print("ви вгадали")
        break
    if answer > rnum:
        print("меньше")
    if answer < rnum:
        print("більше")
    print(a)

# 4
first = int(input("з "))
second = int(input("по "))
for i in range(first, second + 1):
    print(i)

#5

num = 1
num2 = int(input("Введіть число: "))

if num2 % 2 == 0:
  print("Число парне")
  b = int(num2)
  while b != 0:
   print(b)
   b -= 2
else:
  print("Число непарне")

#6
n = int(input("Введіть число: "))
a = 1
for u in range(1, n+1):
  a *= u
print(a)
