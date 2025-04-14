import sqlite3

conn = sqlite3.connect("mi_base_de_datos.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL
    );
''')

# Insertar datos de prueba
cursor.execute("INSERT INTO usuarios (nombre, correo) VALUES (?, ?)", ("Juan", "juan@correo.com"))
conn.commit()

# Leer la tabla
cursor.execute("SELECT * FROM usuarios;")
for fila in cursor.fetchall():
    print(fila)

conn.close()
