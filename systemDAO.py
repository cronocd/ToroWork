from connection import Connection
from motor_cycle import Motor_cycle

class System:
    
    SELECT = 'SELECT * FROM amoung_toro'
    INSERT = 'INSERT INTO amoung_toro(model, amoung, price) value(%s, %s, %s)'
    UPDATE = 'UPDATE amoung_toro SET amoung = %s, price = %s WHERE model = %s'
    DECREMENT = 'UPDATE amoung_toro SET amoung = amoung - %s WHERE model = %s'
    DELETE = 'DELETE FROM amoung_toro WHERE model = %s '

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

    def update(self,motor):
        connection = None
        try:
            connection = Connection().connection()
            cursor = connection.cursor()
            values = (motor.amoung, motor.price, motor.model)
            cursor.execute(self.UPDATE,values)
            connection.commit()
        except Exception as e:
            print(f'Ocurrer an error while we\'re trying to update a motor cycle: {e}')
        finally:
            cursor.close()
            Connection.PlugoutConnection(connection)

    def decrement(self, motor):
        connection = None
        try:
            connection = Connection().connection()
            cursor = connection.cursor()
            cursor.execute('SELECT amoung FROM amoung_toro WHERE model = %s', (motor.model,))
            record = cursor.fetchone()
            if record is None:
                print(f'Model {motor.model} not found in inventory.')
                return False
            current_amount = record[0]
            if current_amount < motor.amoung:
                print(f'Not enough stock for {motor.model}: current={current_amount}, requested={motor.amoung}')
                return False
            values = (motor.amoung, motor.model)
            cursor.execute(self.DECREMENT, values)
            connection.commit()
            return True
        except Exception as e:
            print(f'Ocurrer an error while we\'re trying to decrement a motor cycle: {e}')
            return False
        finally:
            cursor.close()
            Connection.PlugoutConnection(connection)

    def delete(self,motor):
        connection = None
        try:
            connection = Connection().connection()
            cursor = connection.cursor()
            values = (motor.model,)
            cursor.execute(self.DELETE, values)
            connection.commit()
        except Exception as e:
            print(f'Ocurrer an error while we\'re trying to update a motor cycle: {e}')
        finally:
            cursor.close()
            Connection.PlugoutConnection(connection)



if __name__ == '__main__':
    

    #motor = Motor_cycle(model='rxt-760')
    #Delete = System().delete(motor)

    #motor = Motor_cycle(model='rtg-567', amoung=30, price=560)
    #inserts = System().insert(motor)


    selects = System().select()
    for motor in selects:
       print(motor)

    #I made every test this is ruining well.