# Создание класс для User
class User:
    # Конструктор параметризованный класса User
    def __init__(self, name, surname, patronymic, age):
        self.name = ""  # создание и инициализация переменной name
        self.surname = "" # создание и инициализация переменной surname
        self.patronymic = "" # создание и инициализация переменной patronymic
        self.age = 0    # # создание и инициализация переменной age

    def __str__(self):
        return (f"Фамилия: {self.surname} | "
                f"Имя: {self.name} | "
                f"Отечество: {self.patronymic} | "
                f"Возраст: {self.age}")

user = User("Denis", "Tochilov", "Nikolaevich", 34)

user.name = "Denis"  # присвоение переменной
user.surname = "Tochilov"  # присвоение переменной
user.patronymic = "Nikolaevich"  # присвоение переменной
user.age = 34  # присвоение переменной
user.new_attribute = "Это не существующий при создании класса аттрибут теперь там существует"

# выводим на экран
print(user)