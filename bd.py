import sqlite3

conexión = sqlite3.connect("BaseDeDatos")
cursorBD = conexión.cursor()

def tableExiste(nombreTabla):
    cursorBD.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name ='{}' '''.format(nombreTabla))
    if cursorBD.fetchone()[0] == 1:
        return True
    else:
        cursorBD.execute(''' CREATE TABLE '{}' (id INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, PRECIO REAL) '''.format(nombreTabla))
        return False
Tabla = "PRODUCTO"   
tableExiste(Tabla)

#c CREATE INSERT
def insertarProducto(Tabla, nombre, precio):
    cursorBD.execute('''INSERT INTO '{}' (NOMBRE, PRECIO) VALUES ('{}','{}')'''.format(Tabla, nombre, precio))
    conexión.commit()
    
# insertarProducto(Tabla, "Personal 300 cc", 11000)
# insertarProducto(Tabla, "7L und ", 5500)
# insertarProducto(Tabla, "7L x> cc", 4000)

def selccionarProductos(Tabla):
    cursorBD.execute(''' SELECT * FROM '{}' '''.format(Tabla))
    lista = []
    for filaEncontrada in cursorBD.fetchall():
        lista.append(filaEncontrada)
    return lista

print(selccionarProductos(Tabla))