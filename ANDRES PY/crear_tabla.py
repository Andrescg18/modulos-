from conexion import conn

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS andres (
        id SERIAL PRIMARY KEY,
        fecha TIMESTAMP DEFAULT NOW(),
        cosecha_inicio INT NOT NULL,
        cosecha_final INT NOT NULL,
        estado VARCHAR(50)
    );
""")

conn.commit()
cursor.close()
conn.close()

print("✅ Tabla 'andres' creada correctamente o ya existe.")
