import tkinter as tk
from task_3_4 import matrix2
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import warnings
warnings.filterwarnings("ignore")

matrix = None

def set_params(QA1, QA2, QA3)-> None:
    global matrix
    if QA1.get_value()=="":
        N, x0, dx = 100, 0, 1
    else:
        N, x0, dx= int(QA3.get_value()), float(QA1.get_value()), float(QA2.get_value())
    matrix = matrix2(N=N, x0=x0, dx=dx)
    print("Параметры установлены")

def check_params(txt) -> None:
    global matrix
    text = f"N: {matrix.N}, x0: {matrix.x0}, dx: {matrix.dx}"#\n x: {matrix.x}, y: {matrix.y}"
    txt.delete('1.0', tk.END)
    txt.insert('1.0', text)
    txt.pack()

def calculate_values(QA4) -> None:
    if QA4.get_value() == "":
        func = "sin"
    else:
        func = QA4.get_value()
    global matrix
    func = getattr(math, func)
    matrix.setx()
    matrix.sety(func)
    print("Значения x и y рассчитаны")

def export_values() -> None:
    global matrix
    file_obj = open("3_5_file.txt", "w")
    matrix.out(file_obj)
    print("Значения X и Y записаны в файл")

def import_values():
    global matrix
    with open('3_5_import.txt', 'r') as file:
        matrix.x = [float(line.split(' ')[0]) for line in file]
    with open('3_5_import.txt', 'r') as file:
        matrix.y = [float(line.split(' ')[1][:-2]) for line in file]
    print(matrix.x, matrix.y)

def draw_graph(canvas, id, img_tk):
    fig1, ax1 = plt.subplots()
    matrix.plot(ax1)
    fig1.savefig("graph_figure.png")

    img = Image.open("graph_figure.png")
    img = img.resize((550, 400))
    QA.img_tk = ImageTk.PhotoImage(img)
    canvas.itemconfig(id, image=QA.img_tk)
    canvas.image = img_tk

def save_graph():
    fig1, ax1 = plt.subplots()
    matrix.plot(ax1)
    fig1.savefig("graph_figure.png")

def clear_graph(canvas, id, img_tk):
    img = Image.open("picture.png")
    img = img.resize((550, 400))
    QA.img_tk = ImageTk.PhotoImage(img)
    canvas.itemconfig(id, image=QA.img_tk)
    canvas.image = img_tk

def close(window):
    window.destroy()

def create_window():
    window = tk.Tk()
    window.title("Давайте строить графики!")
    
    frame1 = tk.Frame(window)
    QA1 = QA(frame1, "Введи x0")
    QA2 = QA(frame1, "Введи dx")
    frame1.pack()
    
    frame2 = tk.Frame(window)
    QA3 = QA(frame2, "Введи N")
    QA4 = QA(frame2, "Введи функцию")
    frame2.pack()

    button1 = tk.Button(window, text="Задать параметры", command = lambda: set_params(QA1, QA2, QA3))
    button1.pack()
    
    txt = tk.Text(height=1, width = 50)
    txt.pack()

    button2 = tk.Button(window, text="Проверить параметры", command = lambda: check_params(txt))
    button2.pack()

    button3 = tk.Button(window, text="Рассчитать таблицу значений", command = lambda : calculate_values(QA4))
    button3.pack()
    
    button4 = tk.Button(window, text="Записать таблицу значений в файл", command = export_values)
    button4.pack()
    
    button5 = tk.Button(window, text="Считать таблицу значений из файла", command = import_values)
    button5.pack()
    
    
    
    button9 = tk.Button(window, text="Закрыть приложение", command = lambda: close(window))
    button9.pack()
    
    canvas = tk.Canvas(window, width=550, height=400)
    img = Image.open("picture.png")
    img = img.resize((550, 400)) 
    img_tk = tk.PhotoImage(file="picture.png")
    QA.img_tk = img_tk
    image_object_id = canvas.create_image(10, 12, anchor=tk.NW, image=img_tk)
    canvas.pack()

    button6 = tk.Button(window, text="Нарисовать график", command=lambda: draw_graph(canvas, id=image_object_id, img_tk=QA.img_tk))
    button6.pack()
     
    button7 = tk.Button(window, text="Сохранить график", command = lambda: save_graph())
    button7.pack()

    button8 = tk.Button(window, text="Очистить график", command = lambda: clear_graph(canvas, id=image_object_id, img_tk=QA.img_tk))
    button8.pack()

    window.mainloop()


class QA():
    def __init__(self, frame, text: str):
        self.label = tk.Label(frame, text=text)
        self.entry = tk.Entry(frame)
        self.label.pack(side = tk.LEFT)
        self.entry.pack(side = tk.LEFT)
        self.img_tk = None

    def get_value(self):
        return self.entry.get()

create_window()