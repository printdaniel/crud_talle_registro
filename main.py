import sqlite3
mibase = 'database.db'
from bbdd import run_query,conexionBBDD


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



def menu():
    print("""\nSelecciones una acción:\n
          1 MOSTRAR MENU
          2 INGRESAR UNA DATO
          3 ACTUALUZAR UN DATO
          4 ELIMINAR UN DATO
          5 MOSTRAR UN REGISTRO 
          6 MOSTRAR TODOS LOS REGISTROS
          7 SALIR
          """)
      
if __name__ == '__main__':
    conexionBBDD()
    while True:
        opcion = int(input("Ingrese una opción: "))
        list_op = [1,2,3,4,5,6,7]
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
            if opcion == 7:
                print("Programa finalizado")
                break
        else:
            print("elija una opción del 1 al 8")
            opcion = int(input("Ingrese una opción: "))

