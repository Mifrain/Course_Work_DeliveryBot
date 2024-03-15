from models import RobotDelivery

from map import find_route
from order import create_order         
        


if __name__ == "__main__":
    bot1 = RobotDelivery()
    
    create_order(bot1)
    find_route(bot1)