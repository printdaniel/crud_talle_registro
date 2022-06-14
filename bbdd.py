import sqlite3
MI_BASE = 'database.db'

def run_query(query, parameters = ()):
        with sqlite3.connect(MI_BASE) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result


def conexionBBDD():
    miConexion = sqlite3.connect(MI_BASE)
    miCursor = miConexion.cursor()
    try: 
        miCursor.execute('''
            CREATE TABLE talle(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(50),
            altura FLOAT NOT NULL,
            peso INT NOT NULL,
            IMC FLOAT)
            ''')
        print('BASE DE DATOS creada exitosamente')
    except:
        print('Conexión exitosa con la base de datos')

conexionBBDD()

