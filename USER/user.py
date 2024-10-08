# Создание класс для User
class User:
    # Конструктор параметризованный класса User
    def __init__(self, name, surname, patronymic, age):
        self.name = name  # создание и инициализация переменной name
        self.surname = surname # создание и инициализация переменной surname
        self.patronymic = patronymic # создание и инициализация переменной patronymic
        self.age = age    # # создание и инициализация переменной age

    def __str__(self):
        return (f"Фамилия: {self.surname} | "
                f"Имя: {self.name} | "
                f"Отечество: {self.patronymic} | "
                f"Возраст: {self.age}")


class UserList:
    def __init__(self):
        self.users = list()


user = User("Denis", "Tochilov", "Nikolaevich", 34)
user1 = User("Alex", "Smirnov", "Ivanovich", 37)

# выводим на экран
# print(user)

# Первый вариант
users_list = UserList()
users_list.users.append(user)
users_list.users.append(user1)
for u in users_list.users:
    print(u)

# Второй вариант
users_list = UserList().users
users_list.append(user)
users_list.append(user1)

for u in users_list:
    print(u)
