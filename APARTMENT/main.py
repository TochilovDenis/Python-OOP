from house import get_random_house, House

if __name__ == '__main__':
    # apartment = [get_random_apartment() for _ in range(10)]
    # for ap in apartment:
    #     print(ap)

    houses: list[House] = [get_random_house() for _ in range(3)]
    for house in houses:
        print(house)