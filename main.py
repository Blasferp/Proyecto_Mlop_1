from fastapi import FastAPI
import pandas as pd 
import pyarrow.parquet as pq
import joblib

app = FastAPI()


@app.get("/Genero_por_Año/")
def PlayTimeGenre(genero:str):
    # Verificar si el género es una cadena (str)
    if not isinstance(genero, str):
        return {"Por favor, debe ingresar una palabra para el genero"}

    # Convertir el género a minúsculas para realizar la comparación de manera insensible a mayúsculas
    genero = genero.lower()

    # Carga del DataFrame en un variable
    endpoint_1 = pd.read_parquet('Data/endpoint_1.parquet')
    
    # Filtrar el DataFrame por el género dado
    df_filtro = endpoint_1[endpoint_1['Generos'] == genero]

    # Asegurar que tenga en cuenta si no hay datos para el género ingresado
    if df_filtro.empty:
        return {f'No hay datos para el género {genero}, intente nuevamente'}

    # Agrupar por año de lanzamiento y sumar las horas jugadas
    df_grouped = df_filtro.groupby('Año_Lanzamiento')['Tiempo_Jugado'].agg(['sum'])

    # Encontrar el año con más horas jugadas
    año_con_mas_horas = df_grouped['sum'].idxmax()

    # Obtener la cantidad total de horas jugadas para el año con más horas jugadas
    horas_totales = df_grouped.loc[año_con_mas_horas, 'sum']

    resultado = {
        f"Año de lanzamiento con más horas jugadas para {genero}: {año_con_mas_horas}"
    }

    return resultado

@app.get("/Usuario_por_Genero/")
def UserForGenre(genero: str):
    # Verificar si el género es una cadena (str)
    if not isinstance(genero, str):
        return {"Por favor, debe ingresar una palabra para el genero"}
    
    # Convertir el género a minúsculas
    genero = genero.lower()

    # Carga del DataFrame en un variable
    endpoint_2 = pd.read_parquet('Data/endpoint_2.parquet')

    # Filtrar el DataFrame por el género dado
    df_filtro = endpoint_2[endpoint_2['Generos'] == genero]

    if df_filtro.empty:
        return {f'No hay datos para el género {genero}, intente nuevamente'}

    # Calcular la suma del tiempo jugado por usuario y año
    df_agregado = df_filtro.groupby(['Id_Usuario', 'Año_Lanzamiento'])['Tiempo_Jugado'].sum().reset_index()

    # Encontrar al usuario con más horas jugadas
    usuario_max_tiempo = df_agregado.groupby('Id_Usuario')['Tiempo_Jugado'].sum().idxmax()

    # Filtrar el DataFrame para obtener solo las filas del usuario con más tiempo jugado
    df_usuario_max_tiempo = df_agregado[df_agregado['Id_Usuario'] == usuario_max_tiempo]

    # Crear una lista de diccionarios con la acumulación de horas jugadas por año
    acumulacion_horas = [{"Año": int(anio), "Horas": int(horas)} for anio, horas in zip(df_usuario_max_tiempo['Año_Lanzamiento'], df_usuario_max_tiempo['Tiempo_Jugado'])]

    # Crear el diccionario de retorno
    retorno = {"Usuario con más horas jugadas para Género X": usuario_max_tiempo, "Horas jugadas": acumulacion_horas}

    return retorno

@app.get("/Usuario_Recomendacion/")
def UsersRecommend(año: int):

    # Verificar si el año es un entero
    if not isinstance(año, int):
        return {f'El valor ingresado para el año ({año}) no es un número entero. Intente nuevamente.'}
    
    # Carga del DataFrame en un variable
    endpoint_3 = pd.read_parquet('Data/endpoint_3.parquet')

    # Filtro por el año de búsqueda
    df_filtro = endpoint_3[(endpoint_3['Año_Posteo'] == año)]

    # Verificar si el DataFrame resultante está vacío
    if df_filtro.empty:
        return {f'No hay datos para el año {año}. Intente nuevamente.'}

    # Filtrar por recomendaciones y análisis de sentimientos específicos
    df_filtro_2 = df_filtro[(df_filtro['Recomendado'] == 'true') & (df_filtro['Analisis_sentimientos'].isin([1, 2]))]

    # Agrupa por 'titulo' y cuenta la cantidad de recomendaciones
    df_group_by = df_filtro_2.groupby('Titulo').agg({'Recomendado': 'sum'}).reset_index()

    # Ordena en orden descendente por la cantidad de recomendaciones y toma el top 3
    top_3_juegos_recomendados = df_group_by.sort_values(by='Recomendado', ascending=False).head(3).reset_index(drop=True)

    # Formatea el resultado de manera más simple
    resultado_formateado = [{"Puesto " + str(i + 1): top_3_juegos_recomendados.loc[i, 'Titulo']} for i in range(len(top_3_juegos_recomendados))]
    # Retorna el resultado formateado
    return resultado_formateado

@app.get("/Dearrollador_menos_recomendado/")
def UsersWorstDeveloper(año):
    # Verificar si el año es un entero
    if not isinstance(año, int):
        return {f'El valor ingresado para el año ({año}) no es un número entero. Intente nuevamente.'}

    # Carga del DataFrame en un variable
    endpoint_4 = pd.read_parquet('Data/endpoint_4.parquet')

    # Filtro por el año de búsqueda
    df_filtro = endpoint_4[(endpoint_4['Año_Posteo'] == año)]

    # Verificar si el DataFrame resultante está vacío
    if df_filtro.empty:
        return {f'No hay datos para el año {año}. Intente nuevamente.'}

    # Filtrar por recomendaciones y análisis de sentimientos específicos
    df_filtro_2 = df_filtro[(df_filtro['Recomendado'] == 'false') & (df_filtro['Analisis_sentimientos'].isin([0]))]

    # Agrupa por 'titulo' y cuenta la cantidad de recomendaciones
    df_group_by = df_filtro.groupby('Desarrollador').agg({'Recomendado': 'sum'}).reset_index()

    # Ordena en orden descendente por la cantidad de recomendaciones y toma el top 3
    top_3_juegos_recomendados = df_group_by.sort_values(by='Recomendado', ascending=False).head(3).reset_index(drop=True)

    # Formatea el resultado de manera más simple
    resultado_formateado = [{"Puesto " + str(i + 1): top_3_juegos_recomendados.loc[i, 'Desarrollador']} for i in range(len(top_3_juegos_recomendados))]

    # Retorna el resultado formateado
    return resultado_formateado

@app.get("/Desarrollador_Sentimiento/")
def sentiment_analysis(empresa_desarrolladora: str):
    # Verificar si el nombre de la empresa desarrolladora es una cadena
    if not isinstance(empresa_desarrolladora, str):
        return {f'El nombre de la empresa desarrolladora ({empresa_desarrolladora}) no es una cadena de caracteres. Intente nuevamente.'}
    
    # Carga del DataFrame en un variable
    endpoint_5 = pd.read_parquet('Data/endpoint_5.parquet')
    
    # Convertir el género a minúsculas
    empresa_desarrolladora = empresa_desarrolladora.lower()

    # Filtro por la empresa desarrolladora
    df_filtro = endpoint_5[endpoint_5['Desarrollador'] == empresa_desarrolladora]

    # Verificar si el DataFrame resultante está vacío
    if df_filtro.empty:
        return {f'No hay datos para la empresa desarrolladora {empresa_desarrolladora}. Intente nuevamente.'}

    # Realizar el análisis de sentimientos y contar la cantidad de registros para cada categoría
    sentiment_counts = df_filtro['Sentimiento'].value_counts().to_dict()

    # Formatear el resultado como un diccionario
    resultado_formateado = {empresa_desarrolladora: sentiment_counts}

    # Retorna el resultado formateado
    return resultado_formateado

@app.get("/Recomenadcion_Item_Item/")
def recomendacion(titulo:str):
    # Cargar el modelo entrenado desde el archivo pickle
    with open('data/Matriz.pkl', 'rb') as file:
        modelo = joblib.load(file)

    # Carga del DataFrame en un variable
    data_reducido = pd.read_parquet('Data/recomentadion_item_item.parquet')

    if titulo not in data_reducido['app_name'].tolist():
        return {"Respuesta": "No se encontraron resultados para la búsqueda realizada"}

    def get_recommendations(titulo, cosine_sim=modelo ):
    
        # Encuentra el índice del juego con el título proporcionado en el DataFrame 'data_reducido'
        idx = data_reducido[data_reducido['Titulo'] == titulo].index[0]
        
        # Calcula la similitud coseno entre el juego seleccionado y todos los demás juegos    
        sim_scores = list(enumerate(modelo[idx]))
        
        # Ordena los juegos según su similitud coseno en orden descendente
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Selecciona los 5 juegos más similares (excluyendo el juego en sí)    
        sim_scores = sim_scores[1:6]  
        
        # Obtiene los índices de los juegos seleccionados    
        game_indices = [i[0] for i in sim_scores]
        
        # Retorna los títulos de los juegos recomendados
        return data_reducido['Titulo'].iloc[game_indices]

    recommendations = get_recommendations(titulo)

    dicc = recommendations.to_dict()

    return dicc

@app.get("/Recomenadcion_Item_Usuario/")
def obtener_informacion_por_genero(genero: str):