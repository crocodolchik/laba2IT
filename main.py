print('Hello, World!')

# №4
name = 'Кирилл'
age = 45
height = 1.86
is_student = True

print(name)
print(age)
print(height)
print(is_student)

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

age = 46
height = 1.67
print(age)
print(height)

# №5
name = input('Имя')
surname = input('Фамилия')
age = input('Возраст')
print(type(age), 'До преобразований')

age = int(age)
print(type(age))

height = float(input('Рост'))
print(type(height))

print('Имя', name)
print('Фамилия', surname)
print('Возраст', age)
print('Рост', height)

# №6
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b, '=a / b это обычное деление')
print(a // b, '=a // b это деление без остатка')
print(a % b)
print(a ** b)

print(2 + 3 * 4)
print((2 + 3) * 4)

# №7
a = float(input('Первое число '))
b = float(input('Второе число '))
print(a + b)
print(a - b)
print(a * b)

if b != 0:
    print(a / b)
else:
    print('Нет деления на ноль')

# №8
for x in range(1, 11):
    print(x)

for i in range(10, 0, -1):
    print(i)

for t in range(0, 21, 2):
    print(t)

for k in range(0, 20, 4):
    print(k)

# №9
n = int(input('Введи положительное число n'))
summ = 0
for x in range(1, n + 1):
    summ += x
print(summ)

# №10
countt = 10
while countt > 0:
    print(countt)
    countt -= 1
print("Цикл завершён")

# №11
import math
radius = 17
len_ocr = math.pi * 2 * radius
S_kr = math.pi * radius ** 2

print('Длинна окружности', len_ocr)
print('S круга', S_kr)

a = 36
print(math.sqrt(a), '=', 'Квадратный корень')

# №12
a = int(input('Целое число'))
if a > 0:
    print("Число положительное")
elif a < 0:
    print("Число отрицательное")
elif a == 0:
    print('Число равно нулю')

if a % 2 == 0:
    print("Число четное")
else:
    print("Число не четное")

# №13
age = int(input('Возраст'))
has_access = input('Есть доступ(True/False)') == 'True'
print(age)
print(has_access)

if age >= 18 and has_access:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

# №14

n = int(input("Введите количество измерений "))

summa = 0.0

for i in range(n):
    value = float(input(f"Введите измерение {i + 1}: "))
    summa += value

average = summa / n

print("Сумма", summa)
print("Среднее ариф", average)
