import tkinter as tk
from tkinter import END
from binary_tree import Person, BinaryTree


def tree_app(tree, full_name, birth_date, gender):
    person = {"name":full_name.get(), "date_birth":birth_date.get(), "gender":gender.get()}
    tree.append(Person(person))
    clear_entry(full_name, birth_date, gender)

def read_tree(tree):
    file = open("Relatives.txt", "w")
    tree.show(tree.root)
    file.close()

def delete_person(tree, name, birth_date, gender, ent1, ent2, ent3):
    tree.delete({"name":name, "date_birth":birth_date, "gender":gender})
    clear_entry(ent1, ent2, ent3)

def info():
    _win_inf = tk.Tk()
    _win_inf.title("Справка")
    _win_inf.geometry("750x100")

    tk.Label(_win_inf, text="1. Данная курсовая работа представляет из себя программу, храняющую информацию по родственникам в виде бинарного дерева.\n \
             2. Так как дерево бинарное, следовательно, у каждого родителя не может быть более двух потомков.\n \
             3. В дате допускаются только значащие нули.\n\
             4. ФИО вводится через пробел - язык не имеет значения.\n\
             5. Не допускается наличие внутри одного дерева людей с одинаковыми данными.").pack()

def show_tree(tree):
    tree_list = tk.Tk()
    tree_list.geometry("700x200")
    tree_list.title("Генеалогическое дерево")


def clear_entry(ent1, ent2, ent3):
    ent1.delete(0, END)
    ent2.delete(0, END)
    ent3.delete(0, END)

def change_person(full_name, birth_date, gender, tree):
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
