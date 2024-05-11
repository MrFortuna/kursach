import tkinter as tk
from tkinter import END, Variable, NORMAL, messagebox
from binary_tree import Person, BinaryTree

#Добавление элемента в "дерево"
def tree_app(tree: BinaryTree, full_name, birth_date, gender, ent1=None, ent2=None, ent3=None):
    person = {"name":full_name, "date_birth":birth_date, "gender":gender}
    tree.append(Person(person))
    if ent1 is None:
        return
    else:
        clear_entry(ent1, ent2, ent3)

#Перенос данных "дерева" из структуры на форму и в файл
def read_tree(tree, main, tree_view, explan):
    file = open("Relatives_list.txt", "a+")
    people = []
    people = tree.show(tree.root, people)
    if people is None:
        tree_view.delete(0, END)
    else:
        main.geometry('800x800')
        explan.config(text="СПИСОК РОДСТВЕННИКОВ:")
        for i in range(len(people)):
            m = ''
            for j in people[i]:
                m += str(j) + ' '
                people[i] = m
        tree_view.config(width=70, font="arial", yscrollcommand=1, listvariable=Variable(value=people))

    file.close()

#Чтение данных из файла с последующим вызовом функции записи в "дерево"
def read_from_file(tree, file_name=None):
    if file_name is None:
        messagebox.showerror("Опаньки!", "Похоже, вы не ввели название файла")
    try:
        input_data = open(f"{file_name}", "rt", encoding='utf-8')
    except FileNotFoundError:
        messagebox.showerror("Опаньки!", "Похоже, такого файла не существует(")
    data = input_data.readlines()
    for i in range(len(data) - 1):
        data[i] = data[i][:-1]
        data[i] = data[i].split(",")
        tree_app(tree, data[i][0], data[i][1], data[i][2])
    data[-1] = data[-1].split(",")
    tree_app(tree, data[-1][0], data[-1][1], data[-1][2])

    input_data.close()

#Удаление элемента "дерева" по введенным данным
def delete_person(tree, name, birth_date, gender, ent1, ent2, ent3):
    tree.delete(Person({"name":name, "date_birth":birth_date, "gender":gender}).data)
    clear_entry(ent1, ent2, ent3)

#Справка, аналог readme
def info():
    _win_inf = tk.Tk()
    _win_inf.title("Справка")
    _win_inf.geometry("850x150")

    tk.Label(_win_inf, text="1. Данная курсовая работа представляет из себя программу, храняющую информацию по родственникам в виде бинарного дерева.\n \
             2. Так как дерево бинарное, следовательно, у каждого родителя не может быть более двух потомков.\n \
             3. В дате допускаются только значащие нули.\n\
             4. ФИО вводится через пробел - язык не имеет значения.\n\
             5. Не допускается наличие внутри одного дерева людей с одинаковыми данными.\n\
             6. Формат записи в файле при чтении из файла:\n\
             Фамилия Имя Отчество,Дата Рождения,Пол\n\
             Каждого нового родственника следует писать с новой строки.").pack()

#Очистка полей ввода после некоторых действий
def clear_entry(ent1, ent2, ent3):
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)

#Первоначально: поиск по введенным данным по "дереву" с дальнейшим открытием вспомогательного окна
#для ввода данных, которые заменят собой изначальные данные
def change_person(full_name, birth_date, gender, tree):
    #Непосредственно изменение данных обьекта внутри структуры с последующим закрытием вспомогательного окна
    def changed(person):
        if len(full_name2.get()) == 0:
            new_name = full_name
        else:
            new_name = full_name2.get()
        if len(birth_date2.get()) == 0:
            new_birth_date = birth_date
        else:
            new_birth_date = birth_date2.get()
        if len(gender2.get()) == 0:
            new_gender = gender
        else:
            new_gender = gender2.get()

        new_person = {"name":new_name, "date_birth":new_birth_date, "gender":new_gender}
        new_person = Person(new_person).data
        tree.change(tree.root, person, new_person)

        change_win.destroy()

    change_win = tk.Tk()
    change_win.geometry('500x195')
    change_win.title('Данные, которые надо изменить')

    person = {"name":full_name, "date_birth":birth_date, "gender":gender}
    person = Person(person).data

    warning = tk.Frame(change_win)
    warning.pack()

    tk.Label(warning, text="Введите данные, которые хотите изменить \nДля данных, которые не нужно менять - оставьте окна пустыми").pack()

    enter2 = tk.Frame(change_win)
    enter2.pack(pady=20)

    tk.Label(enter2, text="Введите Фамилию, Имя, Отчество:").grid(row=0, column=0)

    full_name2 = tk.Entry(enter2, width=40)
    full_name2.grid(row=0, column=1)

    tk.Label(enter2, text="Введите дату рождения:").grid(row=1, column=0)

    birth_date2 = tk.Entry(enter2, width=40)
    birth_date2.grid(row=1, column=1)

    tk.Label(enter2, text="Введите пол:").grid(row=2, column=0)

    gender2 = tk.Entry(enter2, width=40)
    gender2.grid(row=2, column=1)

    change_btn = tk.Button(enter2, text="ИЗМЕНИТЬ", command=lambda: changed(person))
    change_btn.grid(row=3, columnspan=2, pady=15)