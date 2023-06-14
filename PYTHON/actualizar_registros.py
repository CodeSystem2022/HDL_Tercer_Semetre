import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database='test_basedatos',
)
try:
     with conexion:
         with conexion.cursor() as cursor:
             sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona= %s'
             valores =('Alexis Emanuel', 'Romero', 'aromero@gmail.com', 1) # Es un tupla de tuplas
             cursor.execute(sentencia, valores) # De esta manera ejecutamos la sentencia
             registros_actualizados = cursor.rowcount
             print(f'Los registros actualizados son :{registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un errror :{e}')
finally:
    conexion.close()