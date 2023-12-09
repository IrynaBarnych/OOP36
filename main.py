# Завдання 1
# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати, змінювати, видаляти переклади слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів
# (визначаємо популярність спираючись на лічильник звернень);
# ■ відображати топ-10 найнепопулярніших слів (визначаємо непопулярність спираючись на лічильник звернень).
# Використовуйте дерево для виконання цього завдання.

# Завдання 1
# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати, змінювати, видаляти переклади слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів
# (визначаємо популярність спираючись на лічильник звернень);
# ■ відображати топ-10 найнепопулярніших слів (визначаємо непопулярність спираючись на лічильник звернень).
# Використовуйте дерево для виконання цього завдання.

class TreeNode:
    def __init__(self, key, translation):
        self.key = key
        self.translation = translation
        self.left = None
        self.right = None
        self.counter = 1

class DictionaryTree:
    def __init__(self, initial_data=None):
        self.root = None
        self.popular = []

        if initial_data:
            for key, translation in initial_data:
                self.add_word(key, translation)

    def add_word(self, key, translation):
        if not self.root:
            self.root = TreeNode(key, translation)
        else:
            self._add_word(self.root, key, translation)

    def _add_word(self, node, key, translation):
        if key == node.key:
            node.translation = translation
            node.counter += 1
        elif key < node.key:
            if node.left is None:
                node.left = TreeNode(key, translation)
            else:
                self._add_word(node.left, key, translation)
        else:
            if node.right is None:
                node.right = TreeNode(key, translation)
            else:
                self._add_word(node.right, key, translation)

    def display_top_popular(self):
        self.popular = []
        self._get_popular_words(self.root)
        if self.popular:
            print("Топ 10")
            for word in self.popular[:10]:
                print(f'{word.key}: {word.counter} було додано разів')
        else:
            print("Слова відсутні")

    def _get_popular_words(self, node):
        if node is not None:
            self._get_popular_words(node.left)
            self.popular.append(node)
            self.popular.sort(key=lambda x: x.counter, reverse=True)
            if len(self.popular) > 10:
                self.popular.pop()
            self._get_popular_words(node.right)

    def display_top_unpopular(self):
        self.popular = []
        self._get_unpopular_words(self.root)
        if self.popular:
            print("\nТоп-10 найнепопулярніших слів:")
            for word in reversed(self.popular[-10:]):
                print(f'{word.key}: {word.counter} було додано разів')
        else:
            print("Слова відсутні")

    def _get_unpopular_words(self, node):
        if node is not None:
            self._get_unpopular_words(node.left)
            self.popular.append(node)
            self.popular.sort(key=lambda x: x.counter)
            if len(self.popular) > 10:
                self.popular.pop()
            self._get_unpopular_words(node.right)

    def display_translations(self, key, is_ukrainian=False):
        node = self._search(self.root, key, is_ukrainian)
        if node:
            print(f'{node.key}: {node.translation}')
            return node.translation
        else:
            print(f'{key} не знайдено в словнику')
            return None

    def _search(self, node, key, is_ukrainian=False):
        if node is None or node.key.lower() == key.lower():
            return node
        if (is_ukrainian and key.lower() < node.key.lower()) or (not is_ukrainian and key < node.key):
            return self._search(node.left, key, is_ukrainian)
        elif (is_ukrainian and key.lower() > node.key.lower()) or (not is_ukrainian and key > node.key):
            return self._search(node.right, key, is_ukrainian)

    def update_translation(self, key, old_translation, new_translation):
        node = self._search(self.root, key)
        if node and node.translation == old_translation:
            node.translation = new_translation
            print(f'Переклад для {key} оновлено: {new_translation}')
        elif node:
            print(f'{old_translation} не є поточним перекладом для {key}')
        else:
            print(f'{key} не знайдено в словнику')

    def delete_translations(self, key):
        node = self._search(self.root, key)
        if node:
            confirm = input(f'Ви впевнені, що хочете видалити перший варіант перекладу для {key}? (Так або ні): ')
            if confirm.lower() == "так":
                node.left = None
                node.right = None
                print(f'Початковий переклад для {key} видалено')
        else:
            print(f'{key} не знайдено в словнику')


    def add_translation(self, key, new_translation):
        node = self._search(self.root, key)
        if node:
            self._add_word(node, key, new_translation)
            print(f'Переклад для {key} додано: {new_translation}')
        else:
            self.add_word(key, new_translation)
            print(f'{key}: {new_translation} додано до словника')

    def add_word_with_translation(self, key, translation):
        node = self._search(self.root, key)
        if node:
            print(f'{key} вже присутнє в словнику')
        else:
            self.add_word(key, translation)
            print(f'{key}: {translation} додано до словника')

    def add_word_english(self, key, translation):
        node = self._search(self.root, key)
        if node:
            print(f'{key} вже присутнє в словнику')
        else:
            self.add_word(key, translation)
            print(f'{key}: {translation} додано до словника')

    def print_menu(self):
        print("\nМеню:")
        print("1. Надати початкове введення даних для словника")
        print("2. Відобразити слово та його переклади")
        print("3. Додати, змінити, видалити переклади слова (англійська мова)")
        print("4. Додати, змінити, видалити переклади слова (українська мова)")
        print("5. Відобразити топ-10 найпопулярніших слів")
        print("6. Відобразити топ-10 найнепопулярніших слів")
        print("0. Вихід")

    def main(self):
        initial_data = [
            ("apple", "яблуко"),
            ("apple", "яблучко"),
            ("banana", "банан"),
            ("kiwi", "ківі"),
            ("apricot", "абрикос"),
            ("cherry", "вишня"),
            ("plum", "слива"),
            ("grape", "виноград"),
            ("pear", "груша"),
            ("apricot", "алича"),
            ("strawberry", "полуниця"),
            ("raspberry", "малина"),
            ("яблуко", "apple"),
            ("яблучко", "apple"),
            ("банан", "banana"),
            ("ківі", "kiwi"),
            ("абрикос", "apricot"),
            ("вишня", "cherry"),
            ("слива", "plum"),
            ("виноград", "grape"),
            ("груша", "pear"),
            ("алича", "apricot"),
            ("полуниця", "strawberry"),
            ("малина", "raspberry")
        ]

        dictionary = DictionaryTree(initial_data)

        while True:
            self.print_menu()
            choice = input("Оберіть опцію (введіть число): ")

            if choice == "0":
                print("Дякую за використання програми!")
                break
            elif choice == "1":
                key = input("Введіть слово: ")
                new_translation = input("Введіть переклад: ")
                dictionary.add_word(key, new_translation)
            elif choice == "2":
                key = input("Введіть слово: ")
                displayed_translation = dictionary.display_translations(key)
            elif choice == "3":
                key = input("Введіть слово (англ. мова): ")
                displayed_translation = dictionary.display_translations(key)
                if displayed_translation is not None:
                    translation = input("Введіть переклад слова: ")
                    new_translation = input("Введіть новий переклад: ")
                    dictionary.update_translation(key, displayed_translation, new_translation)

                    confirm = input("Чи бажаєте видалити початковий переклад слова? (Так або ні): ")
                    if confirm.lower() == "так":
                        dictionary.delete_translations(key)
            elif choice == "4":
                key = input("Введіть слово (укр. мова): ")
                displayed_translation = dictionary.display_translations(key)
                if displayed_translation is not None:
                    translation = input("Введіть переклад слова: ")
                    new_translation = input("Введіть новий переклад: ")
                    dictionary.update_translation(key, displayed_translation, new_translation)

                    confirm = input("Чи бажаєте видалити переклади слова? (Так або ні): ")
                    if confirm.lower() == "так":
                        dictionary.delete_translations(key)

            elif choice == "5":
                dictionary.display_top_popular()
            elif choice == "6":
                dictionary.display_top_unpopular()
            else:
                print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    dictionary_instance = DictionaryTree()
    dictionary_instance.main()