from datetime import datetime

class Person():
    def __init__(self, data: dict) -> None:
        self.data = data
        self.right = self.left = None
        self.__short_name(self.data)
        self.__get_age(self.data)

    def __get_age(self, person: dict) -> None:
        __today = datetime.today()
        __person__date = list(map(int, person["date_birth"].split(".")))
        __age = __today.year - __person__date[2] - ((__today.month, __today.day) < (__person__date[1], __person__date[0]))
        person["age"] = __age

    def __short_name(self, person: dict) -> None:
        __name = person['name'].split()
        __name[1] = " " + __name[1][0] + "."
        __name[2] = __name[2][0] + "."
        person['short_name'] = "".join(__name)


class BinaryTree():
    def __init__(self) -> None:
        self.root = None
        self.counter = 0

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

    def append(self, person: Person) -> dict:
        if self.root is None:
            self.root = person
            return person

        parent, x, exist = self.__find(self.root, None, person.data['age'], person.data['name'], person.data['gender'], person.data['date_birth'])

        if not exist and parent:
            if person.data['age'] < parent.data['age']:
                parent.left = person
            else:
                parent.right = person
        return parent

    def show(self, node: object) -> list:
        if node is None:
            return
        self.show(node.right)
        with open("Relatives.txt", "a") as file:
            file.write(f"Ф.И.О: {node.data['name']}\n")
            file.write(f"Дата рождения: {node.data['date_birth']}\n")
            file.write(f"Пол: {node.data['gender']}\n")
            file.write("--------------------------------------\n")
        self.show(node.left)

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

    def change(self, root: object, person: dict, changes: dict) -> Person:
        if root.data == person:
            self.delete(person)
            self.append(Person(changes))
            return Person(changes)

        person, parent, exist = self.__find(self.root, None, person['age'], person['name'], person['gender'], person['date_birth'])

        if exist:
            self.delete(person.data)
            self.append(Person(changes))
            return Person(changes)

tree = BinaryTree()