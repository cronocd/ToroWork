import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from wCart.system_cart import SystemCart
from motor_cycle import Motor_cycle

class Cart:
    

    def add_cart(self, motor):
        SystemCart().insert(motor)

    @classmethod
    def delete_cart(cls):
        SystemCart.clear_cart()


if __name__ == '__main__':

    user = Cart()
    product = Motor_cycle(model='htl-422', amoung=1, price=999.9)
    buy = user.add_cart(product)
    product = Motor_cycle(model='yama-345', amoung=1, price=1222)
    buy = user.add_cart(product)

    #chacerman = user.total_cart()

    #Schacerman = Cart.delete_cart()