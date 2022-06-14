import sqlite3
from bbdd import run_query,conexionBBDD

class RegistroImc:
    def __init__(self):
        self.main()

    def ingresar_dato(self):
        nombre = input('Ingrese el nombre: ')
        altura = float(input('Ingrese la altura: '))
        peso = float(input('Ingrese el peso: '))
        imc = round(peso/(altura*altura),2)
        query = "INSERT INTO talle (nombre,altura,peso,IMC) VALUES (?,?,?,?)"
        parameters = (nombre,altura,peso,imc)
        print("Datos ingresados")
        run_query(query, parameters)
    
    
    def eliminar_dato(self):
        id_eliminar = int(input("Ingrese id de campo que desea elminar: "))
        query = f'DELETE FROM talle WHERE ID = {id_eliminar}'
        run_query(query)
    
    
    def actulizar_dato(self):
        id_actualizar = int(input("Ingrese el ID que desea actualizar: "))
        n_nombre = input('Ingrese el nombre: ')
        n_altura = float(input('Ingrese la altura: '))
        n_peso = int(input('Ingrese el peso: '))
        imc2 = round(n_peso/(n_altura*n_altura),2)
        query = f"UPDATE talle SET nombre = ?,altura = ?,peso = ?,imc = ? WHERE ID = {id_actualizar}"
        parameters = (n_nombre,n_altura,n_peso,imc2)
        run_query(query,parameters)
    
    
    def mostrar_dato(self):
        query_nombre = input("Ingrese el nombre que desea: ")
        query = f"SELECT * FROM talle WHERE nombre LIKE '%{query_nombre}%'"
        rows_query = run_query(query)
        for row in rows_query:
            print(row)
    
    
    def mostrar_todos(self):
        query = "SELECT * FROM talle"
        rows_query = run_query(query)
        print("+-------------------------------------+")
        print("ID  NOMBRE          ALTURA PESO IMC")
        print("+-------------------------------------+")
        for row in rows_query:
            string = "|{:<3}|{:<15}|{:<5}|{:<5}|{:<4}|".format(row[0],row[1],row[2],row[3],row[4])
            print(string)
            print('-'*39)
    
    
    def menu(self):
        print("""\nSelecciones una acción:\n
              1 MOSTRAR MENU
              2 INGRESAR UNA DATO
              3 ACTUALUZAR UN DATO
              4 ELIMINAR UN DATO
              5 MOSTRAR UN REGISTRO 
              6 MOSTRAR TODOS LOS REGISTROS
              7 SALIR
              """)
    def main(self):
        self.menu()
        while True:
            opcion = int(input("Ingrese una opción: "))
            list_op = [1,2,3,4,5,6,7]
            if opcion in list_op:
                if opcion == 1:
                    self.menu()
                if opcion == 2:
                    self.ingresar_dato()
                if opcion == 3:
                    self.actulizar_dato()
                if opcion == 4:
                    self.eliminar_dato()
                if opcion == 5:
                    self.mostrar_dato()
                if opcion == 6:
                    self.mostrar_todos()
                if opcion == 7:
                    print("Programa finalizado")
                    break
            else:
                print("elija una opción del 1 al 8")
                opcion = int(input("Ingrese una opción: "))

if __name__ == '__main__':
    RegistroImc()
