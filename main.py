import tkinter as tk
from binary_tree import Person, BinaryTree, tree
from functions import *


#Основное окно
main = tk.Tk()
main.geometry("500x350")
main.title("Гобечия В. Б., Курсовая работа, 1 курс, Вариант 60")

#Для избежания "накапливания" элементов в файле
global file
file = open("Relatives.txt", "w")

#Фрейм для записи данных
enter = tk.Frame()
enter.pack()

tk.Label(enter, text="Введите Фамилию, Имя, Отчество:").grid(row=0, column=0)

full_name = tk.Entry(enter, width=40)
full_name.grid(row=0, column=1)

tk.Label(enter, text="Введите дату рождения:").grid(row=1, column=0)

birth_date = tk.Entry(enter, width=40)
birth_date.grid(row=1, column=1)

tk.Label(enter, text="Введите пол:").grid(row=2, column=0)

gender = tk.Entry(enter, width=40)
gender.grid(row=2, column=1)

#Фрейм для обработки записанных данных
btns = tk.Frame()
btns.pack(pady=40)

tree_app_btn = tk.Button(btns, text="Запись", command=lambda: tree_app(tree, full_name.get(), birth_date.get(), gender.get(), full_name, birth_date, gender), width=23)
tree_app_btn.pack()

read_tree_btn = tk.Button(btns, text='Прочитать дерево', command=lambda: read_tree(tree, main, tree_view, explan), width=23)
read_tree_btn.pack()

delete_person_btn = tk.Button(btns, text="Удалить", command=lambda: delete_person(tree, full_name.get(), birth_date.get(), gender.get(), full_name, birth_date, gender), width=23)
delete_person_btn.pack()

change_person_btn = tk.Button(btns, text="Изменить данные...", command=lambda: change_person(full_name.get(), birth_date.get(), gender.get(), tree), width=23)
change_person_btn.pack()

read_from_file_btn = tk.Button(btns, text='Прочитать дерево из файла', command=lambda: read_from_file(tree), width=23)
read_from_file_btn.pack()

info_btn = tk.Button(btns, text="*справка", command=info, width=23)
info_btn.pack(pady=20)

explan = tk.Label(btns)
explan.pack(pady=20)

tree_view = tk.Listbox(btns)
tree_view.pack()


if __name__ == "__main__":
    main.mainloop()