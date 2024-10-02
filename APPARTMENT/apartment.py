class Apartment:
    def __init__(self, number_of_occupants, number_of_rooms, floor_number, apartment_number):
        self.numberOfOccupants = number_of_occupants # количество жильцов
        self.numberOfRooms =number_of_rooms # количество комнат
        self.floorNumber = floor_number # номер этажа
        self.apartmentNumber = apartment_number # номер квартиры


    def __str__(self):
        return f"Квартира №{self.apartmentNumber} на {self.floorNumber} этаже, {self.numberOfOccupants} жильцов"

    def __len__(self):
        return len(self.numberOfOccupants)
