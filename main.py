import sqlite3
mibase = 'database.db'


def run_query(query, parameters = ()):
        with sqlite3.connect(mibase) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result


def conexionBBDD():
    miConexion = sqlite3.connect('database.db')
    miCursor = miConexion.cursor()

    try: 
        miCursor.execute('''
            CREATE TABLE tipo(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(50),
            altura FLOAT NOT NULL,
            peso INT NOT NULL,
            IMC FLOAT)
            ''')
        print('BASE DE DATOS creada exitosamente')
    except:
        print('Conexión exitosa con la base de datos')


def ingresar_dato():
    nombre = input('Ingrese el nombre: ')
    altura = float(input('Ingrese la altura: '))
    peso = float(input('Ingrese el peso: '))
    imc = peso/(altura*altura)
    query = "INSERT INTO tipo (nombre,altura,peso,IMC) VALUES (?,?,?,?)"
    parameters = (nombre,altura,peso,imc)
    print("Datos ingresados")
    run_query(query, parameters)


def eliminar_dato():
    id_eliminar = int(input("Ingrese id de campo que desea elminar: "))
    query = f'DELETE FROM tipo WHERE ID = {id_eliminar}'
    run_query(query)


def actulizar_dato():
    id_actualizar = int(input("Ingrese el dato que desea actualizar: "))
    n_nombre = input('Ingrese el nombre: ')
    n_altura = float(input('Ingrese la altura: '))
    n_peso = int(input('Ingrese el peso: '))
    imc2 = n_peso/(n_altura*n_altura)
    query = f"UPDATE tipo SET nombre = ?,altura = ?,peso = ?,imc = ? WHERE ID = {id_actualizar}"
    parameters = (n_nombre,n_altura,n_peso,imc2)
    run_query(query,parameters)


def mostrar_dato():
    query_nombre = input("Ingrese el nombre que desea: ")
    query = f"SELECT * FROM tipo WHERE nombre LIKE '%{query_nombre}%'"
    rows_query = run_query(query)
    for row in rows_query:
        print(row)


def mostrar_todos():
    query = "SELECT * FROM tipo"
    rows_query = run_query(query)
    for row in rows_query:
        print(row[0],row[1],row[2],row[3],round(row[4],2))


def comparacion():
    id_comparar = int(input("Ingrese la ID a comparar: "))
    query = f"SELECT * FROM tipo WHERE ID = {id_comparar}"
    rows_query = run_query(query)
    dws = 1.80
    for row in rows_query:
        if row[2] > dws:
            print("La diferencia es: ",(round((row[2] - dws),2))*100," centíemtros")
        else:
            print("La diferencia es de: ",(round((dws - row[2]),2))*100," centíemtros")


def menu():
    print("""\nSelecciones una acción:\n
          1 MOSTRAR MENU
          2 INGRESAR UNA DATO
          3 ACTUALUZAR UN DATO
          4 ELIMINAR UN DATO
          5 MOSTRAR UN REGISTRO 
          6 MOSTRAR TODOS LOS REGISTROS
          7 COMPARAR
          8 SALIR
          """)
      
if __name__ == '__main__':
    conexionBBDD()
    while True:
        opcion = int(input("Ingrese una opción: "))
        list_op = [1,2,3,4,5,6,7,8]
        if opcion in list_op:
            if opcion == 1:
                menu()
            if opcion == 2:
                ingresar_dato()
            if opcion == 3:
                actulizar_dato()
            if opcion == 4:
                eliminar_dato()
            if opcion == 5:
                mostrar_dato()
            if opcion == 6:
                mostrar_todos()
            if opcion ==7:
                comparacion()
            if opcion ==8:
                print("Programa finalizado")
                break
        else:
            print("elija una opción del 1 al 8")
            opcion = int(input("Ingrese una opción: "))

