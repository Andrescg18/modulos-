import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="gestion_cosecha",
    user="postgres",
    password="1234",
    port="5432"
)