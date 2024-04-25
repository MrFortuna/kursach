class Person():
    def __init__(self, data: dict) -> None:
        self.data = data
        self.right = self.left = None


class BinaryTree():
    def __init__(self) -> None:
        self.root = None

    def __find(self, person: object, parent: dict, age: int, name: str):
        if age == person.data['age'] and name == person.data['name']:
            return person, parent, True

        if age <= person.data['age']:
            if person.left:
                return self.__find(person.left, person, age, name)

        elif age > person.data['age']:
            if person.right:
                return self.__find(person.right, person, age, name)

        return person, parent, False

    def append(self, person: Person) -> dict:
        if self.root is None:
            self.root = person
            return person

        parent, x, exist = self.__find(self.root, None, person.data['age'], person.data['name'])

        if not exist and parent:
            if person.data['age'] < parent.data['age']:
                parent.left = person
            else:
                parent.right = person
        return parent

    def show(self, root: object) -> None:
        if root is None:
            return

        self.show(root.left)
        print(root.data)
        self.show(root.right)

    def delete(self, person: dict) -> dict:
        if self.root.data == person:
            if self.root.right:
                self.root = self.root.right
            else:
                self.root = self.root.left
            return person

        person, parent, exist = self.__find(self.root, None, person['age'], person['name'])
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
            return Person(person)

        person, parent, exist = self.__find(self.root, None, person['age'], person['name'])

        if exist:
            self.delete(person.data)
            self.append(Person(changes))
            return Person(person)






list = [{'name': 'Егор', 'age': 95}, {'name': 'Дима', 'age': 40}, {'name': 'Маша', 'age': 20}, {'name': 'Боря', 'age': 5}, {'name': 'Гена', 'age': 3}, {'name': 'Антон', 'age': 3}]

tree = BinaryTree()

a = {'name': 'Боря', 'age': 5}
b = {"name":"Леша", "age":10}
c

for i in list:
    tree.append(Person(i))



tree.show(tree.root)
print('---------')
tree.change(tree.root, a, b)
print('---------')
tree.show(tree.root)