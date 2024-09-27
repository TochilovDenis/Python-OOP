# Создание класс для User
class User:
    # Конструктор параметризованный класса User
    def __init__(self, name, surname, patronymic, age):
        self.name = ""  # создание и инициализация переменной name
        self.surname = "" # создание и инициализация переменной surname
        self.patronymic = "" # создание и инициализация переменной patronymic
        self.age = 0    # # создание и инициализация переменной age

user = User("Denis", "Tochilov", "Nikolaevich", 34)

user.new_attribute = "Это не существующий при создании класса аттрибут теперь там существует"

# выводим на экран
print(user, user.new_attribute)