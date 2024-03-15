from models import RobotDelivery
from map import *


def create_order(bot: RobotDelivery):
    # Ввод адресса
    print("""Введите через пробел Y и X поля доставки робота
Для корректной работы воспользуйтесь виртуальной картой по ссылке
https://miro.com/welcomeonboard/eG9MVm53TUJYQjRtOTNkSEhnamRWM2RCYVBDUklUckVMN3k3OUdsb2hQVjdJcEhpSmY1NjVJUnc0S3V4OHJZVXwzNDU4NzY0NTM2MDUzNzg0NTg4fDI=?share_link_id=306437873724""")

    target = [int(i) - 1 for i in input().split()]

    while(target[0] > 9 or target[1] > 9 or target[0] < 0 or target[1] < 0 or maps[target[0]][target[1]] != 2):
        print("Введите корректные X и Y согласно виртуальной карте")
        if (maps[target[0]][target[1]] != 2):
            print("Данные координаты не имеют возможности доставки")
        target = [int(i) - 1 for i in input().split()]
    bot.targetX, bot.targetY = target[1], target[0]

    # Ввод товара
    print("Выберите номер товара доступного для заказа\n1 - Кола\n2 - Чипсы\n3 - Хлеб\n4 - Вода\n5 - Колбаса")
    eat = int(input())
    while(eat <= 0 or eat >= 5):
        print("Введите корретный номер!")
        eat = int(input())
        