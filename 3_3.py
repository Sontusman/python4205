import math
import io
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


class matrix():
    def __init__(self, mas: list = None, m: int = 0, n: int = 0):
        self.mas = mas
        self.m = m
        self.n = n

    def set(self, m:int, n:int):
        self.mas = [[(i+1)*(j+1) for i in range(m)] for j in range(n)]

    def out(self, place = None):
        if place== None:
            for row in self.mas:
                print(" ".join(map(str, row)), "\n")
        elif type(place) is str:
            file = open(place, "w")
            for row in self.mas:
                file.write(" ".join(map(str, row)))
                file.write("\n")
            file.close()
        elif isinstance(place, io.TextIOBase):
            for row in self.mas:
                place.write(" ".join(map(str, row)))
                place.write("\n")
            place.close()

    def convert(self, func):
        self.mas = [[func(elem) for elem in row] for row in self.mas]

m, n = print_int(), print_int()
matrix = matrix()
matrix.set(m, n)
matrix.out()
matrix.out("3_3_string.txt")
file_obj = open("3_3_object.txt", "w")
matrix.out(file_obj)
matrix.convert(math.asinh)
matrix.out()