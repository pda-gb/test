## задача 3
import math

print('input number:')
num = int(input())   ## Вводим число


def get_zeros(n):
    sum_zer = 0
    itm = 0
    i = 0
    fact = math.factorial(n)   ## вычисляем факториал
    str_zer = str(fact)   ## переводим в строку
    str_rts = str_zer[::-1]   ## разворачиваем
    for i in str_rts:   ## попорядку ищем нули...
        if i == '0':   ## ...по не наткнёмся на "не ноль"
            sum_zer += 1 счтаем количество
        else:
            break
    return sum_zer


print('sum zero', get_zeros(num))
