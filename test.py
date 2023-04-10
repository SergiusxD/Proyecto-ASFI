import pandas as pd

# creamos un DataFrame de ejemplo
df = pd.DataFrame({'A': [1, 2, 3], 'B': ['h', 'mundo', 'k'], 'C': ['foo', 'bar', 'baz'], 
                   'D': [4, 5, 6], 'E': ['hola', 'mundo', 'hola'], 'F': ['foo', 'bar', 'baz'],
                   'G': [7, 8, 9], 'H': ['hola', 'mundo', 'hola'], 'I': ['TOTAL SISTEMA', 'bar', 'baz'],
                   'J': [10, 11, 12]})
print(df)

# Encontrar la columna que contiene la palabra "hola"
ultima_cols = df.columns[df.apply(lambda x: x.astype(str).str.contains('TOTAL SISTEMA')).any()]
col_idx = df.columns.get_loc(ultima_cols[0])

# Crear un nuevo DataFrame con las columnas hasta la columna encontrada
df = df.iloc[:, :col_idx+1]
