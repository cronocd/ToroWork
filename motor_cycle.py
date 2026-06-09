class Motor_cycle:

    def __init__(self, model = '', amoung = 0, price = 0.0):
        self._model = model
        self._amoung = amoung
        self._price = price
   
    def __str__(self):
        return f'{self._model} {self._amoung} {self._price}'

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self,model):
        self._model = model

    @property
    def amoung(self):
        return self._amoung
    @amoung.setter
    def amoung(self,amoung):
        self._amoung = amoung    

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,price):
        self._model = price

if __name__ == '__main__':
    motor_cycle1 = Motor_cycle('rtx-760', 10, 200)
    print(motor_cycle1)

