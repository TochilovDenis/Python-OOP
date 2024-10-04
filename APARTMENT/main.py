from random import randint
from house import get_random_house, House

if __name__ == '__main__':
    # apartment = [get_random_apartment() for _ in range(10)]
    # for ap in apartment:
    #     print(ap)

    houses: list[House] = [get_random_house(randint(5, 15)) for _ in range(3)]
    for i, house in enumerate(houses, 1):
        print(f"\nHouse {i}:")
        print(house)
        house.print_all_apartment()