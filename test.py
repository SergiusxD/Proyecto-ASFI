import pandas as pd

# Crear DataFrame de ejemplo
df = pd.DataFrame({'col1': ['"valor1"', '"valor2"'], 'col2': ['"valor3"', '"valor4"']})
print(df)

# Eliminar comillas dobles
df = df.replace('"', '', regex=True)
print(df)


engine = create_engine('mysql+mysqlconnector://root:Hels1962*@localhost/Datos')

for archivo in excel_EF:
    # Leer el archivo de Excel en un DataFrame de Pandas
    df = pd.read_excel(archivo, sheet_name='Datos')

    # Escribir el DataFrame en la base de datos
    df.to_sql(name='estados_financieros', con=engine, if_exists='append', index=False)

for archivo in excel_I:
    # Leer el archivo de Excel en un DataFrame de Pandas
    df = pd.read_excel(archivo, sheet_name='Datos')

    # Escribir el DataFrame en la base de datos
    df.to_sql(name='indicadores_financieros', con=engine, if_exists='append', index=False)

# Cerrar la conexión
engine.dispose()
