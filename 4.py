# 4) Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
x = int(input('введите целое положительное число'))
max = 0
while x != 0:
    dig = x % 10
    if dig > max:
        max = dig
    x = x // 10
print(max)
