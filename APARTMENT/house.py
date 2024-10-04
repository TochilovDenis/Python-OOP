from apartment import Apartment, randint, get_random_apartment
from random import choice

class House:
    def __init__(self, house_number, number_of_floors, number_of_entrances):
        self.list_of_apartments: dict[str, Apartment] = {} # список квартир
        self.house_number = house_number # номер дома
        self.number_of_floors = number_of_floors # количество этажей
        self.number_of_entrances = number_of_entrances # количество подъездов

    def __len__(self) -> int:
        return len(self.list_of_apartments)

    def __str__(self) -> str:
        return (f"Дом №{self.house_number} |"
                f" {self.number_of_entrances} подъезда |"
                f" {self.number_of_floors} этажей |"
                f" {len(self.list_of_apartments)} квартир")

    def add_apartment(self, a: Apartment) -> None:
        self.list_of_apartments[a.apartmentNumber] = a


    def print_all_apartment(self) -> None:
        if self.list_of_apartments:
            for _, ap in self.list_of_apartments.items():
                print(f"{ap}")
        else:
            print("Нет квартир!")

RUSSIAN_LETTERS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'

def get_random_house(amount_of_random_apartments: int = 0) -> House:
    house: House = House(str(randint(1, 100)) + choice(RUSSIAN_LETTERS), randint(1, 9), randint(1, 10))

    for _ in range(amount_of_random_apartments):
        house.add_apartment(get_random_apartment())

    return house



