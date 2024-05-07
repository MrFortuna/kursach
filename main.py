import tkinter as tk
from binary_tree import Person, BinaryTree, tree
from functions import *


main = tk.Tk()
main.geometry("500x300")
main.title("Гобечия В. Б., Курсовая работа, 1 курс, Вариант 60")

global file
file = open("Relatives.txt", "w")

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

btns = tk.Frame()
btns.pack(pady=40)

tree_app_btn = tk.Button(btns, text="Запись", command=lambda: tree_app(tree, full_name, birth_date, gender), width=20)
tree_app_btn.pack()

read_tree_btn = tk.Button(btns, text='Прочитать дерево', command=lambda: read_tree(tree), width=20)
read_tree_btn.pack()

delete_person_btn = tk.Button(btns, text="Удалить", command=lambda: delete_person(tree, full_name.get(), birth_date.get(), gender.get(), full_name, birth_date, gender), width=20)
delete_person_btn.pack()

change_person_btn = tk.Button(btns, text="Изменить данные...", command=lambda: change_person(full_name.get(), birth_date.get(), gender.get(), tree), width=20)
change_person_btn.pack()

info_btn = tk.Button(btns, text="*справка", command=info, width=20)
info_btn.pack(pady=20)


if __name__ == "__main__":
    main.mainloop()