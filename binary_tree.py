from datetime import datetime

#Класс-узел для дерева
class Person():
    #Инициализация: запись данных по человеку и определение методов left и right
    #Data представляет из себя словарь с набором параметров, определенным заданием
    def __init__(self, data: dict) -> None:
        self.data = data
        self.right = self.left = None
        self.__get_age(self.data)
    #Обработка даты рождения для получения возраста - для более удобного поиска и записи в "дерево"
    def __get_age(self, person: dict) -> None:
        __today = datetime.today()
        __person__date = list(map(int, person["date_birth"].split(".")))
        __age = __today.year - __person__date[2] - ((__today.month, __today.day) < (__person__date[1], __person__date[0]))
        person["age"] = __age

#Класс структуры данных Бинарное Дерево
class BinaryTree():
    #Инициализация с определением метода root - то есть корневогоь элемента
    def __init__(self) -> None:
        self.root = None
        self.counter = 0
    #Вспомогательный метод для поиска объекта внутри структуры по ключам
    def __find(self, person: object, parent: dict, age: int, name: str, gender: str, birthday: str):
        if name == person.data['name'] and gender == person.data['gender'] and birthday == person.data['date_birth']:
            return person, parent, True

        if age <= person.data['age']:
            if person.left:
                return self.__find(person.left, person, age, name, gender, birthday)

        elif age > person.data['age']:
            if person.right:
                return self.__find(person.right, person, age, name, gender, birthday)

        return person, parent, False
    #Добавление элемента внутрь структуры
    def append(self, person: Person) -> dict:
        if self.root is None:
            self.root = person
            return person

        parent, x, exist = self.__find(self.root, None, person.data['age'], person.data['name'], person.data['gender'], person.data['date_birth'])

        if not exist and parent:
            if person.data['age'] <= parent.data['age']:
                parent.left = person
            else:
                parent.right = person
        return parent
    #Обход дерева и последующая упорядоченная запись в файл, с заполнением list people, для последующего вывода данных на форму
    def show(self, node: object, people: list) -> list:
        if node is None:
            return
        self.show(node.right, people)
        with open("Relatives.txt", "a") as file:
            file.write(f"Ф.И.О: {node.data['name']}\n")
            file.write(f"Дата рождения: {node.data['date_birth']}\n")
            file.write(f"Пол: {node.data['gender']}\n")
            file.write("--------------------------------------\n")
        people.append([node.data['name'], node.data['date_birth'], node.data['gender']])
        self.show(node.left, people)
        return people
    #Удаление обьекта из структуры по ключам, с использованеи вспомогательного метода __find
    def delete(self, person: dict) -> dict:
        if self.root.data == person:
            if self.root.right:
                self.root = self.root.right
            else:
                self.root = self.root.left
            return person

        person, parent, exist = self.__find(self.root, None, person['age'], person['name'], person['gender'], person['date_birth'])
        if exist:

            if person.left is None and person.right is None:
                if parent.right:
                    if parent.right.data == person:
                        parent.right = None
                elif parent.left:
                    parent.left = None

            if (person.left is None and person.right is not None) or (person.left is not None and person.right is not None):
                if parent.right:
                    if parent.right.data == person:
                        parent.right = person.right
                elif parent.left:
                    parent.left = person.right

            if person.left is not None and person.right is None:
                if parent.right:
                    if parent.right.data == person:
                        parent.right = person.left
                elif parent.left:
                    parent.left = person.left

        return person
    #Изменение данных обьекта
    #Производится поиск обьекта по ключам, далее удаление обьекта и добавление уже измененных данных
    def change(self, root: object, person: dict, changes: dict) -> Person:
        if root.data == person:
            self.delete(person)
            self.append(Person(changes))
            return Person(changes)

        person, parent, exist = self.__find(self.root, None, person['age'], person['name'], person['gender'], person['date_birth'])
        if exist:
            print(person.data)
            self.delete(person.data)
            self.append(Person(changes))
            return Person(changes)
#Обьявление экземпляра класса BinaryTree
tree = BinaryTree()