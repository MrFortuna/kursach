def __find(self, child, age, name):
        if name == child.data['name'] and age == child.data['age']:
            return child, True
        if age < child.data['age']:
            if child.left:
                return self.__find(child.left, age, name)
        if age > child.data['age']:
            if child.right:
                return self.__find(child.right, age, name)
        return child, False

    def append(self, person) -> dict:
        if self.root is None:
            self.root = person
            return person

        child, exist = self.__find(self.root, person.data['age'], person.data['name'])

        if not exist and child:
            if person.data['age'] < child.data['age']:
                child.left = person
            else:
                child.right = person
        return person

    def show(self, node) -> None:
        if node is None:
            return