import sqlite3
import pandas as pd
from itertools import combinations


#hacemos la conexión a la base de datos
conexion = sqlite3.connect('sanoyfresco.db')

#leemos la tabla tickets
df = pd.read_sql_query('SELECT * FROM tickets', conexion)

# Mostramos las primeras filas del DataFrame
print(df.head())

# cerramos la conexión a la base de datos
conexion.close()

# Mostramos información general del DataFrame
df.info()
# Convertimos la columna 'fecha' a tipo datetime
df['fecha']=pd.to_datetime(df['fecha'])

# Hacemos un mini dataframe con las colunmas que nos interesan
df_cesta = df[['id_pedido', 'nombre_producto']]
print(df_cesta.head())
# Agrupamos por id_pedido y unimos los productos en una sola cadena
df_agrupado =  df_cesta.groupby('id_pedido')['nombre_producto'].apply(lambda productos: ', '.join(productos))

print(df_agrupado.head())

# tranformamos la serie en un DataFrame con variables dummy
# esto nos permite tener una columna por cada producto si  tiene un 1  si lo ha comprado y 0 si no
df_transacciones = df_agrupado.str.get_dummies(sep=', ')
print(df_transacciones.head())

# hacemos el soporte de cada producto
#sacamos la media de cada columna y multiplicamos por 100 para tener el porcentaje
soporte = df_transacciones.mean()*100
soporte.sort_values(ascending=False)
print(soporte.head(10))

# Funcion para calcular la confianza
def confianza(antecedente, consecuente):

    # conjunto_ab es la frecuencia de compra de ambos productos y filtro para quedarme solo con las transacciones que tienen ambos productos
    conjunto_ab = df_transacciones[(df_transacciones[antecedente]==1) & (df_transacciones[consecuente]==1)]
    # el len me dira cuantas veces aparacen en total el conjunto_ab y luego se sumo en el denominador por que tenemos un DataFrame con variables dummy
    return len(conjunto_ab) / df_transacciones[antecedente].sum()

# Funcion para calcular el lift
def lift(antecedente, consecuente):
    soporte_a= df_transacciones[antecedente].mean()
    soporte_b= df_transacciones[consecuente].mean()
    conteo_ab = len(df_transacciones[(df_transacciones[antecedente] == 1) & (df_transacciones[consecuente] ==1)])
    soporte_ab = conteo_ab / len(df_transacciones)
    return soporte_ab / (soporte_a * soporte_b)

#definimos el umbral de confianza minima

umbral_confianza = 0.05
asociaciones = []

for antecedente, consecuente in combinations(df_transacciones.columns, 2):

    # soporte del antecedente
    soporte_a = df_transacciones[antecedente].mean()
   
   # calculamos la confianza
    conf = confianza(antecedente, consecuente)
    if conf >= umbral_confianza:
        asociaciones.append({
            'antecedente': antecedente,
            'consecuente': consecuente,
            'soporte_a': round(soporte_a * 100, 1),
            'confianza': round(conf * 100, 1),
            'lift': round(lift(antecedente, consecuente), 1)})
        
# Convertimos las asociaciones a un DataFrame        
df_asociaciones = pd.DataFrame(asociaciones)
# ordenamos las asociaciones por lift de forma descendente
df_asociaciones.sort_values(by='lift', ascending=False, inplace=True)
print(df_asociaciones.head(10))

productos_unicos = df[['id_producto', 'id_seccion', 'id_departamento','nombre_producto']].drop_duplicates()

df_asociaciones_total = df_asociaciones.merge(productos_unicos, left_on='antecedente', right_on='nombre_producto', how='left').drop(columns='nombre_producto')
df_asociaciones_total.columns = ['antecedente', 'consecuente', 'soporte_a', 'confianza', 'lift', 'id_producto', 'id_seccion', 'id_departamento']
print(df_asociaciones_total.head(10))

# Guardamos el DataFrame de asociaciones en un archivo CSV
df_asociaciones_total.to_csv('asociaciones.csv', index=False, sep=';', decimal=',')