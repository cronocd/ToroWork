from mysql.connector import pooling
from mysql.connector import Error

class Connection:

    DB_NAME = 'Cart_toro'
    POOL_USER = 'crono'
    POOL_PASSWORD = 'Yoli.27'
    POOL_HOST = 'localhost'
    POOL_PORT = '3306'
    POOL_NAME = 'cart'
    POOL_SIZE = 10
    pool = None

    @classmethod
    def connect_pool(cls):

        if cls.pool == None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.POOL_NAME,
                    pool_size= cls.POOL_SIZE,
                    host = cls.POOL_HOST,
                    port= cls.POOL_PORT,
                    user = cls.POOL_USER,
                    password = cls.POOL_PASSWORD,
                    database = cls.DB_NAME   
                )
                return cls.pool
            except Error as e:
                print(f'Meanwhile we\'re trying connect to server ocurrer an error: {e} ')
        else:
            return cls.pool
            
    @classmethod
    def connection(cls):
        return cls.connect_pool().get_connection()
    
    @classmethod
    def PlugoutConnection(cls, connection):
        connection.close()


if __name__ == '__main__':
    pool_user = Connection()

    user = pool_user.connection()

    print(user)

    pool_user.PlugoutConnection(user)