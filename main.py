import tkinter as tk
from tkinter import Scrollbar, LEFT, Y
from binary_tree import Person, BinaryTree, tree
from functions import *


#Основное окно
main = tk.Tk()
main.geometry("500x350")
main.title("Гобечия В. Б., Курсовая работа, 1 курс, Вариант 60")
main.config(bg="orange")

#Для избежания "накапливания" элементов в файле
global file
file = open("Relatives.txt", "w")

#Фрейм для записи данных
enter = tk.Frame(bg='orange', borderwidth=1, relief='solid')
enter.pack()

tk.Label(enter, text="Введите Фамилию, Имя, Отчество:", bg='orange', font=('system', 14)).grid(row=0, column=0)

full_name = tk.Entry(enter, width=40)
full_name.grid(row=0, column=1)

tk.Label(enter, text="Введите дату рождения:", bg='orange', font=('system', 14)).grid(row=1, column=0)

birth_date = tk.Entry(enter, width=40)
birth_date.grid(row=1, column=1)

tk.Label(enter, text="Введите пол:", bg='orange', font=('system', 14)).grid(row=2, column=0)

gender = tk.Entry(enter, width=40)
gender.grid(row=2, column=1)

#Фрейм для обработки записанных данных
btns = tk.Frame(bg="orange")
btns.pack(pady=40)

tree_app_btn = tk.Button(btns, text="Запись", font=('system', 14), command=lambda: tree_app(tree, full_name.get(), birth_date.get(), gender.get(), full_name, birth_date, gender), width=26)
tree_app_btn.pack()

read_tree_btn = tk.Button(btns, text='Прочитать дерево', font=('system', 14), command=lambda: read_tree(tree, main, tree_view, explan), width=26)
read_tree_btn.pack()

delete_person_btn = tk.Button(btns, text="Удалить", font=('system', 14), command=lambda: delete_person(tree, full_name.get(), birth_date.get(), gender.get(), full_name, birth_date, gender), width=26)
delete_person_btn.pack()

change_person_btn = tk.Button(btns, text="Изменить данные...", font=('system', 14), command=lambda: change_person(full_name.get(), birth_date.get(), gender.get(), tree), width=26)
change_person_btn.pack()

read_from_file_btn = tk.Button(btns, text='Прочитать дерево из файла', font=('system', 14), command=lambda: read_from_file(tree), width=26)
read_from_file_btn.pack()

info_btn = tk.Button(btns, text="*справка", font=('system', 14), command=info, width=26)
info_btn.pack(pady=20)

explan = tk.Label(btns, bg='orange', font="arial")
explan.pack(pady=20)

tree_view_frame = tk.Frame()
tree_view_frame.pack()

tree_view = tk.Listbox(tree_view_frame, yscrollcommand="")
scroll = Scrollbar(tree_view_frame, command=tree_view.yview)
scroll.grid(row=0, column=0)
tree_view.config(yscrollcommand=scroll.set)
tree_view.grid(row=0, column=1)


if __name__ == "__main__":
    main.mainloop()