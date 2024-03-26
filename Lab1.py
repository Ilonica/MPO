import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import numdifftools as nd
from tkinter import scrolledtext

# Функции для оптимизации
def target_function(x, y):
    return ((x ** 2 + y - 11) ** 2) + ((x + y ** 2 - 7) ** 2) # функция Химмельблау

# Функция градиента
def gradient(function, input):
    ret = np.empty(len(input))
    for i in range(len(input)):
        fg = lambda x: partial_function(function, input, i, x)
        ret[i] = nd.Derivative(fg)(input[i])
    return ret

# Функция частной производной
def partial_function(f___, input, pos, value):
    tmp = input[pos]
    input[pos] = value
    ret = f___(*input)
    input[pos] = tmp
    return ret

# Функция для кнопки "Выполнить"
def run_optimization():
    x0 = x_var.get()
    y0 = y_var.get()
    step = step_var.get()
    max_iterations = iterations_var.get()
    delay = delay_var.get()
    ax.cla()
    x_range = np.linspace(x_interval_min.get(), x_interval_max.get(), 100)
    y_range = np.linspace(y_interval_min.get(), y_interval_max.get(), 100)
    X, Y = np.meshgrid(x_range, y_range)
    Z = target_function(X, Y)
    ax.plot_surface(X, Y, Z, cmap='plasma',alpha=0.7)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xticks(np.arange(x_interval_min.get(), x_interval_max.get() + 1, x_axis_interval.get()))
    ax.set_yticks(np.arange(y_interval_min.get(), y_interval_max.get() + 1, y_axis_interval.get()))
    ax.set_title("Алгоритм градиентного спуска с постоянным шагом")

    function_choice = function_var.get()
    if function_choice == "Функция Химмельблау":
        target_func = target_function

    results = []
    results_text.config(state=tk.NORMAL)
    results_text.delete(1.0, tk.END)
    for k in range(max_iterations):
        (gx, gy) = gradient(target_func, [x0, y0])

        if np.linalg.norm((gx, gy)) < 0.0001:
            break
        x1, y1 = x0 - step * gx, y0 - step * gy
        f1 = target_func(x1, y1)
        f0 = target_func(x0, y0)

        while not f1 < f0:
            step = step / 2
            x1, y1 = x0 - step * gx, y0 - step * gy
            f1 = target_func(x1, y1)
            f0 = target_func(x0, y0)

        if np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2) < 0.0001 and abs(f1 - f0) < 0.0001:
            x0, y0 = x1, y1
            break
        else:
            x0, y0 = x1, y1

        results.append((x0, y0, k,f1))
        ax.scatter([x0], [y0], [f1], color='red',s=10)
        results_text.insert(tk.END,
                           f"Шаг {k}: Координаты ({x0:.2f}, {y0:.2f}), Значение функции: {f1:.7f}\n")
        results_text.yview_moveto(1)
        canvas.draw()
        root.update()
        time.sleep(delay)

    length=len(results)-1
    ax.scatter(results[length][0], results[length][1], results[length][3], color='black',marker='x',s=60)
    results_text.insert(tk.END,
                        f"Результат:\nКоординаты ({results[length][0]:.8f}, {results[length][1]:.8f})\nЗначение функции: {results[length][3]:.8f}\n")
    results_text.yview_moveto(1)
    results_text.config(state=tk.DISABLED)

# Создание окна приложения
root = tk.Tk()
root.title("Methods of search engine optimization")
root.geometry("1396x868")

# Инициализация графика при запуске программы
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()

# Вкладка для параметров задачи
param_frame = ttk.Frame(root, padding=(15, 0))
param_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Вкладка для графика
canvas_widget.pack(side=tk.LEFT, padx=20)

notebook = ttk.Notebook(root)
notebook.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Меню
param_frame = ttk.Frame(notebook,padding=(15, 0))
notebook.add(param_frame, text="Lab 1")

param_frame2 = ttk.Frame(notebook)
notebook.add(param_frame2, text="Lab 2")

param_frame3 = ttk.Frame(notebook)
notebook.add(param_frame3, text="Lab 3")

param_frame4 = ttk.Frame(notebook)
notebook.add(param_frame4, text="Lab 4")

param_frame5 = ttk.Frame(notebook)
notebook.add(param_frame5, text="Lab 5")

param_frame6 = ttk.Frame(notebook)
notebook.add(param_frame6, text="Lab 6")

param_frame7 = ttk.Frame(notebook)
notebook.add(param_frame7, text="Lab 7")

param_frame8 = ttk.Frame(notebook)
notebook.add(param_frame8, text="Lab 8")


# Параметры задачи
ttk.Label(param_frame, text="", font=("Helvetica", 10)).grid(row=0, column=0)
ttk.Label(param_frame, text="Начальная точка X", font=("Helvetica", 10)).grid(row=1, column=0)
ttk.Label(param_frame, text="Начальная точка Y", font=("Helvetica", 10)).grid(row=2, column=0)
ttk.Label(param_frame, text="Начальный шаг", font=("Helvetica", 10)).grid(row=3, column=0)
ttk.Label(param_frame, text="Число итераций", font=("Helvetica", 10)).grid(row=4, column=0)
ttk.Label(param_frame, text="Задержка", font=("Helvetica", 10)).grid(row=5, column=0)

x_var = tk.DoubleVar(value=-1)
y_var = tk.DoubleVar(value=-1)
step_var = tk.DoubleVar(value=0.5)
iterations_var = tk.IntVar(value=100)
delay_var = tk.DoubleVar(value=0.5)

x_entry = ttk.Entry(param_frame, textvariable=x_var)
y_entry = ttk.Entry(param_frame, textvariable=y_var)
step_entry = ttk.Entry(param_frame, textvariable=step_var)
iterations_entry = ttk.Entry(param_frame, textvariable=iterations_var)
delay_entry = ttk.Entry(param_frame, textvariable=delay_var)

x_entry.grid(row=1, column=1)
y_entry.grid(row=2, column=1)
step_entry.grid(row=3, column=1)
iterations_entry.grid(row=4, column=1)
delay_entry.grid(row=5, column=1)

# Горизонтальная полоса
separator = ttk.Separator(param_frame, orient="horizontal")
separator.grid(row=7, column=0, columnspan=2, sticky="ew",pady=10)

# Параметры функции
ttk.Label(param_frame, text="Функция и отображение ее графика", font=("Helvetica", 12)).grid(row=9, column=0,pady=10)
ttk.Label(param_frame, text="Функция для минимизации", font=("Helvetica", 10)).grid(row=10, column=0)
function_choices = ["Функция Химмельблау"]
function_var = tk.StringVar(value=function_choices[0])
function_menu = ttk.Combobox(param_frame, textvariable=function_var, values=function_choices,width=22)
function_menu.grid(row=10, column=1,pady=5)
ttk.Label(param_frame, text="X интервал (min)", font=("Helvetica", 10)).grid(row=11, column=0)
ttk.Label(param_frame, text="X интервал (max)", font=("Helvetica", 10)).grid(row=12, column=0)
ttk.Label(param_frame, text="Y интервал (min)", font=("Helvetica", 10)).grid(row=13, column=0)
ttk.Label(param_frame, text="Y интервал (max)", font=("Helvetica", 10)).grid(row=14, column=0)
ttk.Label(param_frame, text="Ось X интервал", font=("Helvetica", 10)).grid(row=16, column=0)
ttk.Label(param_frame, text="Ось Y интервал", font=("Helvetica", 10)).grid(row=17, column=0)

# И еще одна горизонтальная полоса
separator = ttk.Separator(param_frame, orient="horizontal")
separator.grid(row=18, column=0,columnspan=2, sticky="ew",pady=10)

x_interval_min = tk.DoubleVar(value=-5)
x_interval_max = tk.DoubleVar(value=5)
y_interval_min = tk.DoubleVar(value=-5)
y_interval_max = tk.DoubleVar(value=5)
x_axis_interval = tk.IntVar(value=2)
y_axis_interval = tk.IntVar(value=2)
x_interval_min_entry = ttk.Entry(param_frame, textvariable=x_interval_min)
x_interval_max_entry = ttk.Entry(param_frame, textvariable=x_interval_max)
y_interval_min_entry = ttk.Entry(param_frame, textvariable=y_interval_min)
y_interval_max_entry = ttk.Entry(param_frame, textvariable=y_interval_max)
x_axis_interval_entry = ttk.Entry(param_frame, textvariable=x_axis_interval)
y_axis_interval_entry = ttk.Entry(param_frame, textvariable=y_axis_interval)

x_interval_min_entry.grid(row=11, column=1)
x_interval_max_entry.grid(row=12, column=1)
y_interval_min_entry.grid(row=13, column=1)
y_interval_max_entry.grid(row=14, column=1)
x_axis_interval_entry.grid(row=16, column=1)
y_axis_interval_entry.grid(row=17, column=1)

# Функция для очистки текстового поля
def clear_results():
    results_text.config(state=tk.NORMAL)
    results_text.delete(1.0, tk.END)
    results_text.config(state=tk.DISABLED)

# Кнопка "Выполнить"
apply_settings_button = tk.Button(param_frame, text="Выполнить", command=run_optimization, bg='#f9e3fa', fg='black', font=('Helvetica', 15))
apply_settings_button.grid(row=70, column=0, padx=0, pady=20, sticky="nsew", columnspan=2)

# Кнопка "Очистить"
clear_button = tk.Button(param_frame, text="Очистить", command=clear_results, bg='#E6E6FA', fg='black', font=('Helvetica', 15))
clear_button.grid(row=90, column=0, padx=0, pady=0,  sticky="nsew", columnspan=2)

ttk.Label(param_frame, text="Выполнение и результаты", font=("Helvetica", 12)).grid(row=20, column=0, pady=10)
results_text = scrolledtext.ScrolledText(param_frame, wrap=tk.WORD, height=18, width=40, padx=2, state=tk.DISABLED)
results_text.grid(row=21, column=0, padx=0, sticky="nsew", columnspan=2)

root.mainloop()
