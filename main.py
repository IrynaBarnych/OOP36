# Реалізуйте базу даних зі штрафами податкової інспекції.
# Ідентифікувати кожну конкретну людину буде персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання.

class Person:
    def __init__(self, person_id, name, city):
        self.id = person_id
        self.name = name
        self.city = city

class Penalty:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

class PenaltyNode:
    def __init__(self, penalty):
        self.penalty = penalty
        self.left = None
        self.right = None

class TaxDatabase:
    def __init__(self):
        self.people = {}

    def add_person(self, person):
        if person.id not in self.people:
            self.people[person.id] = {"person": person, "penalties": None}

    def add_penalty(self, person_id, penalty):
        if person_id in self.people:
            new_penalty_node = PenaltyNode(penalty)
            self.people[person_id]["penalties"] = self._insert_penalty(self.people[person_id]["penalties"], new_penalty_node)

    def display_database(self):
        for person_id, data in self.people.items():
            person = data["person"]
            penalties = data["penalties"]
            print(f"Ідентифікаційний номер особи: {person.id}, Ім'я: {person.name}")
            if penalties is not None:
                self._display_penalties(penalties)
            else:
                print("Штрафів немає")

    def _display_penalties(self, penalty_node):
        if penalty_node:
            self._display_penalties(penalty_node.left)
            print(f"  Штраф: {penalty_node.penalty.description}, Сума: {penalty_node.penalty.amount}")
            self._display_penalties(penalty_node.right)

    def _insert_penalty(self, root, new_penalty_node):
        if not root:
            return new_penalty_node
        if new_penalty_node.penalty.amount < root.penalty.amount:
            root.left = self._insert_penalty(root.left, new_penalty_node)
        else:
            root.right = self._insert_penalty(root.right, new_penalty_node)
        return root

    def remove_penalty(self, root, description):
        if not root:
            return root

        if description < root.penalty.description:
            root.left = self.remove_penalty(root.left, description)
        elif description > root.penalty.description:
            root.right = self.remove_penalty(root.right, description)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            min_node = self._min_value_node(root.right)
            root.penalty = min_node.penalty
            root.right = self.remove_penalty(root.right, min_node.penalty.description)

        return root

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def display_person_data(self, person_id):
        data = self.people.get(person_id)
        if data is not None:
            person = data["person"]
            penalties = data["penalties"]
            print(f"Ідентифікаційний номер особи: {person.id}, Ім'я: {person.name}")
            if penalties is not None:
                self._display_penalties(penalties)
            else:
                print("Штрафів немає")
        else:
            print(f"Особи з ідентифікаційним номером {person_id} не існує в базі даних.")

    def display_penalty_type_data(self, penalty_type):
        found = False
        for person_id, data in self.people.items():
            penalties = data["penalties"]
            if penalties is not None:
                self._display_penalties_by_type(penalties, penalty_type, person_id)
        if not found:
            print(f"Штрафів за типом '{penalty_type}' не знайдено в базі даних.")

    def _display_penalties_by_type(self, penalty_node, penalty_type, person_id):
        if penalty_node:
            self._display_penalties_by_type(penalty_node.left, penalty_type, person_id)
            if penalty_node.penalty.description == penalty_type:
                found = True
                person = self.people[person_id]["person"]
                print(f"Ідентифікаційний номер особи: {person.id}, Ім'я: {person.name}")
                print(f"  Штраф: {penalty_node.penalty.description}, Сума: {penalty_node.penalty.amount}")
            self._display_penalties_by_type(penalty_node.right, penalty_type, person_id)

    def display_city_data(self, city):
        found = False
        for person_id, data in self.people.items():
            person = data["person"]
            penalties = data["penalties"]
            if person.city == city and penalties is not None:
                found = True
                print(f"Ідентифікаційний номер особи: {person.id}, Ім'я: {person.name}, Місто: {person.city}")
                self._display_penalties(penalties)

        if not found:
            print(f"Штрафів для осіб з містом '{city}' не знайдено в базі даних.")

    def add_new_person_info(self, person_id, name, city):
        new_person = Person(person_id, name, city)
        self.add_person(new_person)

    def add_penalty_to_person(self, person_id, penalty):
        if person_id in self.people:
            new_penalty_node = PenaltyNode(penalty)
            self.people[person_id]["penalties"] = self._insert_penalty(self.people[person_id]["penalties"],
                                                                       new_penalty_node)
            print(f"Штраф додано до особи з ідентифікаційним номером {person_id}.")
        else:
            print(f"Особи з ідентифікаційним номером {person_id} не існує в базі даних. Додавання штрафу не виконано.")

    def remove_penalty_from_person(self, person_id, penalty_description):
        if person_id in self.people:
            penalties = self.people[person_id]["penalties"]
            if penalties is not None:
                self.people[person_id]["penalties"] = self.remove_penalty(penalties, penalty_description)
            else:
                print(f"Особа з ідентифікаційним номером {person_id} не має жодного штрафу. Видалення не виконано.")
        else:
            print(f"Особи з ідентифікаційним номером {person_id} не існує в базі даних. Видалення не виконано.")

    def update_person_info(self, person_id, new_name, new_city):
        if person_id in self.people:
            self.people[person_id]["person"].name = new_name
            self.people[person_id]["person"].city = new_city
            print(f"Інформацію про особу з ідентифікаційним номером {person_id} змінено.")


tax_database = TaxDatabase()

person1 = Person(1, "Тарас Шевченко", "Київ")
person2 = Person(2, "Іван Франко", "Суми")

new_person_id = 3
new_person_name = "Леся Українка"
new_person_city = "Львів"

tax_database.add_person(person1)
tax_database.add_person(person2)

penalty1 = Penalty("Запізнене подання податкових документів", 100)
penalty2 = Penalty("Не заплачено", 50)

tax_database.add_penalty(1, penalty1)
tax_database.add_penalty(1, penalty2)
tax_database.add_penalty(2, penalty1)

tax_database.add_new_person_info(new_person_id, new_person_name, new_person_city)

print("\nВідображення податкової бази даних:")
tax_database.display_database()

print("\nВідображення даних за конкретним ідентифікаційним номером:")
tax_database.display_person_data(1)

print("\nВідображення даних за конкретним типом штрафу:")
tax_database.display_penalty_type_data("Запізнене подання податкових документів")

print("\nВідображення даних за конкретним містом:")
tax_database.display_city_data("Київ")

print("\n Відображення податкової бази даних після додавання нової людини:")
tax_database.display_database()

new_penalty3 = Penalty("Несплачено податок на нерухомість", 200)
tax_database.add_penalty_to_person(1, new_penalty3)

print("\n Відображення податкової бази даних після додавання нового штрафу:")
tax_database.display_database()


tax_database.remove_penalty_from_person(1, "Запізнене подання податкових документів")

print("\n Відображення податкової бази даних після видалення штрафу:")
tax_database.display_database()

tax_database.update_person_info(1, "Нове Ім'я", "Нове Місто")

print("\n Відображення податкової бази даних після зміни інформації про особу:")
tax_database.display_database()