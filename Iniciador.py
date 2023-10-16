#Iniciador para los ESTADOS FINANCIEROS

from datetime import datetime, date, timedelta
from urllib import request
import zipfile
import os
from os import remove
import pandas as pd
from sqlalchemy import create_engine, text
import os
import re

def guardar_fecha_actual(year, month):
    fecha_actual = f"{year}-{month}"
    
    try:
        with open("fecha_actual.txt", "w") as archivo:
            archivo.write(fecha_actual)
        print("Fecha actual guardada en el archivo fecha_actual.txt")
    except Exception as e:
        print("Error al guardar la fecha actual:", str(e))

def leer_fecha_guardada():
    try:
        with open("fecha_actual.txt", "r") as archivo:
            fecha_actual = archivo.read()
        return fecha_actual.split("-")  # Devolver año y mes por separado
    except Exception as e:
        print("Error al leer la fecha guardada:", str(e))
        return None

def verificar_archivo_existente(nombre_archivo):
    return os.path.exists(nombre_archivo)

nombre_archivo = "fecha_actual.txt"

if verificar_archivo_existente(nombre_archivo):
    # El archivo existe, puedes proceder a leerlo o realizar otras operaciones
    fecha_guardada = leer_fecha_guardada()
    if fecha_guardada:
        Year = int(fecha_guardada[0])
        Month = int(fecha_guardada[1])
else:
    # El archivo no existe
    now = datetime.now()
    Month = now.month
    #Month = 1
    Year = now.year
    #Year = 2018
    # print (Year)
    # print (Month)
    print("El archivo", nombre_archivo, "no existe.")
    

file_BDR_EF = "BDR_EstadosFinancieros.zip"
file_BMU_EF = "BMU_EstadosFinancieros.zip"
file_BPY_EF = "BPY_EstadosFinancieros.zip"
file_EFV_EF = "EFV_EstadosFinancieros.zip"
file_COO_EF = "COO_EstadosFinancieros.zip"
file_IFD_EF = "IFD_EstadosFinancieros.zip"
file_BDR_I = "BDR_IndicadoresFinancieros.zip"
file_BMU_I = "BMU_IndicadoresFinancieros.zip"
file_BPY_I = "BPY_IndicadoresFinancieros.zip"
file_EFV_I = "EFV_IndicadoresFinancieros.zip"
file_COO_I = "COO_IndicadoresFinancieros.zip"
file_IFD_I = "IFD_IndicadoresFinancieros.zip"

# Condicion cuando es Primero del Mes
if Month == 1:
    newYear = Year - 1
    Month = 12
    mes = Month
    #Definiendo el Mes en Numero
    def current_date_format(Month):
        months = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        month = months[Month - 1]
        messsage = "{}".format( month)

        return messsage
    Month = current_date_format(Month)
    nowYear = newYear
    nowMonth = Month

else:
    newMonth = Month - 1
    mes = Month - 1
    #Definiendo el Mes en Numero
    def current_date_format(newMonth):
        months = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        month = months[newMonth - 1]
        messsage = "{}".format( month)

        return messsage
    newMonth = current_date_format(newMonth)
    nowYear = Year
    nowMonth = newMonth

# https://appweb.asfi.gob.bo/boletines_if/2022/12/BDR_IndicadoresFinancieros.zip
# https://appweb.asfi.gob.bo/boletines_if/2022/12/BDR_EstadosFinancieros.zip

# Definimos la URL del archivo a descargar
remote_urls = [
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_BDR_EF),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_BMU_EF),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_BPY_EF),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_EFV_EF),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_COO_EF),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_IFD_EF),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_BDR_I),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_BMU_I),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_BPY_I),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_EFV_I),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_COO_I),
    'https://appweb.asfi.gob.bo/boletines_if/{}/{}/{}'.format(nowYear, nowMonth, file_IFD_I),
]

# Definimos el nombre del archivo local a guardar
local_files = [
    '{}'.format(file_BDR_EF),
    '{}'.format(file_BMU_EF),
    '{}'.format(file_BPY_EF),
    '{}'.format(file_EFV_EF),
    '{}'.format(file_COO_EF),
    '{}'.format(file_IFD_EF),
    '{}'.format(file_BDR_I),
    '{}'.format(file_BMU_I),
    '{}'.format(file_BPY_I),
    '{}'.format(file_EFV_I),
    '{}'.format(file_COO_I),
    '{}'.format(file_IFD_I),
]

# Se realiza la descarga y se guarda el archivo de manera local
for remote_url, local_file in zip(remote_urls, local_files):
    try:
        request.urlretrieve(remote_url, local_file)
    except:
        print ("No se encontro el siguiente URL: " + remote_url)
        guardar_fecha_actual(Year, Month)

# D:\MSI\Documentos\PROYECTO DE ASFI\IDEPRO IFD
my_dir = "D:\\MSI\\Documentos\\PROYECTO DE ASFI\\Proyecto-ASFI" # Ruta de archivos ZIP
files_Zip = [file_BDR_EF, file_BMU_EF, file_BPY_EF, file_EFV_EF, file_COO_EF, file_IFD_EF, file_BDR_I, file_BMU_I, file_BPY_I, file_EFV_I, file_COO_I, file_IFD_I]
excel_EF = ["", "", "","", "", ""]
excel_I = ["", "", "","", "", ""]
j = 0

for i in range(len(files_Zip)):
    try:
        with zipfile.ZipFile(files_Zip[i]) as zip:
            for zip_info in zip.infolist():
                if zip_info.filename[-1] == '.xls':
                    continue
                zip_info.filename = os.path.basename(zip_info.filename)
                if i<=5:
                    excel_EF[i] = zip_info.filename
                else:
                    excel_I[j] = zip_info.filename
                    j = j + 1
                zip.extract(zip_info, my_dir)
    except:
        print ("No existe el zip: " + files_Zip[i])

#Eliminar los zip
for i in range(len(files_Zip)):
    try:
        remove(files_Zip[i])
    except:
        print ("No existe el zip: " + files_Zip[i])

#Comprabamos que esten los archivos para empezar
if all(elem == '' for elem in excel_EF) or all(elem == '' for elem in excel_I):
    print("No tengo nada que hacer")
else:
    #Creamos los DateFrame para cambiar los EXCELS
    columnas_I = ['Fecha', 'Tipo de Institucion', 'Institución', 'Dimension 1', 'Cuenta', 'Valor', 'Nombre del Archivo']
    columnas_EF = ['Fecha', 'Tipo de Institucion', 'Institución', 'Dimension 1', 'Código', 'Cuenta', 'Valor', 'Nombre del Archivo']
    datos_I = pd.DataFrame(columns=columnas_I)
    datos_EF = pd.DataFrame(columns=columnas_EF)

    for name in range(len(excel_I)):

        # Modificar los excels descargados INDICADORES
        excel1 = pd.read_excel(excel_I[name], header=None)
        info = pd.DataFrame(excel1)
        pd.set_option('display.max_rows', None)

        #print (info)
        # Encontrar la columna que contiene la palabra "TOTAL SISTEMA"
        ultima_cols = info.columns[info.apply(lambda x: x.astype(str).str.contains('TOTAL SISTEMA')).any()]
        col_idx = info.columns.get_loc(ultima_cols[0])
        info = info.iloc[:, :col_idx+1]
        print (info)

        if pd.isna(info.iloc[0, 0]) and nowYear < 2020:
            info = info.drop(info.index[0])
            info = info.reset_index(drop=True) # Reinicio de las filas y columnas

        if nowYear < 2020:
            tipo_indentidad = info.loc[1][0]
            if tipo_indentidad == 'BANCOS DE DESARROLLO PRODUCTIVO'or tipo_indentidad == 'BANCO DE DESARROLLO PRODUCTIVO':
                info = info.replace('TOTAL SISTEMA', 'TSBDR')
            elif tipo_indentidad == 'BANCOS MÚLTIPLES': 
                info = info.replace('TOTAL SISTEMA', 'TSBMU')
            elif tipo_indentidad == 'BANCOS PYME':
                info = info.replace('TOTAL SISTEMA', 'TSBPY')
            elif tipo_indentidad == 'COOPERATIVAS DE AHORRO Y CRÉDITO' or tipo_indentidad == 'COOPERATIVAS DE AHORRO Y CRÉDITO ABIERTAS':
                info = info.replace('TOTAL SISTEMA', 'TSCOO')
            elif tipo_indentidad == 'ENTIDADES FINANCIERAS DE VIVIENDA':
                info = info.replace('TOTAL SISTEMA', 'TSEFV')
            elif tipo_indentidad == 'INSTITUCIONES FINANCIERAS DE DESARROLLO':
                info = info.replace('TOTAL SISTEMA', 'TSIFD')
        else:
            tipo_indentidad = info.loc[0][0]
            if tipo_indentidad == 'BANCOS DE DESARROLLO PRODUCTIVO':
                info = info.replace('TOTAL SISTEMA', 'TSBDR')
            elif tipo_indentidad == 'BANCOS MÚLTIPLES':
                info = info.replace('TOTAL SISTEMA', 'TSBMU')
            elif tipo_indentidad == 'BANCOS PYME':
                info = info.replace('TOTAL SISTEMA', 'TSBPY')
            elif tipo_indentidad == 'COOPERATIVAS DE AHORRO Y CRÉDITO':
                info = info.replace('TOTAL SISTEMA', 'TSCOO')
            elif tipo_indentidad == 'ENTIDADES FINANCIERAS DE VIVIENDA':
                info = info.replace('TOTAL SISTEMA', 'TSEFV')
            elif tipo_indentidad == 'INSTITUCIONES FINANCIERAS DE DESARROLLO':
                info = info.replace('TOTAL SISTEMA', 'TSIFD')

        if pd.isna(info.iloc[0, 0]):
            info = info.drop(info.index[0])
            info = info.reset_index(drop=True) # Reinicio de las filas y columnas

        if pd.isna(info.iloc[0, 1]) and nowYear < 2020 and nowYear < 2020 and tipo_indentidad == 'COOPERATIVAS DE AHORRO Y CRÉDITO':
            info = info.drop(info.index[0])
            info = info.reset_index(drop=True) # Reinicio de las filas y columnas

        print (info)

        fecha_info = info.loc[2][0]
        split = fecha_info.split()

        m = {
            'enero': "01",
            'febrero': "02",
            'marzo': "03",
            'abril': "04",
            'mayo': "05",
            'junio': "06",
            'julio': "07",
            'agosto': "08",
            'septiembre': "09",
            'octubre': "10",
            'noviembre': "11",
            'diciembre': "12"
        }

        out = str(m[split[3].lower()])
        fecha = split[5] + "-" +  out + "-" + split[1]

        if nowYear < 2020:
            # Borror la basura de las 7 lineas
            info.drop([0,1,2,3,4,5,6], axis=0, inplace=True)
            info = info.reset_index(drop=True) # Reinicio de las filas y columnas
            info[0] = info[0].str.strip()
        else:
            # Borror la basura de las 4 lineas
            info.drop([0,1,2,3], axis=0, inplace=True)
            info = info.reset_index(drop=True) # Reinicio de las filas y columnas
            info[0] = info[0].str.strip()
            
        # Borro lineas basura
        if nowYear < 2020:
            idx = info.index[info[0].str.contains('Activo improductivo/Patrimonio', na=False)].tolist()[0]
            info = info.drop(info.index[idx+1:idx+8])
        else:
            idx = info.index[info[0].str.contains('Activo improductivo/Patrimonio', na=False)].tolist()[0]
            info = info.drop(info.index[idx+1:idx+7])
            
        #print (info)
        info = info.reset_index(drop=True) # Reinicio de las filas y columnas
        # Borro lineas basura
        index_to_drop = info.loc[info[0] == 'UTILIDAD NETA'].index[0]
        info = info.drop(index=range(index_to_drop+1, len(info)))
        info = info.reset_index(drop=True) # Reinicio de las filas y columnas
        # Borro nan de la primera colunma
        info = info.dropna(subset=info.columns[0:], thresh=1)
        info = info.reset_index(drop=True) # Reinicio de las filas y columnas
        info = info.drop(index=[45])
        info = info.reset_index(drop=True) # Reinicio de las filas y columnas

        num_columnas = info.shape[1] - 1

        # inicializar variables
        group = None
        groups = []

        # iterar sobre cada fila del dataframe
        for i, row in info.iterrows():
            # si la primera columna es un string en mayúsculas, entonces es un nuevo grupo
            if isinstance(row[0], str) and row[0].isupper():
                group = row[0]
            
            # agregar el grupo actual a la lista de grupos
            groups.append(group)

        # agregar la columna de grupos al dataframe
        info['Group'] = groups
        #print (info)

        # Esto seria para reparar los error que existen en sintaxis o espacios que se olvidan en la cuenta
        if nowYear <= 2022:           
            info[0] = info[0].replace('Prev.Cartera Incobrable/Cartera (1)', 'Prev. Cartera Incobrable/Cartera (1)')
            info[0] = info[0].replace('Gastos de Administración/Total Egresos (4)', 'Gastos de Administración/Total Egresos(4)')
            info[0] = info[0].replace('Oblig. Persones Jurídicas e Institucionales /Total Oblig. Público', 'Oblig. Personas Jurídicas e Institucionales /Total Oblig. Público')
            info[0] = info[0].replace('Oblig. Pers. Jurídicas e Institucionales /Total Oblig. Público', 'Oblig. Personas Jurídicas e Institucionales /Total Oblig. Público')
            info[0] = info[0].replace('Oblig. Personas. Naturales /Total Oblig. Público', 'Oblig. Personas Naturales /Total Oblig. Público')
            info[0] = info[0].replace('Oblig.con el Público y con Empresas Públicas/Pasivo+Patrimonio', 'Oblig. con el Público y con Empresas Públicas/Pasivo+Patrimonio')
            info[0] = info[0].replace('Oblig.con el Público/Pasivo+Patrimonio', 'Oblig. con el Público/Pasivo+Patrimonio')
            info[0] = info[0].replace('Oblig.con Bancos y Ent. Fin./Pasivo+Patrimonio', 'Oblig. con Bancos y Ent. Fin./Pasivo+Patrimonio')
            info[0] = info[0].replace('Obligaciones Subordinadas/Pasivo+Patrimonio', 'Oblig. Subordinadas/Pasivo+Patrimonio')
            info[0] = info[0].replace('Cargos por Oblig.con el B.C.B./Oblig.con el B.C.B.', 'Cargos por Oblig. con el B.C.B./Oblig. con el B.C.B.')
            info[0] = info[0].replace('Int.Deptos.Caja de Ahorro/Ob.Púb.Ctas.Ahorro', 'Int. Depósitos Caja de Ahorro/Oblig. Púb. Ctas. Ahorro')
            info[0] = info[0].replace('Int.Depósitos Púb.a Plazo/Dptos.Púb.a Plazo', 'Int. Depósitos Púb. a Plazo/Depósitos Púb. a Plazo')
            info[0] = info[0].replace('Int.Oblig.con Emp. públicas/Oblig.c/emp. públicas', 'Int. Oblig. con Emp. públicas/Oblig. c/emp. públicas')
            info[0] = info[0].replace('Int.Oblig.Púb.a la Vista/Oblig.Púb. a la Vista', 'Int. Oblig. Púb. a la Vista/Oblig. Púb. a la Vista')
            info[0] = info[0].replace('Int. penales Cartera en Ejecución Total / Productos cartera en Ejecución', 'Int. penales Cartera en Ejecución Total/Productos cartera en Ejecución')
            info[0] = info[0].replace('Int. penales Cartera Vencida Total y en Ejecución Total / Productos cartera Vencida Total y en Ejecución Total', 'Int. penales Cartera Vencida Total y en Ejecución Total/Productos cartera Vencida Total y en Ejecución')
            info[0] = info[0].replace('Int. penales Cartera Vencida Total / Productos cartera vencida total', 'Int. penales Cartera Vencida Total/Productos cartera vencida total')
            info[0] = info[0].replace('Productos por Cartera Reprog. y Reestruct. Vencida y en Ejec. /Cartera Reprog. y Reestruct. Vencida y en Ejec.', 'Productos por Cartera Reprog. y Reestruct. Vencida y en Ejec./Cartera Reprog. y Reestruct. Vencida')
            info[0] = info[0].replace('Productos por Cartera Reprog. y Reestruct. Vigente/ Cartera Reprog. y Reestruct. Vigente', 'Productos por Cartera Reprog. y Reestruct. Vigente/Cartera Reprog. y Reestruct. Vigente')
            info[0] = info[0].replace('Productos por CarteraVencida y en Ejecución/Cartera Vencida y en Ejecución', 'Productos por Cartera Vencida y en Ejecución/Cartera Vencida y en Ejecución')
            info[0] = info[0].replace('Productos por Cartera Vigente/Cartera Vigente.', 'Productos por Cartera Vigente/Cartera Vigente')
            info[0] = info[0].replace('Activos líquidos/Depósitos corto plazo (5)', 'Activos líquidos/Pasivos de corto plazo (5)')
            info[0] = info[0].replace('Margen Financiero en Activos ProductivosPromedio Neto de Contingente', 'Margen Financiero en Activos Productivos Promedio Neto de Contingente')
            info[0] = info[0].replace('Gastos de Administración/Depositos(3)', 'Gastos de Administración/Depósitos (3)')
            info[0] = info[0].replace('Result.de Operación Bruto/(Activo+Contingente)', 'Resultado de Operación Bruto/(Activo+Contingente)')
            info[0] = info[0].replace('Gastos de Administración/Depósitos (3)', 'Gastos de Administración/Depósitos(3)')
            info[0] = info[0].replace('Resultado de operación después de Incobrables /(Activo + Contingente)', 'Resultado de operación después de Incobrables/(Activo + Contingente)')
            info[0] = info[0].replace('Result.de Operación Neto Antes de Impuestos/(Activo+Contingente)', 'Resultado de Operación Neto Antes de Impuestos/(Activo+Contingente)')
            info[0] = info[0].replace('Result. de Operación Neto/(Activo + Contingente)', 'Resultado de Operación Neto/(Activo + Contingente)')
            info[0] = info[0].replace('Result.Neto de la Gestión/(Activo+Contingente) (ROA)', 'Resultado Neto de la Gestión/(Activo+Contingente) (ROA)')
            info[0] = info[0].replace('Result.Neto de la Gestión/Patrimonio (ROE)', 'Resultado Neto de la Gestión/Patrimonio (ROE)')
            info[0] = info[0].replace('Ajustes netos por inflación y por diferencias de cambio/Activo+Conting. (2)', 'Ajustes netos por inflación y por diferencias de cambio/Activo+Conting.(2)')
            info[0] = info[0].replace('Cargos por Incob.Netos de Recuper./Activo+Conting.', 'Cargos por Incob. Netos de Recuper./Activo+Conting.')
            info[0] = info[0].replace('Deprec.y Desval.Bienes de Uso/Bienes de Uso-Terrenos.', 'Deprec.y Desval.Bienes de Uso/Bienes de Uso-Terrenos')
            info[0] = info[0].replace('Deprec.y Desval.Bienes de Uso/Bienes de Uso-Terrenos', 'Deprec. y Desval. Bienes de Uso/Bienes de Uso-Terrenos')
            info[0] = info[0].replace('Gastos de Administración/Activo+Contingente.', 'Gastos de Administración/Activo+Contingente')
            info[0] = info[0].replace('Ing.Extraord.y de Gest.Ant.Netos/Activo+Conting.', 'Ing. Extraord. y de Gest. Ant. Netos/Activo+Conting.')
            info[0] = info[0].replace('Otros Ingresos Operativos Netos/Activo+Contingente.', 'Otros Ingresos Operativos Netos/Activo+Contingente')
            
        info = info.dropna(subset=[1])
        info = info.reset_index(drop=True) # Reinicio de las filas y columnas

        info_indicadores = info.loc[:, [0, 'Group']]
        info_indicadores = info_indicadores.dropna(subset=[0])
        #print(info_indicadores)

        #Multiplicamos la tabla deacuerdo a las columnas o las entidas que se tenga
        info_indicadores_final = pd.concat([info_indicadores] * num_columnas, ignore_index=True)

        # Agregar datos iniciales al dataframe
        datos_I[['Dimension 1', 'Cuenta']] = info_indicadores_final.loc[:, ['Group',0]]

        info = info.drop([0, 'Group'], axis=1).reset_index(drop=True)
        info = info.reset_index(drop=True) # Reinicio de las filas y columnas

        info.columns = info.iloc[0]
        info = info.drop(0)
        info = info.reset_index().melt(id_vars='index')
        info.columns = ['Index', 'Institución', 'Valores']
        info = info.drop('Index', axis=1)

        datos_I[['Institución', 'Valor']] = info.loc[:, ['Institución','Valores']]

        # Llenar las columnas Fecha y Tipo de Institución con las variables fecha y tipo, respectivamente
        datos_I['Fecha'] = fecha
        datos_I['Tipo de Institucion'] = tipo_indentidad
        datos_I['Nombre del Archivo'] = excel_I[name]

        datos_I['Valor'] = pd.to_numeric(datos_I['Valor'], errors='coerce')
        datos_I['Valor'] = datos_I['Valor'].round(4)

        # crear un objeto ExcelWriter
        writer = pd.ExcelWriter(excel_I[name], engine='xlsxwriter')
        # escribir el DataFrame en una hoja llamada 'Datos'
        datos_I.to_excel(writer, sheet_name='Datos', index=False)
        # guardar los cambios
        writer.save()
        writer.close()
        datos_I.drop(index=datos_I.index, inplace=True)
        info.drop(index=info.index, inplace=True)

    #Codigos para Estados Financieros
    def assign_code(row):
        Columna = row[0]
        if Columna.endswith('ACTIVO'):
            return '100.00'
        elif re.search(r'\bPRODUCTOS DEVENGADOS POR COBRAR DISPONIBILIDADES\b', Columna):
            return '118.00'
        elif re.search(r'\bPREVISIÓN PARA DISPONIBILIDADES\b', Columna):
            return '119.00'
        elif re.search(r'\bCambiado\b', Columna):
            return '121.00'
        elif re.search(r'\bPRODUCTOS DEVENGADOS POR COBRAR INVERSIONES TEMPORARIAS\b', Columna):
            return '128.00'
        elif re.search(r'\bPRODUCTOS DEVENGADOS POR COBRAR CARTERA\b', Columna):
            return '138.00'
        elif re.search(r'\bOTROS BIENES REALIZABLES\b', Columna):
            return '157.00'
        elif re.search(r'\bINVERSIONES EN EL BANCO CENTRAL DE BOLIVIA\b', Columna):
            return '161.00'
        elif re.search(r'\bINVERSIONES EN ENTIDADES FINANCIERAS DEL PAÍS\b', Columna):
            return '162.00'
        elif re.search(r'\bINVERSIONES EN ENTIDADES FINANCIERAS DEL EXTERIOR\b', Columna):
            return '163.00'
        elif re.search(r'\bINVERSIONES EN ENTIDADES PÚBLICAS NO FINANCIERAS DEL PAÍS\b', Columna):
            return '164.00'
        elif re.search(r'\bINVERSIONES EN OTRAS ENTIDADES NO FINANCIERAS\b', Columna):
            return '166.00'
        elif re.search(r'\bINVERSIONES DE DISPONIBILIDAD RESTRINGIDA\b', Columna):
            return '167.00'
        elif re.search(r'\bPRODUCTOS DEVENGADOS POR COBRAR INVERSIONES PERMANENTES\b', Columna):
            return '168.00'
        elif re.search(r'\bPRODUCTOS DEVENGADOS DE OTRAS CUENTAS POR COBRAR\b', Columna):
            return '148.00'
        elif re.search(r'\bCARGOS DEVENGADOS POR PAGAR OBLIGACIONES CON EL PÚBLICO\b', Columna):
            return '218.00'
        elif re.search(r'\bPARTIDAS PENDIENTES DE IMPUTACIÓN\b', Columna):
            return '244.00'
        elif re.search(r'\bCARGOS DEVENGADOS DE OTRAS CUENTAS POR PAGAR\b', Columna):
            return '248.00'
        elif re.search(r'\bDIVERSAS\b', Columna):
            return '242.00'
        elif re.search(r'\bOTRAS PREVISIONES\b', Columna):
            return '257.00'
        elif 'CARGOS DEVENGADOS POR PAGAR VALORES EN CIRCULACIÓN' in Columna:
            return '268.00'
        elif re.search(r'\bOBLIGACIONES SUBORDINADAS INSTRUMENTADAS MEDIANTE BONOS\b', Columna):
            return '272.00'
        elif re.search(r'\bCARGOS DEVENGADOS POR PAGAR OBLIGACIONES SUBORDINADAS\b', Columna):
            return '278.00'
        elif re.search(r'\bAJUSTES AL PATRIMONIO\b', Columna):
            return '330.00'
        elif re.search(r'\bAJUSTES PARTICIPACIÓN EN ENTIDADES FINANCIERAS Y AFINES\b', Columna):
            return '333.00'
        elif 'PASIVO + PATRIMONIO' in Columna:
            return 'C00.20'
        elif re.search(r'\bOTROS VALORES Y BIENES RECIBIDOS EN CUSTODIA\b', Columna):
            return '819.00'
        elif re.search(r'\bADMINISTRACIÓN DE CARTERA\b', Columna):
            return '822.00'
        elif re.search(r'\bOTROS VALORES Y BIENES RECIBIDOS EN ADMINISTRACIÓN\b', Columna):
            return '829.00'
        elif re.search(r'\bCambiado3\b', Columna):
            return '0.00'
        elif re.search(r'\bPRODUCTOS POR DISPONIBILIDADES\b', Columna):
            return '511.00'
        elif re.search(r'\bPRODUCTOS POR INVERSIONES TEMPORARIAS\b', Columna):
            return '512.00'
        elif re.search(r'\bPRODUCTOS DE CARTERA VIGENTE\b', Columna):
            return '513.00'
        elif re.search(r'\bPRODUCTOS DE CARTERA VENCIDA\b', Columna):
            return '515.00'
        elif re.search(r'\bCambiado20\b', Columna):
            return '516.00'
        elif re.search(r'\bCARGOS POR OBLIGACIONES CON EL PÚBLICO\b', Columna):
            return '411.00'
        elif re.search(r'\bCARGOS POR OBLIGACIONES CON INSTITUCIONES FISCALES\b', Columna):
            return '412.00'
        elif re.search(r'\bCARGOS POR OBLIGACIONES CON BANCOS Y ENTIDADES DE FINANCIAMIENTO\b', Columna):
            return '413.00'
        elif re.search(r'\bCARGOS POR VALORES EN CIRCULACIÓN\b', Columna):
            return '415.00'
        elif re.search(r'\bCARGOS POR OBLIGACIONES SUBORDINADAS\b', Columna):
            return '416.00'
        elif re.search(r'\bCARGOS POR OBLIGACIONES CON EMPRESAS PÚBLICAS\b', Columna):
            return '417.00'
        elif re.search(r'\bINGRESOS POR BIENES REALIZABLES\b', Columna):
            return '543.00'
        elif re.search(r'\bRENDIMIENTOS EN FIDEICOMISOS CONSTITUIDOS\b', Columna):
            return '546.00'
        elif re.search(r'\bCOMISIONES POR SERVICIOS\b', Columna):
            return '441.00'
        elif re.search(r'\bCOSTO DE BIENES REALIZABLES\b', Columna):
            return '442.00'
        elif re.search(r'\bCARGOS POR FIDEICOMISOS CONSTITUIDOS\b', Columna):
            return '446.00'
        elif re.search(r'\bDISMINUCIÓN DE PREVISIÓN PARA INVERSIONES TEMPORARIAS\b', Columna):
            return '533.00'
        elif re.search(r'\bCambiado4\b', Columna):
            return '535.00'
        elif re.search(r'\bCambiado5\b', Columna):
            return '536.00'
        elif re.search(r'\bPÉRDIDAS POR INVERSIONES TEMPORARIAS\b', Columna):
            return '432.00'
        elif re.search(r'\bPÉRDIDAS POR DISPONIBILIDADES\b', Columna):
            return '435.00'
        elif re.search(r'\bCambiado7\b', Columna):
            return '436.00'
        elif re.search(r'\bDEPRECIACIÓN Y DESVALORIZACIÓN DE BIENES DE USO\b', Columna):
            return '457.00'
        elif re.search(r'\bAMORTIZACIÓN DE CARGOS DIFERIDOS Y ACTIVOS INTANGIBLES\b', Columna):
            return '458.00'
        elif re.search(r'\bPATRIMONIO\b', Columna):
            return '300.00'
        elif re.search(r'\bOBLIGACIONES CON BANCOS Y ENTIDADES DE FINANCIAMIENTO\b', Columna):
            return '230.00'
        elif re.search(r'\bCOMISIONES POR SERVICIOS\b', Columna):
            return '541.00'
        elif Columna.endswith('DISPONIBILIDADES'):
            return '110.00'
        elif Columna.endswith('CAJA'):
            return '111.00'
        elif Columna.endswith('BANCO CENTRAL DE BOLIVIA'):
            return '112.00'
        elif Columna.endswith('BANCOS Y CORRESPONSALES DEL PAÍS'):
            return '113.00'
        elif Columna.endswith('OFICINA MATRIZ Y SUCURSALES'):
            return '114.00'
        elif Columna.endswith('BANCOS Y CORRESPONSALES DEL EXTERIOR'):
            return '115.00'
        elif Columna.endswith('DOCUMENTOS DE COBRO INMEDIATO Y OTRAS OPERACIONES PENDIENTES DE LIQUIDACIÓN'):
            return '117.00'
        elif Columna.endswith('INVERSIONES TEMPORARIAS'):
            return '120.00'
        elif re.search(r'\bCambiado12\b', Columna):
            return '122.00'
        elif re.search(r'\bCambiado13\b', Columna):
            return '123.00'
        elif re.search(r'\bCambiado14\b', Columna):
            return '124.00'
        elif re.search(r'\bCambiado15\b', Columna):
            return '126.00'
        elif re.search(r'\bCambiado16\b', Columna):
            return '127.00'
        elif Columna.endswith('(PREVISIÓN PARA INVERSIONES TEMPORARIAS)'):
            return '129.00'
        elif Columna.endswith('CARTERA'):
            return '130.00'
        elif Columna.endswith('CARTERA VIGENTE TOTAL'):
            return '131.00 + 135.00 + 99.00'
        elif Columna.endswith('CARTERA VIGENTE'):
            return '131.00'
        elif Columna.endswith('CARTERA REPROGRAMADA VIGENTE'):
            return '135.00'
        elif Columna.endswith('CARTERA REESTRUCTURADA VIGENTE'):
            return '99.00'
        elif Columna.endswith('CARTERA VENCIDA TOTAL'):
            return '133.00 + 136.00 + 98.00'
        elif Columna.endswith('CARTERA VENCIDA'):
            return '133.00'
        elif Columna.endswith('CARTERA REPROGRAMADA VENCIDA'):
            return '136.00'
        elif Columna.endswith('CARTERA REESTRUCTURADA VENCIDA'):
            return '98.00'
        elif Columna.endswith('CARTERA EJECUCIÓN TOTAL'):
            return '134.00 + 137.00 + 97.00'
        elif re.search(r'\bCARTERA EN EJECUCIÓN\b', Columna):
            return '134.00'
        elif re.search(r'\bCARTERA REPROGRAMADA EJECUCIÓN\b', Columna):
            return '137.00'
        elif re.search(r'\bCARTERA REESTRUCTURADA EN EJECUCIÓN\b', Columna):
            return '97.00'        
        elif Columna.endswith('Productos devengados por cobrar cartera vigente'):
            return '138.01'
        elif Columna.endswith('Productos devengados por cobrar cartera reprogramada o reestructurada vigente'):
            return '138.05'
        elif Columna.endswith('Productos devengados por cobrar cartera vencida'):
            return '138.03'
        elif Columna.endswith('Productos devengados por cobrar cartera reprogramada o reestructurada vencida'):
            return '138.06'
        elif re.search(r'\bProductos devengados por cobrar cartera en ejecución\b', Columna):
            return '138.04'
        elif re.search(r'\bProductos devengados por cobrar cartera reprogramada o reestructurada ejecución\b', Columna):
            return '138.07'
        elif Columna.endswith('Productos devengados por cobrar de préstamos diferidos vigentes'):
            return '138.50'
        elif Columna.endswith('Productos devengados por cobrar de préstamos reprogramados o reestructurados diferidos vigentes'):
            return '138.51'
        elif Columna.endswith('Productos devengados por cobrar de préstamos diferidos vencidos'):
            return '138.52'
        elif Columna.endswith('Productos devengados por cobrar de préstamos reprogramados o reestructurados diferidos vencidos'):
            return '138.53'
        elif re.search(r'\bProductos devengados por cobrar de préstamos diferidos en ejecución\b', Columna):
            return '138.54'
        elif re.search(r'\bProductos devengados por cobrar de préstamos reprogramados o reestructurados diferidos en ejecución\b', Columna):
            return '138.55'
        elif Columna.endswith('(PREVISIÓN PARA INCOBRABILIDAD DE CARTERA)'):
            return '139.00'
        elif Columna.endswith('(Previsión específica para incobrabilidad de cartera vigente)'):
            return '139.01'
        elif Columna.endswith('(Previsión específica para incobrabilidad de cartera reprogramada o reestructurada vigente)'):
            return '139.05'
        elif Columna.endswith('(Previsión específica para incobrabilidad de cartera vencida)'):
            return '139.03'
        elif Columna.endswith('(Previsión específica para incobrabilidad de cartera reprogramada o reestructurada vencida)'):
            return '139.06'
        elif re.search(r'\b(Previsión específica para incobrabilidad de cartera en ejecución)\b', Columna):
            return '139.04'
        elif re.search(r'\b(Previsión especifica para incobrabilidad de cartera reprogramada o reestructurada en ejecución)\b', Columna):
            return '139.07'
        elif re.search(r'\b(Previsión específica para incobrabilidad de cartera reprogramada o reestructurada en ejecución)\b', Columna):
            return '139.07'
        elif Columna.endswith('(Previsión genérica para incobrabilidad de cartera por factores de riesgo adicional)'):
            return '139.08'
        elif Columna.endswith('(Previsión genérica para incobrabilidad de cartera por otros riesgos)'):
            return '139.09'
        elif Columna.endswith('(Previsión específica adicional)'):
            return '139.10'
        elif Columna.endswith('(Previsión genérica por exceso al límite de Operaciones de Consumo No Debidamente Garantizadas)'):
            return '139.11'
        elif Columna.endswith('(Previsión específica para incobrabilidad de préstamos diferidos vigentes)'):
            return '139.50'
        elif Columna.endswith('(Previsión específica para incobrabilidad de préstamos reprogramados o reestructurados diferidos vigentes)'):
            return '139.51'
        elif Columna.endswith('(Previsión específica para incobrabilidad de préstamos diferidos vencidos)'):
            return '139.52'
        elif Columna.endswith('(Previsión específica para incobrabilidad de préstamos reprogramados o reestructurados diferidos vencidos)'):
            return '139.53'
        elif re.search(r'\b(Previsión específica para incobrabilidad de préstamos diferidos en ejecución)\b', Columna):
            return '139.54'
        elif re.search(r'\b(Previsión específica para incobrabilidad de préstamos reprogramados o reestructurados diferidos en ejecución)\b', Columna):
            return '139.55'
        elif re.search(r'\bOTRAS CUENTAS POR COBRAR\b', Columna):
            return '140.00'
        elif Columna.endswith('POR INTERMEDIACIÓN FINANCIERA'):
            return '141.00'
        elif Columna.endswith('PAGOS ANTICIPADOS'):
            return '142.00'
        elif 'Cambiado2' in Columna:
            return '143.00'
        elif re.search(r'\bCambiado17\b', Columna):
            return '149.00'
        elif Columna.endswith('BIENES REALIZABLES'):
            return '150.00'
        elif Columna.endswith('BIENES ADQUIRIDOS O CONSTRUIDOS PARA LA VENTA'):
            return '151.00'
        elif Columna.endswith('BIENES RECIBIDOS EN RECUPERACIÓN DE CRÉDITOS'):
            return '152.00'
        elif Columna.endswith('BIENES FUERA DE USO'):
            return '153.00'
        elif Columna.endswith('(PREVISIÓN POR DESVALORIZACIÓN)'):
            return '159.00'
        elif Columna.endswith('INVERSIONES PERMANENTES'):
            return '160.00'
        elif Columna.endswith('PARTICIPACIÓN EN ENTIDADES FINANCIERAS Y AFINES'):
            return '165.00'
        elif Columna.endswith('(PREVISIÓN PARA INVERSIONES PERMANENTES)'):
            return '169.00'
        elif Columna.endswith('BIENES DE USO'):
            return '170.00'
        elif Columna.endswith('TERRENOS'):
            return '171.00'
        elif Columna.endswith('EDIFICIOS'):
            return '172.00'
        elif Columna.endswith('MOBILIARIO Y ENSERES'):
            return '173.00'
        elif Columna.endswith('EQUIPOS E INSTALACIONES'):
            return '174.00'
        elif Columna.endswith('EQUIPOS DE COMPUTACIÓN'):
            return '175.00'
        elif Columna.endswith('VEHÍCULOS'):
            return '176.00'
        elif Columna.endswith('OBRAS DE ARTE'):
            return '177.00'
        elif Columna.endswith('BIENES TOMADOS EN ARRENDAMIENTO FINANCIERO'):
            return '178.00'
        elif Columna.endswith('OBRAS EN CONSTRUCCIÓN'):
            return '179.00'
        elif Columna.endswith('OTROS ACTIVOS'):
            return '180.00'
        elif Columna.endswith('BIENES DIVERSOS'):
            return '181.00'
        elif Columna.endswith('CARGOS DIFERIDOS'):
            return '182.00'
        elif re.search(r'\bCambiado18\b', Columna):
            return '183.00'
        elif Columna.endswith('ACTIVOS INTANGIBLES'):
            return '184.00'
        elif re.search(r'\bCambiado19\b', Columna):
            return '189.00'
        elif Columna.endswith('FIDEICOMISOS CONSTITUIDOS'):
            return '190.00'
        elif Columna.endswith('FIDEICOMISOS PARA SECTORES PRODUCTIVOS'):
            return '191.00'
        elif Columna.endswith('FIDEICOMISOS POR SERVICIOS DE PAGO'):
            return '192.00'
        elif Columna.endswith('FIDEICOMISOS POR LA TRANSMISIÓN DE ACCIONES'):
            return '193.00'
        elif Columna.endswith('FIDEICOMISOS PARA FONDOS DE CAPITAL DE RIESGO'):
            return '194.00'
        elif Columna.endswith('RENDIMIENTOS POR COBRAR POR FIDEICOMISOS'):
            return '198.00'
        elif Columna.endswith('PREVISIONES POR FIDEICOMISOS'):
            return '199.00'
        elif Columna.endswith('PASIVO'):
            return '200.00'
        elif Columna.endswith('OBLIGACIONES CON EL PÚBLICO'):
            return '210.00'
        elif Columna.endswith('OBLIGACIONES CON EL PÚBLICO A LA VISTA'):
            return '211.00'
        elif Columna.endswith('Depósitos en cuenta corriente'):
            return '211.01'
        elif Columna.endswith('Otras obligaciones con el público a la vista'):
            return '211.99'
        elif Columna.endswith('OBLIGACIONES CON EL PÚBLICO POR CUENTAS DE AHORROS'):
            return '212.00'
        elif Columna.endswith('OBLIGACIONES CON EL PÚBLICO A PLAZO'):
            return '213.00'
        elif Columna.endswith('Depósitos a plazo fijo hasta 30 días'):
            return '213.01'
        elif Columna.endswith('Depósitos a plazo fijo de 31 a 60 días'):
            return '213.02'
        elif Columna.endswith('Depósitos a plazo fijo de 61 a 90 días'):
            return '213.03'
        elif Columna.endswith('Depósitos a plazo fijo de 91 a 180 días'):
            return '213.04'
        elif Columna.endswith('Depósitos a plazo fijo de 181 a 360 días'):
            return '213.05'
        elif Columna.endswith('Depósitos a plazo fijo de 361 a 720 días'):
            return '213.06'
        elif Columna.endswith('Depósitos a plazo fijo de 721 a 1.080 días'):
            return '213.07'
        elif Columna.endswith('Depósitos a plazo fijo mayor a 1.080 días'):
            return '213.08'
        elif Columna.endswith('OBLIGACIONES CON EL PÚBLICO RESTRINGIDAS'):
            return '214.00'
        elif Columna.endswith('OBLIGACIONES CON EL PÚBLICO A PLAZO FIJO CON ANOTACIÓN EN CUENTA'):
            return '215.00'
        elif Columna.endswith('OBLIGACIONES CON INSTITUCIONES FISCALES'):
            return '220.00'
        elif Columna.endswith('OBLIGACIONES CON EMPRESAS PÚBLICAS'):
            return '280.00'
        elif Columna.endswith('Obligaciones con empresas públicas a la vista'):
            return '281.00'
        elif Columna.endswith('Obligaciones con empresas públicas por cuentas de ahorros'):
            return '282.00'
        elif Columna.endswith('Obligaciones con empresas públicas a plazo'):
            return '283.00'
        elif Columna.endswith('Obligaciones con empresas públicas restringidas'):
            return '284.00'
        elif Columna.endswith('Obligaciones con empresas públicas a plazo fijo con anotación en cuenta'):
            return '285.00'
        elif Columna.endswith('Cargos devengados por pagar con empresas públicas'):
            return '288.00'
        elif Columna.endswith('Obligaciones con bancos y entidades financieras a la vista'):
            return '231.00'
        elif Columna.endswith('Obligaciones con el BCB a plazo'):
            return '232.00'
        elif Columna.endswith('Obligaciones con el FONDESIF a plazo'):
            return '233.00'
        elif Columna.endswith('Obligaciones con entidades financieras que realizan actividades de segundo piso a plazo'):
            return '234.00'
        elif Columna.endswith('Obligaciones con bancos y otras entidades financieras del país a plazo'):
            return '235.00'
        elif Columna.endswith('Otros financiamientos internos a plazo'):
            return '236.00'
        elif Columna.endswith('Financiamientos de entidades del exterior a plazo'):
            return '237.00'
        elif Columna.endswith('Cargos devengados por pagar obligaciones con bancos y ent. de financiamiento'):
            return '238.00'
        elif Columna.endswith('OTRAS CUENTAS POR PAGAR'):
            return '240.00'
        elif Columna.endswith('POR INTERMEDIACIÓN FINANCIERA'):
            return '241.00'
        elif Columna.endswith('PROVISIONES'):
            return '243.00'
        elif Columna.endswith('PREVISIONES'):
            return '250.00'
        elif Columna.endswith('PREVISIÓN PARA ACTIVOS CONTINGENTES'):
            return '251.00'
        elif Columna.endswith('PREVISIÓN PARA DESAHUCIO'):
            return '252.00'
        elif Columna.endswith('PREV. GENÉRICAS VOLUNT. PARA PÉRDIDAS FUTURAS AÚN NO IDENTIF.'):
            return '253.00'
        elif Columna.endswith('PREVISIÓN PARA CUENTAS DE ORDEN'):
            return '254.00'
        elif Columna.endswith('PREVISIÓN GENÉRICA CÍCLICA'):
            return '255.00'
        elif 'VALORES EN CIRCULACIÓN' in Columna:
            return '260.00'
        elif Columna.endswith('BONOS'):
            return '261.00'
        elif Columna.endswith('CÉDULAS HIPOTECARIAS'):
            return '262.00'
        elif Columna.endswith('PAGARÉS'):
            return '263.00'
        elif Columna.endswith('OBLIGACIONES SUBORDINADAS'):
            return '270.00'
        elif Columna.endswith('OBLIG.SUBORDIN. INSTRUMENTADAS MEDIANTE CONTRATO DE PRÉSTAMO'):
            return '271.00'
        elif Columna.endswith('Oblig. subordinadas con programas gubernamentales de apoyo al sistema financiero'):
            return '271.01'
        elif Columna.endswith('Obligaciones subordinadas con el FONDESIF'):
            return '271.02'
        elif Columna.endswith('Obligaciones subordinadas con entidades financieras del exterior'):
            return '271.03'
        elif Columna.endswith('Obligaciones subordinadas PROFOP'):
            return '271.04'
        elif Columna.endswith('Otras oblig.subordinadas instrumentadas mediante contrato de préstamo'):
            return '271.99'
        elif Columna.endswith('CAPITAL SOCIAL'):
            return '310.00'
        elif Columna.endswith('CAPITAL PAGADO'):
            return '311.00'
        elif Columna.endswith('CAPITAL SUSCRITO'):
            return '312.00'
        elif Columna.endswith('(SUSCRIPCIONES DE CAPITAL PENDIENTES DE INTEGRACIÓN)'):
            return '313.00'
        elif Columna.endswith('APORTES NO CAPITALIZADOS'):
            return '320.00'
        elif Columna.endswith('PRIMAS DE EMISIÓN'):
            return '321.00'
        elif Columna.endswith('APORTES PARA FUTUROS AUMENTOS DE CAPITAL'):
            return '322.00'
        elif Columna.endswith('DONACIONES NO CAPITALIZABLES'):
            return '323.00'
        elif Columna.endswith('RESERVAS'):
            return '340.00'
        elif Columna.endswith('RESERVA LEGAL'):
            return '341.00'
        elif Columna.endswith('OTRAS RESERVAS OBLIGATORIAS'):
            return '342.00'
        elif Columna.endswith('RESERVAS VOLUNTARIAS'):
            return '343.00'
        elif Columna.endswith('RESULTADOS ACUMULADOS'):
            return '350.00'
        elif Columna.endswith('Utilidades (pérdidas) acumuladas'):
            return '351.00'
        elif Columna.endswith('Utilidades (pérdidas) del periodo o gestión'):
            return '352.00'
        elif Columna.endswith('CUENTAS CONTINGENTES DEUDORAS'):
            return '600.00'
        elif Columna.endswith('CARTAS DE CRÉDITO'):
            return '610.00'
        elif Columna.endswith('CARTAS DE CRÉDITO EMITIDAS A LA VISTA'):
            return '611.00'
        elif Columna.endswith('CARTAS DE CRÉDITO EMITIDAS DIFERIDAS'):
            return '612.00'
        elif Columna.endswith('CARTAS DE CRÉDITO CONFIRMADAS'):
            return '613.00'
        elif Columna.endswith('CARTAS DE CRÉDITO CON PREPAGOS'):
            return '614.00'
        elif Columna.endswith('CARTAS DE CRÉDITO STAND BY'):
            return '615.00'
        elif Columna.endswith('GARANTÍAS OTORGADAS'):
            return '620.00'
        elif Columna.endswith('AVALES'):
            return '621.00'
        elif Columna.endswith('BOLETAS DE GARANTÍA CONTRAGARANTIZADAS'):
            return '622.00'
        elif Columna.endswith('BOLETAS DE GARANTÍA'):
            return '623.00'
        elif Columna.endswith('OTRAS FIANZAS'):
            return '624.00'
        elif Columna.endswith('GARANTÍAS A PRIMER REQUERIMIENTO'):
            return '625.00'
        elif Columna.endswith('DOCUMENTOS DESCONTADOS'):
            return '630.00'
        elif Columna.endswith('LÍNEAS DE CRÉDITO COMPROMETIDAS'):
            return '640.00'
        elif Columna.endswith('CRÉDITOS ACORDADOS EN CUENTA CORRIENTE'):
            return '641.00'
        elif Columna.endswith('CRÉDITOS ACORDADOS PARA TARJETAS DE CRÉDITO'):
            return '642.00'
        elif Columna.endswith('CRÉDITOS ACORDADOS PARA FACTORAJE'):
            return '643.00'
        elif Columna.endswith('LÍNEAS DE CRÉDITO OTORGADAS'):
            return '644.00'
        elif Columna.endswith('OTRAS CONTINGENCIAS'):
            return '650.00'
        elif Columna.endswith('CUENTAS DE ORDEN DEUDORAS'):
            return '800.00'
        elif Columna.endswith('VALORES Y BIENES RECIBIDOS EN CUSTODIA'):
            return '810.00'
        elif Columna.endswith('CUSTODIA DE TÍTULOS VALORES NEGOCIABLES EN BOLSA'):
            return '811.00'
        elif Columna.endswith('VALORES PÚBLICOS EN CUSTODIA'):
            return '812.00'
        elif Columna.endswith('VALORES Y BIENES RECIBIDOS EN ADMINISTRACIÓN'):
            return '820.00'
        elif Columna.endswith('ADMINISTRACIÓN DE TÍTULOS VALORES NEGOCIABLES EN BOLSA'):
            return '821.00'
        elif Columna.endswith('ADMINISTRACIÓN DE CUENTAS FISCALES'):
            return '823.00'
        elif Columna.endswith('ADMIN. DE TRASPASO DE CTAS. DE ENCAJE LEGAL DE ENT. DE INTERM. FINANC.'):
            return '824.00'
        elif Columna.endswith('VALORES EN COBRANZA'):
            return '830.00'
        elif Columna.endswith('COBRANZAS EN COMISIÓN RECIBIDAS'):
            return '831.00'
        elif Columna.endswith('COBRANZAS EN COMISIÓN REMITIDAS'):
            return '832.00'
        elif Columna.endswith('VALORES Y BIENES RECIBIDOS EN CONSIGNACIÓN'):
            return '840.00'
        elif Columna.endswith('VALORES RECIBIDOS EN CONSIGNACIÓN'):
            return '841.00'
        elif Columna.endswith('BIENES RECIBIDOS EN CONSIGNACIÓN'):
            return '842.00'
        elif Columna.endswith('GARANTÍAS RECIBIDAS'):
            return '850.00'
        elif Columna.endswith('GARANTÍAS HIPOTECARIAS'):
            return '851.00'
        elif Columna.endswith('GARANTÍAS EN TÍTULOS VALORES'):
            return '852.00'
        elif Columna.endswith('OTRAS GARANTÍAS PRENDARIAS'):
            return '853.00'
        elif Columna.endswith('BONOS DE PRENDA'):
            return '854.00'
        elif Columna.endswith('DEPÓSITOS EN LA ENTIDAD FINANCIERA'):
            return '855.00'
        elif Columna.endswith('GARANTÍAS DE OTRAS ENTIDADES FINANCIERAS'):
            return '856.00'
        elif Columna.endswith('BIENES EMBARGADOS'):
            return '857.00'
        elif Columna.endswith('OTRAS GARANTÍAS'):
            return '859.00'
        elif Columna.endswith('CUENTAS DE REGISTRO'):
            return '860.00'
        elif Columna.endswith('LÍNEAS DE CRÉDITO OTORGADAS Y NO UTILIZADAS'):
            return '861.00'
        elif Columna.endswith('LÍNEAS DE CRÉDITO OBTENIDAS Y NO UTILIZADAS'):
            return '862.00'
        elif Columna.endswith('CUENTAS INCOBRABLES CASTIGADAS Y CONDONADAS'):
            return '865.00'
        elif Columna.endswith('PRODUCTOS EN SUSPENSO'):
            return '866.00'
        elif Columna.endswith('OPERACIONES A FUTURO DE MONEDA EXTRANJERA'):
            return '867.00'
        elif Columna.endswith('CUENTAS DEUDORAS DE LOS PATRIMONIOS AUTÓNOMOS CONSTITUIDOS CON RECURSOS PRIVADOS'):
            return '870.00'
        elif Columna.endswith('Activos de los patrimonios autónomos'):
            return '0.00'
        elif Columna.endswith('Gastos de los patrimonios autónomos'):
            return '0.00'
        elif Columna.endswith('CUENTAS DEUDORAS DE LOS PATRIMONIOS AUTÓNOMOS CONSTITUIDOS CON RECURSOS DEL ESTADO'):
            return '880.00'
        elif Columna.endswith('Activos de los patrimonios autónomos'):
            return '0.00'
        elif Columna.endswith('Gastos de los patrimonios autónomos'):
            return '0.00'
        elif Columna.endswith('(+) INGRESOS FINANCIEROS'):
            return '510.00'
        elif re.search(r'\bCambiado8\b', Columna):
            return '513.99'
        elif re.search(r'\bCambiado9\b', Columna):
            return '515.02'
        elif re.search(r'\bCambiado21\b', Columna):
            return '516.02'
        elif re.search(r'\bCambiado10\b', Columna):
            return '517.00'
        elif re.search(r'\bCambiado11\b', Columna):
            return '518.00'
        elif Columna.endswith('COMISIONES DE CARTERA Y CONTINGENTE'):
            return '519.00'
        elif Columna.endswith('(-) GASTOS FINANCIEROS'):
            return '410.00'
        elif Columna.endswith('CARGOS POR OTRAS CUENTAS POR PAGAR Y COMISIONES FINANCIERAS'):
            return '414.00'
        elif Columna.endswith('(=) RESULTADO FINANCIERO BRUTO'):
            return 'CC0.00'
        elif Columna.endswith('(+) OTROS INGRESOS OPERATIVOS'):
            return '540.00'
        elif Columna.endswith('GANANCIAS POR OPERACIONES DE CAMBIO Y ARBITRAJE'):
            return '542.00'
        elif Columna.endswith('INGRESOS POR INVERSIONES PERMANENTES NO FINANCIERAS'):
            return '544.00'
        elif Columna.endswith('INGRESOS OPERATIVOS DIVERSOS'):
            return '545.00'
        elif Columna.endswith('(-) OTROS GASTOS OPERATIVOS'):
            return '440.00'
        elif Columna.endswith('PÉRDIDAS POR INVERSIONES PERMANENTES NO FINANCIERAS'):
            return '443.00'
        elif Columna.endswith('DEPRECIACIÓN Y DESVALORIZACIÓN DE BIENES ALQUILADOS'):
            return '444.00'
        elif Columna.endswith('GASTOS OPERATIVOS DIVERSOS'):
            return '445.00'
        elif Columna.endswith('(=) RESULTADO DE OPERACIÓN BRUTO'):
            return 'CC0.01'
        elif Columna.endswith('(+) RECUPERACION DE ACTIVOS FINANCIEROS'):
            return '530.00'
        elif Columna.endswith('RECUPERACIONES DE ACTIVOS FINANCIEROS CASTIGADOS'):
            return '531.00'
        elif Columna.endswith('DISMIN.PREV. CART., PREV.GEN.EXC.LIM.CONS.NO DEB.GARANT., PREV. GEN.CÍCLICA Y OT.CTAS P/COB.'):
            return '532.00'
        elif Columna.endswith('DISMINUCIÓN DE PREVISIÓN PARA INVERSIONES PERMANENTES FINANCIERAS'):
            return '534.00'
        elif Columna.endswith('DISMINUCIÓN DE PREVISIÓN PARA FIDEICOMISOS'):
            return '537.00'
        elif Columna.endswith('(-) CARGOS POR INCOBRABILIDAD Y DESVALORIZACIÓN DE ACTIVOS FINANCIEROS'):
            return '430.00'
        elif Columna.endswith('PÉRD.P/INCOB.CRED., PREV. GEN.CÍCLICA, PREV.GEN.EXC.LIM.CONS.NO DEB.GARANT. Y OT.CTAS P/COB.'):
            return '431.00'
        elif Columna.endswith('PÉRDIDAS POR INVERSIONES PERMANENTES FINANCIERAS'):
            return '433.00'
        elif Columna.endswith('CASTIGO DE PRODUCTOS FINANCIEROS'):
            return '434.00'
        elif Columna.endswith('(=) RESULTADO DE OPERACIÓN DESPUÉS DE INCOBRABLES'):
            return 'CC0.02'
        elif Columna.endswith('(-) GASTOS DE ADMINISTRACIÓN'):
            return '450.00'
        elif Columna.endswith('GASTOS DE PERSONAL'):
            return '451.00'
        elif Columna.endswith('SERVICIOS CONTRATADOS'):
            return '452.00'
        elif Columna.endswith('SEGUROS'):
            return '453.00'
        elif Columna.endswith('COMUNICACIONES Y TRASLADOS'):
            return '454.00'
        elif Columna.endswith('IMPUESTOS'):
            return '455.00'
        elif Columna.endswith('MANTENIMIENTO Y REPARACIONES'):
            return '456.00'
        elif Columna.endswith('OTROS GASTOS DE ADMINISTRACIÓN'):
            return '459.00'
        elif Columna.endswith('(=) RESULTADO DE OPERACIÓN NETO'):
            return 'CC0.03'
        elif Columna.endswith('(+) ABONOS POR DIFERENCIA DE CAMBIO Y MANTENIMIENTO DE VALOR'):
            return '520.00 (96.00 + 95.00)'
        elif Columna.endswith('Abonos por diferencia de cambio'):
            return '96.00'
        elif Columna.endswith('Abonos por mantenimiento de valor'):
            return '95.00'
        elif Columna.endswith('(-) CARGOS POR DIFERENCIA DE CAMBIO Y MANTENIMIENTO DE VALOR'):
            return '420.00 (94.00 + 93.00)'
        elif Columna.endswith('Cargos por diferencia de cambio'):
            return '94.00'
        elif Columna.endswith('Cargos por mantenimiento de valor'):
            return '93.00'
        elif Columna.endswith('(=) RESULTADO DESPUES DE AJUSTE POR DIFERENCIA DE CAMBIO Y MANTENIMIENTO DE VALOR'):
            return 'CC0.04'
        elif Columna.endswith('(+/-) Ingresos (gastos) extraordinarios'):
            return '570.00'
        elif Columna.endswith('(=) RESULTADO NETO DEL EJERCICIO ANTES DE AJUSTES DE GESTIONES ANTERIORES'):                   
            return 'CC0.05'
        elif Columna.endswith('(+/-) Ingresos (gastos) de gestiones anteriores'):
            return '580.00'
        elif Columna.endswith('(=) RESULTADO ANTES DE IMPUESTOS Y AJUSTE CONTABLE POR EFECTO DE INFLACIÓN'):
            return 'CC0.06'
        elif Columna.endswith('(+/-) Ajuste contable por efecto de la inflación'):
            return '0.00'
        elif re.search(r'\bCambiado6\b', Columna):
            return 'CC0.08'
        elif Columna.endswith('(-) IMPUESTO SOBRE LAS UTILIDADES DE LAS EMPRESAS'):
            return '460.00'
        elif Columna.endswith('(=) RESULTADO NETO DE LA GESTIÓN'):
            return 'CC0.08 - 460.00'
        elif re.search(r'\bDOCUMENTOS DE COBRO INMEDIATO\b', Columna):
            return '117.00'
        elif re.search(r'\bObligaciones con bancos y otras entidades del país a plazo\b', Columna):
            return '235.00'
        elif re.search(r'\bObligaciones con bancos y otras entidades del país a plazo\b', Columna):
            return '235.00'
        elif re.search(r'\bPAGARÉS BURSÁTILES\b', Columna):
            return '263.00'
        elif re.search(r'\bBOLETAS DE GARANTÍA NO CONTRAGARANTIZADAS\b', Columna):
            return '623.00'
        elif re.search(r'\bGARANTÍAS TRANSFERIDAS PARA TITULARIZACIÓN\b', Columna):
            return '92.00'
        elif re.search(r'\bOPERACIONES DE COMPRA Y VENTA A FUTURO DE MONEDA EXTRANJERA\b', Columna):
            return '867.00'
        elif re.search(r'\bCUENTAS ACREEDORAS DE LOS PATRIMONIOS AUTÓNOMOS CONSTITUIDOS CON RECURSOS PRIVADOS\b', Columna):
            return '970.00'
        elif re.search(r'\bCUENTAS ACREEDORAS DE LOS PATRIMONIOS AUTÓNOMOS CONSTITUIDOS CON RECURSOS DEL ESTADO\b', Columna):
            return '980.00'
        elif re.search(r'\bPrevisiones por constituir sujetas a cronograma\b', Columna):
            return '869.90'
        elif re.search(r'\bESTADO DE GANANCIAS Y PÉRDIDAS\b', Columna):
            return '869.90'
        

    for name in range(len(excel_EF)):
        # Modificar los excels descargados INDICADORES
        excel2 = pd.read_excel(excel_EF[name], header=None)
        info = pd.DataFrame(excel2)
        pd.set_option('display.max_rows', None)

        #print (info)
        # Encontrar la columna que contiene la palabra "TOTAL SISTEMA"
        ultima_cols = info.columns[info.apply(lambda x: x.astype(str).str.contains('TOTAL SISTEMA')).any()]
        col_idx = info.columns.get_loc(ultima_cols[0])
        info = info.iloc[:, :col_idx+1]
        #print (info)

        if nowYear < 2020:
            tipo_indentidad = info.loc[1][0]
            if tipo_indentidad == 'BANCOS DE DESARROLLO PRODUCTIVO':
                info = info.replace('TOTAL SISTEMA', 'TSBDR')
            elif tipo_indentidad == 'BANCOS MÚLTIPLES':
                info = info.replace('TOTAL SISTEMA', 'TSBMU')
            elif tipo_indentidad == 'BANCOS PYME':
                info = info.replace('TOTAL SISTEMA', 'TSBPY')
            elif tipo_indentidad == 'COOPERATIVAS DE AHORRO Y CRÉDITO' or tipo_indentidad == 'COOPERATIVAS DE AHORRO Y CRÉDITO ABIERTAS':
                info = info.replace('TOTAL SISTEMA', 'TSCOO')
            elif tipo_indentidad == 'ENTIDADES FINANCIERAS DE VIVIENDA':
                info = info.replace('TOTAL SISTEMA', 'TSEFV')
            elif tipo_indentidad == 'INSTITUCIONES FINANCIERAS DE DESARROLLO':
                info = info.replace('TOTAL SISTEMA', 'TSIFD')
        else:
            tipo_indentidad = info.loc[0][0]
            if tipo_indentidad == 'BANCOS DE DESARROLLO PRODUCTIVO':
                info = info.replace('TOTAL SISTEMA', 'TSBDR')
            elif tipo_indentidad == 'BANCOS MÚLTIPLES':
                info = info.replace('TOTAL SISTEMA', 'TSBMU')
            elif tipo_indentidad == 'BANCOS PYME':
                info = info.replace('TOTAL SISTEMA', 'TSBPY')
            elif tipo_indentidad == 'COOPERATIVAS DE AHORRO Y CRÉDITO':
                info = info.replace('TOTAL SISTEMA', 'TSCOO')
            elif tipo_indentidad == 'ENTIDADES FINANCIERAS DE VIVIENDA':
                info = info.replace('TOTAL SISTEMA', 'TSEFV')
            elif tipo_indentidad == 'INSTITUCIONES FINANCIERAS DE DESARROLLO':
                info = info.replace('TOTAL SISTEMA', 'TSIFD')
            
        if nowYear < 2020:
            fecha_info = info.loc[3][0]
            split = fecha_info.split()
        else:
            fecha_info = info.loc[2][0]
            split = fecha_info.split()

        m = {
                'enero': "01",
                'febrero': "02",
                'marzo': "03",
                'abril': "04",
                'mayo': "05",
                'junio': "06",
                'julio': "07",
                'agosto': "08",
                'septiembre': "09",
                'octubre': "10",
                'noviembre': "11",
                'diciembre': "12"
            }

        out = str(m[split[3].lower()])
        fecha = split[5] + "-" +  out + "-" + split[1]

        #print (info)

        if nowYear < 2020:
            # Borror la basura de las 7 lineas
            info.drop([0,1,2,3,4,5,6], axis=0, inplace=True)
            info = info.reset_index(drop=True) # Reinicio de las filas y columnas
            info[0] = info[0].str.strip()
        else:
            # Borror la basura de las 4 lineas
            info = info.dropna(subset=[1])
            info = info.reset_index(drop=True) # Reinicio de las filas y columnas
            info[0] = info[0].str.strip()
        
        #print (info)
        
        num_columnas = info.shape[1] - 1

        info[0] = info[0].replace(r'\bACTIVO\b(?!\s*\+)', 'Dimension1', regex=True)
        info[0] = info[0].replace(r'\bPASIVO\b(?!\s*\+)', 'Dimension1.1', regex=True)
        info[0] = info[0].replace('PATRIMONIO', 'Dimension1.1.1')
        info[0] = info[0].replace('PASIVO + PATRIMONIO', 'Dimension1.1.1.1')
        info[0] = info[0].replace('CUENTAS CONTINGENTES DEUDORAS', 'Dimension1.1.1.1.1')
        info[0] = info[0].replace('CUENTAS DE ORDEN DEUDORAS', 'Dimension1.1.1.1.1.1')
        info[0] = info[0].replace('(+) INGRESOS FINANCIEROS', 'Dimension1.1.1.1.1.1.1')

        #print (info)

        # inicializar variables
        group = None
        groups = []

        # iterar sobre cada fila del dataframe
        for i, row in info.iterrows():
            # si la primera columna no es nula y es una palabra completa que contiene alguna de las palabras buscadas, entonces es un nuevo grupo
            if not pd.isnull(row[0]) and any(s.lower() == w.lower() for w in row[0].split() for s in ['Dimension1', 'Dimension1.1', 'Dimension1.1.1','Dimension1.1.1.1','Dimension1.1.1.1.1','Dimension1.1.1.1.1.1','Dimension1.1.1.1.1.1.1']):
                group = row[0]

            # agregar el grupo actual a la lista de grupos
            groups.append(group)

        # agregar la columna de grupos al dataframe
        info['Group'] = groups
        #print (info)
        #info[0,'Group'] = info[0,'Group'].replace(r'\bACTIVO\b(?!\s*\+)', 'Dimension1', regex=True)
        #info[0,'Group'] = info[0,'Group'].replace(r'\bPASIVO\b(?!\s*\+)', 'Dimension1.1', regex=True)
        info['Group'] = info['Group'].replace('Dimension1', 'ACTIVO')
        info[0] = info[0].replace('Dimension1', 'ACTIVO')
        info['Group'] = info['Group'].replace('Dimension1.1', 'PASIVO')
        info[0] = info[0].replace('Dimension1.1', 'PASIVO')
        info['Group'] = info['Group'].replace('Dimension1.1.1', 'PATRIMONIO')
        info[0] = info[0].replace('Dimension1.1.1', 'PATRIMONIO')
        info['Group'] = info['Group'].replace('Dimension1.1.1.1', 'PASIVO + PATRIMONIO')
        info[0] = info[0].replace('Dimension1.1.1.1', 'PASIVO + PATRIMONIO')
        info['Group'] = info['Group'].replace('Dimension1.1.1.1.1', 'CUENTAS CONTINGENTES DEUDORAS')
        info[0] = info[0].replace('Dimension1.1.1.1.1', 'CUENTAS CONTINGENTES DEUDORAS')
        info['Group'] = info['Group'].replace('Dimension1.1.1.1.1.1', 'CUENTAS DE ORDEN DEUDORAS')
        info[0] = info[0].replace('Dimension1.1.1.1.1.1', 'CUENTAS DE ORDEN DEUDORAS')
        info['Group'] = info['Group'].replace('Dimension1.1.1.1.1.1.1', 'ESTADO DE RESULTADO')
        info[0] = info[0].replace('Dimension1.1.1.1.1.1.1', '(+) INGRESOS FINANCIEROS')
        info[0] = info[0].replace({'\s+': ' '}, regex=True).str.strip()
        info = info.replace('"', '', regex=True)

        #print (info)
        info_estados = info.loc[:, [0, 'Group']]
        info_estados = info_estados.dropna(subset=[0])
        #print (info_estados)
        #Modificando los nombres para poner los codigos
        info_estados.iloc[:50, info_estados.columns.get_loc(0)] = info_estados.iloc[:50, info_estados.columns.get_loc(0)].replace('INVERSIONES EN EL BANCO CENTRAL DE BOLIVIA', 'Cambiado')
        info_estados.iloc[:70, info_estados.columns.get_loc(0)] = info_estados.iloc[:70, info_estados.columns.get_loc(0)].replace('DIVERSAS', 'Cambiado2')
        info_estados[0] = info_estados[0].replace('CUENTAS DE REGISTRO DIVERSAS', 'Cambiado3')
        info_estados[0] = info_estados[0].replace('DISMINUCIÓN DE PREVISIÓN PARA DISPONIBILIDADES', 'Cambiado4')
        info_estados[0] = info_estados[0].replace('DISMINUCIÓN DE PREVISIÓN PARA PARTIDAS PENDIENTES DE IMPUTACIÓN', 'Cambiado5')
        info_estados[0] = info_estados[0].replace('(=) RESULTADO ANTES DE IMPUESTOS', 'Cambiado6')
        info_estados[0] = info_estados[0].replace('PÉRDIDAS POR PARTIDAS PENDIENTES DE IMPUTACIÓN', 'Cambiado7')
        info_estados[0] = info_estados[0].replace('PRODUCTOS DE CARTERA VIGENTE REPROGRAMADA O REESTRUCTURADA', 'Cambiado8')
        info_estados[0] = info_estados[0].replace('PRODUCTOS DE CARTERA VENCIDA REPROGRAMADA O REESTRUCTURADA', 'Cambiado9')
        info_estados[0] = info_estados[0].replace('PRODUCTOS POR OTRAS CUENTAS POR COBRAR', 'Cambiado10')
        info_estados[0] = info_estados[0].replace('PRODUCTOS POR INVERSIONES PERMANENTES FINANCIERAS', 'Cambiado11')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('INVERSIONES EN ENTIDADES FINANCIERAS DEL PAÍS', 'Cambiado12')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('INVERSIONES EN ENTIDADES FINANCIERAS DEL EXTERIOR', 'Cambiado13')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('INVERSIONES EN ENTIDADES PÚBLICAS NO FINANCIERAS DEL PAÍS', 'Cambiado14')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('INVERSIONES EN OTRAS ENTIDADES NO FINANCIERAS', 'Cambiado15')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('INVERSIONES DE DISPONIBILIDAD RESTRINGIDA', 'Cambiado16')
        info_estados[0] = info_estados[0].replace('(PREVISIÓN PARA OTRAS CUENTAS POR COBRAR)', 'Cambiado17')
        info_estados[0] = info_estados[0].replace('PARTIDAS PENDIENTES DE IMPUTACIÓN', 'Cambiado18')
        info_estados[0] = info_estados[0].replace('(PREVISIÓN PARA PARTIDAS PENDIENTES DE IMPUTACIÓN)', 'Cambiado19')
        info_estados[0] = info_estados[0].replace('PRODUCTOS DE CARTERA EN EJECUCIÓN', 'Cambiado20')
        info_estados[0] = info_estados[0].replace('PRODUCTOS DE CARTERA EN EJECUCIÓN REPROGRAMADA O REESTRUCTURADA', 'Cambiado21')

        #print (info_estados)
        # Esto seria para reparar los error que existen en sintaxis o espacios que se olvidan en la cuenta
        if nowYear <= 2022:
            info_estados[0] = info_estados[0].replace('(=)RESULTADO NETO DE LA GESTIÓN', '(=) RESULTADO NETO DE LA GESTIÓN')
            info_estados[0] = info_estados[0].replace('(=)RESULTADO ANTES DE IMPTOS. Y AJUSTE CONTABLE POR EFECTO DE INFLACIÓN', '(=) RESULTADO ANTES DE IMPUESTOS Y AJUSTE CONTABLE POR EFECTO DE INFLACIÓN')
            info_estados[0] = info_estados[0].replace('(=)RESULTADO NETO DEL EJERCICIO ANTES DE AJUSTES DE GESTIONES ANTERIORES', '(=) RESULTADO NETO DEL EJERCICIO ANTES DE AJUSTES DE GESTIONES ANTERIORES')
            info_estados[0] = info_estados[0].replace('(=)RESULTADO DESPUES DE AJUSTE POR DIF. DE CAMBIO Y MANTENIM. DE VALOR', '(=) RESULTADO DESPUES DE AJUSTE POR DIFERENCIA DE CAMBIO Y MANTENIMIENTO DE VALOR')
            info_estados[0] = info_estados[0].replace('(=)RESULTADO DE OPERACIÓN NETO', '(=) RESULTADO DE OPERACIÓN NETO')
            info_estados[0] = info_estados[0].replace('(=)RESULTADO DE OPERACIÓN DESPUÉS DE INCOBRABLES', '(=) RESULTADO DE OPERACIÓN DESPUÉS DE INCOBRABLES')
            info_estados[0] = info_estados[0].replace('PÉRDIDAS POR DISPONIBILIDAD', 'PÉRDIDAS POR DISPONIBILIDADES')
            info_estados[0] = info_estados[0].replace('(=)RESULTADO DE OPERACIÓN BRUTO', '(=) RESULTADO DE OPERACIÓN BRUTO')
            info_estados[0] = info_estados[0].replace('(=)RESULTADO FINANCIERO BRUTO', '(=) RESULTADO FINANCIERO BRUTO')
            info_estados[0] = info_estados[0].replace('Depositos a plazo fijo mayor a 720 a 1.080 días', 'Depósitos a plazo fijo de 721 a 1.080 días')
            info_estados[0] = info_estados[0].replace('Depositos a plazo fijo mayor a 1.080 días', 'Depósitos a plazo fijo mayor a 1.080 días')
            info_estados[0] = info_estados[0].replace('RENDIMIENTOS POR COBRAR POR FIDEICOMISOS)', 'RENDIMIENTOS POR COBRAR POR FIDEICOMISOS')
            info_estados[0] = info_estados[0].replace('(Previsión especifica para incobrabilidad de cartera reprogramada o reestructurada vigente)', '(Previsión específica para incobrabilidad de cartera reprogramada o reestructurada vigente)')
            info_estados[0] = info_estados[0].replace('(Previsión especifica para incobrabilidad de cartera reprogramada o reestructurada vencida)', '(Previsión específica para incobrabilidad de cartera reprogramada o reestructurada vencida)')
            info_estados[0] = info_estados[0].replace('(=) RESULTADO DESPUES DE AJUSTE POR DIF. DE CAMBIO Y MANTENIM. DE VALOR', '(=) RESULTADO DESPUES DE AJUSTE POR DIFERENCIA DE CAMBIO Y MANTENIMIENTO DE VALOR')
            info_estados[0] = info_estados[0].replace('(=) RESULTADO ANTES DE IMPTOS. Y AJUSTE CONTABLE POR EFECTO DE INFLACIÓN', '(=) RESULTADO ANTES DE IMPUESTOS Y AJUSTE CONTABLE POR EFECTO DE INFLACIÓN')

        #print (info_estados)
        #Aplicamos los codigos a las Cuentas
        info_estados['Código'] = info_estados.apply(assign_code, axis=1)

        #Modificando los nombres volver normal
        info_estados.iloc[:50, info_estados.columns.get_loc(0)] = info_estados.iloc[:50, info_estados.columns.get_loc(0)].replace('Cambiado', 'INVERSIONES EN EL BANCO CENTRAL DE BOLIVIA')
        info_estados.iloc[:70, info_estados.columns.get_loc(0)] = info_estados.iloc[:70, info_estados.columns.get_loc(0)].replace('Cambiado2', 'DIVERSAS')
        info_estados[0] = info_estados[0].replace('Cambiado3', 'CUENTAS DE REGISTRO DIVERSAS')
        info_estados[0] = info_estados[0].replace('Cambiado4', 'DISMINUCIÓN DE PREVISIÓN PARA DISPONIBILIDADES')
        info_estados[0] = info_estados[0].replace('Cambiado5', 'DISMINUCIÓN DE PREVISIÓN PARA PARTIDAS PENDIENTES DE IMPUTACIÓN')
        info_estados[0] = info_estados[0].replace('Cambiado6', '(=) RESULTADO ANTES DE IMPUESTOS')
        info_estados[0] = info_estados[0].replace('Cambiado7', 'PÉRDIDAS POR PARTIDAS PENDIENTES DE IMPUTACIÓN')
        info_estados[0] = info_estados[0].replace('Cambiado8', 'PRODUCTOS DE CARTERA VIGENTE REPROGRAMADA O REESTRUCTURADA')
        info_estados[0] = info_estados[0].replace('Cambiado9', 'PRODUCTOS DE CARTERA VENCIDA REPROGRAMADA O REESTRUCTURADA')
        info_estados[0] = info_estados[0].replace('Cambiado10', 'PRODUCTOS POR OTRAS CUENTAS POR COBRAR')
        info_estados[0] = info_estados[0].replace('Cambiado11', 'PRODUCTOS POR INVERSIONES PERMANENTES FINANCIERAS')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('Cambiado12', 'INVERSIONES EN ENTIDADES FINANCIERAS DEL PAÍS')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('Cambiado13', 'INVERSIONES EN ENTIDADES FINANCIERAS DEL EXTERIOR')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('Cambiado14', 'INVERSIONES EN ENTIDADES PÚBLICAS NO FINANCIERAS DEL PAÍS')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('Cambiado15', 'INVERSIONES EN OTRAS ENTIDADES NO FINANCIERAS')
        info_estados.iloc[:25, info_estados.columns.get_loc(0)] = info_estados.iloc[:25, info_estados.columns.get_loc(0)].replace('Cambiado16', 'INVERSIONES DE DISPONIBILIDAD RESTRINGIDA')
        info_estados[0] = info_estados[0].replace('Cambiado17', '(PREVISIÓN PARA OTRAS CUENTAS POR COBRAR)')
        info_estados[0] = info_estados[0].replace('Cambiado18', 'PARTIDAS PENDIENTES DE IMPUTACIÓN')
        info_estados[0] = info_estados[0].replace('Cambiado19', '(PREVISIÓN PARA PARTIDAS PENDIENTES DE IMPUTACIÓN)')
        info_estados[0] = info_estados[0].replace('Cambiado20', 'PRODUCTOS DE CARTERA EN EJECUCIÓN')
        info_estados[0] = info_estados[0].replace('Cambiado21', 'PRODUCTOS DE CARTERA EN EJECUCIÓN REPROGRAMADA O REESTRUCTURADA')
        #print (info_estados)

        palabra_buscar = "ESTADO DE SITUACIÓN PATRIMONIAL"

        if palabra_buscar in info_estados.iloc[0, 0]:
            info_estados = info_estados.drop(info_estados.index[0])
            info_estados = info_estados.reset_index(drop=True) # Reinicio de las filas y columnas

        #Multiplicamos la tabla deacuerdo a las columnas o las entidas que se tenga
        info_estados_final = pd.concat([info_estados] * num_columnas, ignore_index=True)

        # Agregar datos iniciales al dataframe
        datos_EF[['Dimension 1', 'Código', 'Cuenta']] = info_estados_final.loc[:, ['Group', 'Código',0]]
        info = info.drop([0, 'Group'], axis=1).reset_index(drop=True)
        info = info.reset_index(drop=True) # Reinicio de las filas y columnas
        info.columns = info.iloc[0]
        info = info.drop(0)
        info = info.reset_index().melt(id_vars='index')
        info.columns = ['Index', 'Institución', 'Valores']
        info = info.drop('Index', axis=1)
        datos_EF[['Institución', 'Valor']] = info.loc[:, ['Institución','Valores']]

        # Llenar las columnas Fecha y Tipo de Institución con las variables fecha y tipo, respectivamente
        datos_EF['Fecha'] = fecha
        datos_EF['Tipo de Institucion'] = tipo_indentidad
        datos_EF['Nombre del Archivo'] = excel_EF[name]

        #print (datos_EF)
        datos_EF['Valor'] = pd.to_numeric(datos_EF['Valor'], errors='coerce')
        datos_EF['Valor'] = datos_EF['Valor'].round(4)
        #print (datos_EF)

        # crear un objeto ExcelWriter
        writer = pd.ExcelWriter(excel_EF[name], engine='xlsxwriter')

        # escribir el DataFrame en una hoja llamada 'Datos'
        datos_EF.to_excel(writer, sheet_name='Datos', index=False)

        # guardar los cambios
        writer.save()
        writer.close()
        datos_EF.drop(index=datos_EF.index, inplace=True)
        info.drop(index=info.index, inplace=True)

    # Configuración de la conexión a MySQL
    engine = create_engine('mysql+mysqlconnector://root:Hels1962*@localhost/Datos') 

    # Nombre del archivo de texto para guardar los nombres de los archivos ya subidos a MySQL
    archivo_subidos = "subidos.txt"
    if not os.path.exists(archivo_subidos):
        with open(archivo_subidos, 'w') as archivo:
            archivo.write('')

    # Ciclo para subir datos de excel_EF a MySQL
    for archivo in excel_EF: 
        # Verificar si el nombre del archivo ya ha sido subido previamente
        nombre_archivo = os.path.basename(archivo)
        if nombre_archivo not in open(archivo_subidos).read():
            # Leer el archivo de Excel en un DataFrame de Pandas
            df = pd.read_excel(archivo, sheet_name='Datos')
    
            # Escribir el DataFrame en la base de datos
            df.to_sql(name='estados_financieros', con=engine, if_exists='append', index=False)
            # Agregar nombre del archivo al archivo de texto
            with open(archivo_subidos, 'a') as archivo:
                archivo.write(nombre_archivo + '\n')

    # Ciclo para subir datos de excel_I a MySQL
    for archivo in excel_I: 
        # Verificar si el nombre del archivo ya ha sido subido previamente
        nombre_archivo = os.path.basename(archivo)
        if nombre_archivo not in open(archivo_subidos).read():
            # Leer el archivo de Excel en un DataFrame de Pandas
            df = pd.read_excel(archivo, sheet_name='Datos')
    
            # Escribir el DataFrame en la base de datos
            df.to_sql(name='indicadores_financieros', con=engine, if_exists='append', index=False)
            # Agregar nombre del archivo al archivo de texto
            with open(archivo_subidos, 'a') as archivo:
                archivo.write(nombre_archivo + '\n')

    # Cerrar la conexión
    engine.dispose()

    # eliminar archivos en excel_I
    for archivo in excel_I:
        os.remove(archivo)

    # eliminar archivos en excel_EF
    for archivo in excel_EF:
        os.remove(archivo)
    
    print ("TERMINE!")