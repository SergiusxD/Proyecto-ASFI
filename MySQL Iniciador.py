import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hels1962*"
)

mycursor = mydb.cursor()

# eliminar la base de datos "Datos" si existe
mycursor.execute("DROP DATABASE IF EXISTS Datos")

# crear la base de datos "Datos"
mycursor.execute("CREATE DATABASE Datos")

# conectar a la base de datos "Datos"
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Hels1962*",
  database="Datos"
)

mycursor = mydb.cursor()

# crear la tabla "estados_financieros" si no existe
mycursor.execute("CREATE TABLE IF NOT EXISTS estados_financieros (id INT AUTO_INCREMENT PRIMARY KEY, Fecha DATE, `Tipo de Institucion` VARCHAR(255), `Institución` VARCHAR(255), `Dimension 1` VARCHAR(255), `Código` VARCHAR(255), Cuenta VARCHAR(255), Valor FLOAT, `Nombre del Archivo` VARCHAR(255))")


# crear la tabla "indicadores_financieros" si no existe
mycursor.execute("CREATE TABLE IF NOT EXISTS indicadores_financieros (id INT AUTO_INCREMENT PRIMARY KEY, Fecha DATE, `Tipo de Institucion` VARCHAR(255), `Institución` VARCHAR(255), `Dimension 1` VARCHAR(255), Cuenta VARCHAR(255), Valor FLOAT, `Nombre del Archivo` VARCHAR(255))")
