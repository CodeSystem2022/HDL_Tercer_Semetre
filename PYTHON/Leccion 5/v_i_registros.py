import psycopg2 # Esto es para poder conectarnos a Postgre

conexion = psycopg2.connect(user = 'postgres', password = 'admin', host = '127.0.0.1', port = '5432', database='test_basedatos',
)
try:
     with conexion:
         with conexion.cursor() as cursor:
             sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, %s, %s)'
             valores =(
                 ('Carlos', 'Soto', 'csoto@mail.com'),
                ('Marcos', 'Solis', 'msolis@mail.com'),
                ('Marcelo', 'Casco', 'mcasco@mail.com')

             ) # Es un tupla de tuplas
             cursor.executemany(sentencia, valores) # De esta manera ejecutamos la sentencia
             #conexion.commit() # esto se utiliza para guardar los cambios en base de datos
             registros_insertados = cursor.rowcount
             print(f'Los registros insertados son :{registros_insertados}')

except Exception as e:
    print(f'Ocurrio un errror :{e}')
finally:
    conexion.close()