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