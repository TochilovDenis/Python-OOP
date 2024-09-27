# Создание класс для User
class User:
    # Конструктор класса User
    def __init__(self):
        self.name = ""  # создание и инициализация переменной name
        self.surname = "" # создание и инициализация переменной surname
        self.patronymic = "" # создание и инициализация переменной patronymic
        self.age = 0    # # создание и инициализация переменной age

user = User() # создание переменной объекта для User
user.name = "Denis" # присваиваем переменной имена
user.surname = "Tochilov" # присваиваем переменной фамилия
user.patronymic = "Nikolaevich"  # присваиваем переменной отечество
user.age = 34 # присваиваем переменной возраста
user.new_attribute = "Это не существующий при создании класса аттрибут теперь там существует"

# выводим на экран
print(user.name, user.surname, user.patronymic, user.age, user.new_attribute)