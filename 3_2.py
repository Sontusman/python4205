import random
import numpy as np

def print_int():
    try:
        number = int(input("Введите целое число:"))
        return number
    except:
        print("Упс... С числом что-то не так. Пожалуйста, введите еще раз")
        return print_int()


def print_float():
    try:
        number = float(input("Введите действительное число:"))
        return number
    except:
        print("Упс... С числом что-то не так. Пожалуйста, введите еще раз")
        return print_float()

def update_mas(mas: list, m: int, n: int)->list:
    mas = [[i*j for i in range(m)] for j in range(n)]
    return mas

m, n = print_int(), print_int()
mas = [[0]*m]*n
mas = update_mas(mas, m, n)
i, j = random.randrange(n), random.randrange(m)
print(j, i)
print(np.array(mas))
print(mas[i][j])
mas[i][j] = print_float()

print(np.array(mas))

