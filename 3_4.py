def print_int(text: str = "Введите число:"):
    try:
        number = int(input(text))
        return number
    except:
        print("Упс... С числом что-то не так. Пожалуйста, введите еще раз")
        return print_int()

def print_float(text: str = "Введите число:"):
    try:
        number = float(input(text))
        return number
    except:
        print("Упс... С числом что-то не так. Пожалуйста, введите еще раз")
        return print_float()
import sys
import matplotlib.pyplot as plt
from math import sin, cos, atan

class matrix2():
    def __init__(self, x0: float, dx: float, x: list=None, y: list=None, N: int = 10):
        self.x = [[0]*N]
        self.y = [[0]*N]
        self.N = N
        self.x0 = x0
        self.dx = dx
    def setx(self):
        self.x = [self.x0+i*self.dx for i in range(self.N)]
    def sety(self, func):
        self.y = [func(x_) for x_ in self.x]
    def out(self, file_obj = sys.stdout):
        for i in range(N):
            file_obj.write(f"{self.x[i]} {self.y[i]}\n")
    def plot(self, axes_object, xlabel = "x", ylabel = "y", title="График", label=None):
        axes_object.plot(self.x, self.y, label=label)
        axes_object.grid()
        axes_object.set_title(title)
        axes_object.set_xlabel(xlabel)
        axes_object.set_ylabel(ylabel)
        axes_object.legend()
        return axes_object

fig1, ax1 = plt.subplots()
N = print_int()
x0, dx = print_float(), print_float()
matrix_1, matrix_2, matrix_3 = matrix2(N=N, x0=x0, dx=dx), matrix2(N=N, x0=x0, dx=dx), matrix2(N=N, x0=x0, dx=dx)
matrix_1.setx(); matrix_2.setx(); matrix_3.setx()
matrix_1.sety(sin); matrix_2.sety(cos); matrix_3.sety(atan)
matrix_1.out()
file_obj = open("3_4_object.txt", "w")
matrix_1.out(file_obj)
fig1, ax1 = plt.subplots()
matrix_1.plot(ax1, title="sin, cos, exp", label="sin")
matrix_2.plot(ax1, title="sin, cos, exp", label = "cos")
matrix_3.plot(ax1, title="sin, cos, exp", label="exp")


fig2, ax2 = plt.subplots(1, 3, figsize=(11, 4))
matrix_1.plot(ax2[0], title="sin")
matrix_2.plot(ax2[1], title="cos")
matrix_3.plot(ax2[2], title="exp")
plt.show()