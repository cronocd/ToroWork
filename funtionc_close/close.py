import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import date
from datetime import datetime
from wCart import system_cart

class CloseStore:
    
    
    FOLDER = '/home/crono/Desktop/Coding/BreakDown'
    FILE = f'/home/crono/Desktop/Coding/BreakDown/sell{date.today()}.txt'
    
    def products_cart(self):
        products_list = []
        products = system_cart.SystemCart().select()
        for product in products:
            products_list.append([product.model, product.amoung, product.price])
        return self.create_finall_count(products_list)

    def create_finall_count(self, products_list):
        now = datetime.now()
        total = 0

        if os.path.exists(self.FOLDER):
            products = products_list
            with open(self.FILE, 'a') as file:
                file.write(f'\nDone: {now.replace(microsecond=0)}\n')
                file.write('Model-----amount\n')
                for product in products:
                    file.write(f'{product[0]}    {product[1]}\n')

                for product in products:
                    if product[2] == 1:
                        prices = product[2]
                        total += prices
                        
                    else:
                        prices = product[2] * product[1]
                        total += prices
                file.write(f'total..............{total}\n')

            file.close()
        else:
            os.makedirs(self.FOLDER)
            products = products_list
            with open(self.FILE, 'a') as file:
                file.write(f'Done: {self.now.replace(microsecond=0)}\n')
                file.write('Model-----amount\n')
                for product in products:
                    file.write(f'{product[0]}    {product[1]}\n')

                for product in products:
                    if product[2] == 1:
                        prices = product[2]
                        total += prices
                        
                    else:
                        prices = product[2] * product[1]
                        total += prices
                file.write(f'total..............{total}\n')


            file.close()

    def close_store(self):
        self.now_close = datetime.now()
        with open(self.FILE,'a') as file:
            file.write(f'\nClose hour: {self.now_close.replace(microsecond=0)}')
        file.close()

if __name__ == '__main__':

    #CloseStore().products_cart()
    CloseStore().close_store()