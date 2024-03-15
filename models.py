
class RobotDelivery:
    id: int
    # speed: float
    is_free: bool #свободен
    is_full: bool #заполнен
    #
    route: list
    # текущие коорд
    currentX: int
    currentY: int
    # коорд доставки
    targetX: int
    targetY: int
    estimated_delivery_time: int #пока инт
    
    def __init__(self):
        self.currentX, self.currentY = 0, 0


# Заказ, будет зависима от робота
class Order:
    ...  

# Все продукты
class Products:
    ...