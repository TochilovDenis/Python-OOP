import time
from random import randint

FLOOR = {0: "Нулевой",
         1: "Первый",
         2: "Второй",
         3: "Третий",
         4: "Четвертый",
         5: "Пятый",
         6: "Шестой",
         7: "Седьмой",
         8: "Восьмой",
         9: "Девятый"}

class Lift:
    def __init__(self, star_floor, end_floor, second=2) -> None:
        self.star_floor = star_floor
        self.end_floor = end_floor
        self.second = second

    def move(self) -> None:
        if self.star_floor < self.end_floor:
            for i in range(self.star_floor, self.end_floor):
                print(f"{FLOOR[i]} этаж")
                time.sleep(self.second)
            print(f"{FLOOR[self.end_floor]} этаж. Мы приехали")
        else:
            for i in reversed(range(self.end_floor + 1, self.star_floor + 1)):
                print(f"{FLOOR[i]} этаж")
                time.sleep(self.second)
            print(f"{FLOOR[self.end_floor]} этаж. Мы приехали.")


def process_lift() -> None:
    while True:
        try:
            min_floor = 0
            max_floor = 9
            now = randint(min_floor, max_floor)
            print(f"Сейчас лифт находится {FLOOR[now].lower()} этаж")
            start = int(input("Выбрать назначение этаж: "))
            end = int(input("На какой этаж отправить? №  "))

            if now == start:
                if max(start, end) > max_floor:
                    print(f"Нет такого номера этажа! Введите число от {min_floor} до {max_floor}.")
                elif start == end:
                    print("Вы выбрали один и тот же этаж. Ничего не происходит.")
                lift = Lift(start, end)
                lift.move()
            elif now > start:
                if max(start, end) > max_floor:
                    print(f"Нет такого номера этажа! Введите число от {min_floor} до {max_floor}.")
                lift = Lift(now, end)
                lift.move()

        except ValueError:
            print("Программа завершена")
            exit()



if __name__ == '__main__':
    try:
        process_lift()
    except KeyboardInterrupt:
        print("\nExit")

