from random import randint


class Apartment:
    def __init__(self, number_of_occupants, number_of_rooms, floor_number, apartment_number):
        self.numberOfOccupants = number_of_occupants # количество жильцов
        self.numberOfRooms = number_of_rooms # количество комнат
        self.floorNumber = floor_number # номер этажа
        self.apartmentNumber = apartment_number # номер квартиры


    def __str__(self):
        return f"Квартира №{self.apartmentNumber} на {self.floorNumber} этаже, {self.numberOfOccupants} жильцов"

    def __len__(self):
        return len(self.numberOfOccupants)

def get_random_apartment():
    return Apartment(randint(1, 5), randint(1,4), randint(1,9), randint(1, 36))

apartment = [get_random_apartment() for _ in range(10)]
for ap in apartment:
    print(ap)


class House:
    def __init__(self, house_number, number_of_floors, number_of_entrances):
        self.list_of_apartments = [] # список квартир
        self.house_number = house_number # номер дома
        self.number_of_floors = number_of_floors # количество этажей
        self.number_of_entrances = number_of_entrances # количество подъездов

    def __len__(self) -> int:
        return len(self.list_of_apartments)

    def __str__(self) -> str:
        return (f"Дом №{self.house_number} |"
                f" {self.number_of_entrances} подъезда |"
                f" {self.number_of_floors} этажей |"
                f" {self.list_of_apartments} квартир")

    def add_apartment(self, a: Apartment):
        self.list_of_apartments.append(a)


    def print_all_apartment(self) -> None:
        for a in self.list_of_apartments:
            print(a)


def get_random_house(amount_of_random_apartments: int = 0) -> House:
    house: House = House(str(randint(1, 100)), randint(1, 9), randint(1, 10))

    for _ in range(amount_of_random_apartments):
        house.add_apartment(get_random_apartment())

    return house
