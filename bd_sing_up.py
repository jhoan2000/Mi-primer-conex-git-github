import sqlite3



class sing_up:
    def __init__(self, name,
            last_name,
            email,
            birth_date,
            phone_num,
            password_hash ):
        self.BD = "BaseDeDatos" # Nombre de BD
        self.conexión = sqlite3.connect(self.BD) # Se conecta con la BD
        self.cursorBD = self.conexión.cursor() # Establece el cursor
        self.Tabla = "REGISTRE_USERS" # Tabla de Usuarios
        self.tablaExiste(self.Tabla) # Chequea si la tabla exista en caso de que no se creá 

    def tablaExiste(self, nombreTabla):
        # ---Chequea si existe un objeto tipo TABLA con el nombre predeterminado
        self.cursorBD.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name ='{}' '''.format(nombreTabla))
        if self.cursorBD.fetchone()[0] == 1:
            return True
        # --- Si no existe lo crea
        else:
            self.cursorBD.execute(''' CREATE TABLE '{}' (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            last_name TEXT NOT NULL,
                            email TEXT UNIQUE NOT NULL,
                            birth_date DATE NOT NULL,
                            phone_num INT UNIQUE NOT NULL,
                            password_hash TEXT NOT NULL
                            ) '''.format(nombreTabla))
            return False

    