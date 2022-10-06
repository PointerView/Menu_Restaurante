import sqlite3
from os import system

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

def crear_bd():

    try:
        cursor.execute("""CREATE TABLE categoria (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) UNIQUE NOT NULL)
        """)

        cursor.execute("""CREATE TABLE platos (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(100) UNIQUE NOT NULL, categoria_id INTEGER NOT NULL,
        FOREIGN KEY(categoria_id) REFERENCES categoria(id))""")

    except sqlite3.OperationalError:
        system("cls")
        print("Las tablas ya estan creadas")
    else:
        system("cls")
        print("Las tablas se crearon correctamente")

    conexion.close()



def agregar_categoria():

    categoria = input("Nueva categoria para agregar: ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoria '{}' ya existe".format(categoria))
    else:
        system("cls")
        print("La categoria '{}' se agregó correctamente.".format(categoria))

    conexion.commit()
    conexion.close()


def agregar_plato():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Seleccione una categoria para añadir un plato.\n")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato_usuario = input("Nombre del nuevo plato\n>")

    try:
        cursor.execute("INSERT INTO platos VALUES (null, '{}', {})".format(plato_usuario, categoria_usuario))
    except sqlite3.IntegrityError:
        print("El plato '{}' ya existe".format(plato_usuario))
    else:
        system("cls")
        print("La categoria '{}' se agregó correctamente.".format(plato_usuario))

    conexion.commit()
    conexion.close()


def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1]+":")
        platos = cursor.execute("SELECT * FROM platos WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("\t{}".format(plato[1]))
        print()

    input("Pulse una tecla para continuar...")
    system("cls")
    conexion.close()



def opciones():

    while True:
        print("+-----------------------------+")
        print("|    BIENVENIDO AL SISTEMA    |")
        print("+-----------------------------+")

        opt = int(input("\n1. Agregar una Categoria.\n2. Agregar un Plato\n3. Mostrar lista de Platos\n4. Salir del programa\n\n> "))
        if opt == 1:
            agregar_categoria()
        elif opt == 2:
            agregar_plato()
        elif opt == 3:
            mostrar_menu()
        elif opt == 4:
            system("cls")
            print("Nos Vemos!!")
            break
        else:
            system("cls")
            print("Opcion incorrecta")


crear_bd()
opciones()




conexion.close()