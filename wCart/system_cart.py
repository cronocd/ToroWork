from .connection_db_car import Connection
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from motor_cycle import Motor_cycle

class SystemCart:
    
    SELECT = 'SELECT * FROM cart'
    INSERT = 'INSERT INTO cart(model, amoung, price) value(%s, %s, %s)'
    CLEAR = 'DELETE FROM cart'

    def select(self):

        connection = None
        try:

            connection = Connection().connection()
            cursor = connection.cursor()
            cursor.execute(self.SELECT)
            records = cursor.fetchall()
            motor_cycles = []
            #I'm gonna map every person I get
            for record in records:
                motor_cycle = Motor_cycle(model=record[0], amoung=record[1], price=record[2])
                motor_cycles.append(motor_cycle)
            return motor_cycles
        except Exception as e:
            print(f'UPS ocurrer a error while we\'re trying show the motorcycles: {e}')
        finally:
            cursor.close()
            Connection.PlugoutConnection(connection)

    def insert(self,motor):
        connection = None
        try:
            connection = Connection().connection()
            cursor = connection.cursor()
            values = (motor.model, motor.amoung, motor.price)
            cursor.execute(self.INSERT, values)
            connection.commit()
        except Exception as e:
            print(f'Ocurrer an error while we\'re trying to add a motor cycle: {e}')
        finally:
            cursor.close()
            Connection.PlugoutConnection(connection)

    @classmethod
    def clear_cart(cls):
        connection = None
        try:
            connection = Connection().connection()
            cursor = connection.cursor()
            cursor.execute(cls.CLEAR)
            connection.commit()
        except Exception as e:
            print(f'Ocurrer an error while we\'re trying to clear the cart: {e}')
        finally:
            cursor.close()
            Connection.PlugoutConnection(connection)



if __name__ == '__main__':
    

    #motor = Motor_cycle(model='rxt-760')
    #Delete = System().delete(motor)

    #motor = Motor_cycle(model='rtg-567', amoung=30, price=560)
    #inserts = System().insert(motor)

    SystemCart().clear_cart()

    #|selects = SystemCart().select()
    #for motor in selects:
    #   print(motor)

    #I made every test this is ruining well.