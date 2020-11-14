import socket
from cifrado import *
import os
import time
import pickle
import sqlite3

# Creando base de datos SQLite
conn = sqlite3.connect('Hash.sqlite')
cur = conn.cursor()

# Se crea la tabla 'hash', si esta creada se elimina y se crea de nuevo
try:
    cur.execute('CREATE TABLE hash (hash VARCHAR)')
    
    conn.commit()
except:
    print('La tabla ya existe, se reestablecera.')
    cur.execute('DROP TABLE hash')
    cur.execute('CREATE TABLE hash (hash VARCHAR)')

# Largo de los numeros primos usados para genrar las laves
prime = 1200

if (len(sys.argv)>1):
    m=str(sys.argv[1])
if (len(sys.argv)>2):
    prime=int(sys.argv[2])

# Se generan las llaves publicas y privadas
n,g,h,p,q=gen_key(prime) 


print("==Public key====")
print("n=",n)
print("g=",g)
print("h=",h)
print("==Private key (%d-bit prime)===" %prime)
print("p=",p)
print("q=",q)

# Se inicializa socket
sckt = socket.socket()
# Se asocia la direccion y puerto
sckt.bind(('localhost',8000))
# Permite la entrada de 1 cliente a la vez
sckt.listen(1)

while True:
    T_incial = time.time()
    # Acepta al cliente
    conexion, adress = sckt.accept()
    print("nueva conexion establecida")
    print(conexion)
    # Envía las tres llaves publicas
    conexion.send(str(n).encode('ascii'))
    time.sleep(1)
    conexion.send(str(g).encode('ascii'))
    time.sleep(1)
    conexion.send(str(h).encode('ascii'))
    # Crea el arreglo donde se guardará lo recibido por cliente
    array = []
    data = ''
    while True:
        # Se recibe un mensaje
        data = conexion.recv(2042)
        # Se extrae el largo del mensaje recibido
        data_len = int(data[:10])
        # Se verifica que el largo de el mensaje coincida con el valor enviado en el encabezado
        if len(data) - 10 == data_len:
            # Se verifica si es el mensaje de término, si lo es se sale del loop for
            if str(pickle.loads(data[10:])) == 'end':
                break
            # Se agrega el mensaje cifrado a el arreglo, sin el encabezado
            array.append(str(pickle.loads(data[10:])))

    # Se recorre el arreglo
    for line in range(len(array)):

        cipher_str = array[line]
        # El cifrado se transforma a entero
        cipher = int(cipher_str)
        # Se descifra con una de las llaves públicas y una de las privadas
        hash_bytes = decrypt(cipher, p, g)
        # Se decodifican y se corta trunca a un tamaño de 128, tamaño del output del algoritmo hash
        hash = hash_bytes.decode('utf-8','ignore')[:128]
        # Se inserta a la base de datos
        cur.execute('INSERT INTO hash (hash) values (?)', [str(hash)])
        conn.commit()

    # Se termina la conexión con la base de datos
    conn.close()

    print('Terminó el proceso')
    # Se termina la conexión con el cliente
    T_final = time.time()
    conexion.close()
    
    T_conn = T_final - T_incial
    print("Tiempo de conexion: " + str(T_conn) )

sckt.close()
