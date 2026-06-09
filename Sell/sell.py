import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from funtionc_close import close
from systemDAO import System
from wCart.car import Cart
from wCart.system_cart import SystemCart


class Sell:
    total = 0

    def total_cart(cls):
        products = SystemCart().select()
        for product in products:
            success = System().decrement(product)
            if not success:
                print(f"Failed to update inventory for {product.model}")

        for product in products:
            if product.amoung > 1:
                cls.total += product.price * product.amoung
            else:
                cls.total += product.price

        return f"{cls.total:.2f}"

    def create_check(self, name, ci, numberph):

        checks = []
        products = SystemCart().select()
        for product in products:
            checks.append(
                [
                    {product.model},
                    {product.price},
                    {product.amoung},
                    {product.amoung * product.price},
                ]
            )

        file = f"{name}.docx"
        with open(file, "w") as FILE:
            FILE.write(f"Name:{name}      C.I:{ci}      Number Phone:{numberph}\n")
            FILE.write(
                "_______________________________________________________________________________\n"
            )

            for product in checks:
                FILE.write(
                    f"{product[0]}...............{product[1]}...............{product[2]}...............{product[3]}\n"
                )
            FILE.write(
                f"Total...............................................................................{self.total_cart()}"
            )
        FILE.close
        close.CloseStore().products_cart()
        Cart().delete_cart()


if __name__ == "__main__":
    Sell().create_check("Francisco Barazarte", "32495769", "11111111111")
    print(Sell().total_cart())
