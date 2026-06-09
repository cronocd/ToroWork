# Motor Cycle App

Aplicación de escritorio en Python para la gestión de inventario y ventas de motocicletas.

## Descripción general

Este proyecto utiliza `tkinter` como interfaz gráfica y `mysql-connector-python` para acceder a bases de datos MySQL.

- `signin.py`: Ventana de inicio de sesión para acceder a la aplicación.
- `GUI/Toro_interface.py`: Interfaz principal de inventario donde se pueden ver, agregar, actualizar y eliminar registros de motocicletas.
- `GUI/Sell_windows.py`: Ventana secundaria para procesar ventas y realizar operaciones relacionadas con el carrito de compra.
- `systemDAO.py`: Lógica de acceso a datos para la tabla principal `amoung_toro`.
- `connection.py`: Conexión con MySQL para la base de datos principal `count_toro`.
- `wCart/connection_db_car.py`: Conexión con MySQL para la base de datos secundaria `Cart_toro`.
- `wCart/system_cart.py`: DAO para la tabla `cart` usada por el carrito de compras.
- `wCart/car.py`: Clase de fachada para agregar y eliminar productos del carrito.
- `motor_cycle.py`: Modelo de datos para representar una motocicleta.
- `funtionc_close/close.py`: Genera un registro de cierre de tienda y calcula totales del carrito.

## Estructura de carpetas

- `/GUI`
  - `Toro_interface.py`: Interfaz principal de inventario.
  - `Sell_windows.py`: Ventana de ventas y carrito.
- `/wCart`
  - `car.py`: Clase `Cart` para manejar el carrito.
  - `connection_db_car.py`: Conexión a la base de datos del carrito.
  - `system_cart.py`: Acceso a datos para la tabla `cart`.
- `/funtionc_close`
  - `close.py`: Funciones para cerrar la tienda y escribir archivos de cierre.
- `/logo`
  - Imagen `torott.png` que usa la interfaz de inicio de sesión.

## Archivos principales

- `connection.py`
  - Define `Connection` para la base de datos principal `count_toro`.
  - Usa `mysql.connector.pooling.MySQLConnectionPool`.
  - Proporciona métodos `connect_pool()`, `connection()` y `PlugoutConnection(connection)`.

- `motor_cycle.py`
  - Define la clase `Motor_cycle` con atributos `model`, `amoung` y `price`.
  - Se utiliza como DTO/entidad para transportar datos entre la UI y la capa DAO.

- `systemDAO.py`
  - Define operaciones CRUD para la tabla `amoung_toro`:
    - `select()`
    - `insert(motor)`
    - `update(motor)`
    - `decrement(motor)`
    - `delete(motor)`
  - Convierte cada registro SQL en una instancia de `Motor_cycle`.

- `signin.py`
  - Inicia sesión con credenciales fijas: `admin` / `12345678`.
  - Si el acceso es correcto, arranca la ventana principal `Windows()` desde `GUI/Toro_interface.py`.

- `GUI/Toro_interface.py`
  - Interfaz de inventario con ventana `Windows`.
  - Permite cargar datos desde MySQL, mostrar tabla de productos y manejar botones:
    - Guardar
    - Eliminar
    - Limpiar campos
    - Vender
    - Cerrar
  - Envía correo automático cuando un producto tiene stock bajo (<20 unidades).

- `GUI/Sell_windows.py`
  - Ventana de ventas con formulario para nombre, C.I. y teléfono.
  - Permite seleccionar productos del inventario y agregarlos al carrito.
  - Usa `Sell.sell.Sell` para crear un comprobante de venta.

- `funtionc_close/close.py`
  - Genera o actualiza un archivo de cierre en `/home/crono/Desktop/Coding/BreakDown`.
  - Registra productos del carrito y el total de venta.

## Dependencias

El proyecto usa las siguientes librerías principales:

- `mysql-connector-python` (conexión a MySQL)
- `tkinter` (interfaz gráfica, ya viene con Python estándar)
- `smtplib` y `email.message` (envío de correo, estándar de Python)

## Requisitos previos

- Python 3.13 (o similar)
- MySQL funcionando en `localhost:3306`
- Bases de datos y tablas necesarias:
  - Base de datos `count_toro` con tabla `amoung_toro(model, amoung, price)`
  - Base de datos `Cart_toro` con tabla `cart(model, amoung, price)`

## Instalación de dependencias

Si usas el entorno virtual incluido en `env`, actívalo:

```bash
source env/bin/activate
```

Luego instala la dependencia de MySQL:

```bash
pip install mysql-connector-python
```

> Nota: `tkinter` ya está incluido en la instalación estándar de Python, pero en algunas distribuciones puede requerir un paquete adicional del sistema.

## Ejecución

Para iniciar la app desde la raíz del proyecto:

```bash
python signin.py
```

### Flujo de uso

1. Ejecutar `signin.py`.
2. Iniciar sesión con:
   - Usuario: `admin`
   - Contraseña: `12345678`
3. En la ventana principal se maneja inventario y productos.
4. El botón `Sell` abre la ventana de ventas.
5. El botón `Close` escribe el cierre de tienda y cierra la app.

## Funcionalidad por componente

### `connection.py`
- Pool de conexiones para la base de datos principal.
- Tabla objetivo: `amoung_toro`.

### `wCart/connection_db_car.py`
- Pool de conexiones para la base de datos del carrito.
- Tabla objetivo: `cart`.

### `systemDAO.py`
- DAO de inventario general.
- Lee, crea, actualiza, decrementa y borra motocicletas.

### `wCart/system_cart.py`
- DAO para el carrito de compra.
- Inserta artículos en la tabla `cart` y limpia el carrito.

### `GUI/Toro_interface.py`
- Ventana principal del sistema.
- Carga inventario y permite operaciones de mantenimiento.
- Envía correo cuando hay stock bajo.

### `GUI/Sell_windows.py`
- Ventana para ventas con formulario y tabla de inventario.
- Controla selección de producto y validación de datos.

### `funtionc_close/close.py`
- Crea registro de cierre de tienda en archivo de texto.
- Calcula totales del carrito.

## Notas importantes

- Los archivos `.docx` en la raíz parecen ser comprobantes de ventas generados manualmente.
- La imagen `logo/torott.png` se usa en `signin.py` para el logo de la pantalla de login.
- El proyecto no incluye `requirements.txt` ni scripts de instalación automatizados.
- Hay credenciales y rutas codificadas en Python, lo cual puede requerir ajustes antes de producción.

## Orden recomendado de archivos

1. `signin.py`  
2. `GUI/Toro_interface.py`  
3. `GUI/Sell_windows.py`  
4. `systemDAO.py`  
5. `connection.py`  
6. `wCart/connection_db_car.py`  
7. `wCart/system_cart.py`  
8. `wCart/car.py`  
9. `motor_cycle.py`  
10. `funtionc_close/close.py`

## Mejoras sugeridas

- Añadir un `requirements.txt` con dependencias.
- Mover las credenciales de MySQL a variables de entorno.
- Corregir el setter de `price` en `motor_cycle.py` para que no sobrescriba `model`.
- Añadir manejo de errores más detallado en la interfaz.
- Añadir documentación de las tablas SQL requeridas.
