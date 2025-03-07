import sqlite3
import bcrypt


class sing_up:
    def __init__(self, name,
            last_name,
            email,
            birth_date,
            phone_num,
            password ):
        self.BD = "BaseDeDatos" # Nombre de BD
        self.conexión = sqlite3.connect(self.BD) # Se conecta con la BD
        self.cursorBD = self.conexión.cursor() # Establece el cursor
        self.Tabla = "REGISTRE_USERS" # Tabla de Usuarios
        self.tablaExiste(self.Tabla) # Chequea si la tabla exista en caso de que no se creá 

        self.password_hash = self.hashed_password(password)

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

    def hashed_password(self, password):
        self.haspass =bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        print("Contraseña hasheada: ", self.haspass)
    def check_password(self, password):
        self.status_paswword = bcrypt.checkpw(password.encode(), self.haspass)


        print("Estado de contraseña : ", self.status_paswword)
prueba = sing_up("Yhoan Smith", "Mosquera Peñaloza", 
                 "Jhoanpa57@gmail.com",
                 "27/20/2000", 3128628658,
                 "Jhosmope27") 
