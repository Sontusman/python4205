import tkinter as tk
from task_3_4 import matrix2
import math
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import warnings
warnings.filterwarnings("ignore")

matrix = None
plotting_history = []


def set_params(QA1, QA2, QA3) -> None:
    global matrix
    if QA1.get_value() == "":
        N, x0, dx = 100, 0, 1
    else:
        N, x0, dx = int(QA3.get_value()), float(QA1.get_value()), float(QA2.get_value())
    matrix = matrix2(N=N, x0=x0, dx=dx)
    print("Параметры установлены")

def check_params(txt) -> None:
    global matrix
    text = f"N: {matrix.N}, x0: {matrix.x0}, dx: {matrix.dx}"
    txt.delete('1.0', tk.END)
    txt.insert('1.0', text)

def calculate_values(QA4, txt) -> None:
    if QA4.get_value() == "":
        func = "sin"
    else:
        func = QA4.get_value()
    global matrix
    func = getattr(math, func)
    matrix.setx()
    matrix.sety(func)
    text = ""
    for i in range(len(matrix.x)):
        text += f"x{i}: {matrix.x[i]}, y{i}: {matrix.y[i]}\n"
    txt.delete('1.0', tk.END)
    txt.insert('1.0', text)

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


def draw_graph(canvas, id, img_tk, fig1, ax1, label):
    matrix.plot(ax1, label=label)
    fig1.savefig("graph_figure.png")
    img = Image.open("graph_figure.png")
    img = img.resize((550, 400))
    QA.img_tk = ImageTk.PhotoImage(img)
    canvas.itemconfig(id, image=QA.img_tk)
    canvas.image = img_tk

def save_graph(fig1):
    fig1.savefig("graph_figure.png")

def clear_graph(canvas, id, img_tk, fig1, ax1):
    global matrix
    matrix=None
    img = Image.open("picture.png")
    img = img.resize((550, 400))
    QA.img_tk = ImageTk.PhotoImage(img)
    canvas.itemconfig(id, image=QA.img_tk)
    canvas.image = img_tk
    ax1.cla()

def close(window):
    window.destroy()

def create_window():
    window = tk.Tk()
    window.title("Давайте строить графики!")

    left_frame = tk.Frame(window, width=200, height=400)
    left_frame.grid(row=0, column=0, padx=10, pady=5)

    right_frame = tk.Frame(window, width=650, height=400)
    right_frame.grid(row=0, column=1, padx=10, pady=5)


    frame1 = tk.Frame(left_frame)
    QA1 = QA(frame1, "Введи x0")
    QA2 = QA(frame1, "Введи dx")
    frame1.pack()

    frame2 = tk.Frame(left_frame)
    QA3 = QA(frame2, "Введи N")
    QA4 = QA(frame2, "Введи функцию")
    frame2.pack()

    button1 = create_button(left_frame, "Задать параметры", lambda: set_params(QA1, QA2, QA3))
    txt = tk.Text(left_frame, height=20, width=50)
    txt.pack()
    button2 = create_button(left_frame, "Проверить параметры", lambda: check_params(txt))
    button3 = create_button(left_frame, "Рассчитать таблицу значений", lambda: calculate_values(QA4, txt))
    button4 = create_button(left_frame, "Записать таблицу значений в файл", export_values)
    button5 = create_button(left_frame, "Считать таблицу значений из файла", import_values)
    button9 = create_button(left_frame, "Закрыть приложение", lambda: close(window))

    canvas = tk.Canvas(right_frame, width=550, height=400)
    img = Image.open("picture.png")
    img = img.resize((550, 400))
    img_tk = tk.PhotoImage(file="picture.png")
    QA.img_tk = img_tk
    image_object_id = canvas.create_image(10, 12, anchor=tk.NW, image=img_tk)
    canvas.pack()
    fig1, ax1 = plt.subplots()
    button6 = create_button(right_frame, "Нарисовать график", lambda: draw_graph(canvas, id=image_object_id, img_tk=QA.img_tk, fig1=fig1, ax1=ax1, label=QA4.get_value()))
    button7 = create_button(right_frame, "Сохранить график", lambda: save_graph(fig1=fig1))
    button8 = create_button(right_frame, "Очистить график", lambda: clear_graph(canvas, id=image_object_id, img_tk=QA.img_tk, fig1=fig1, ax1=ax1))

    window.mainloop()

def create_button(window, text, command):
    button = tk.Button(window, text=text, command = command)
    button.pack()
    return button

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