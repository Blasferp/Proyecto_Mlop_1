# Machine Learning Operations:
 ### Análisis de Datos y Rcomendacion de juegos de la Plataforma Steam

![Precios por fechas](steam.jpg)

# Índice

1. [Análisis de Datos y Rcomendacion de juegos de la Plataforma Steam](#an%C3%A1lisis-de-datos-y-predicci%C3%B3n-de-precios-de-juegos-de-steam)
2. [Requisitos](#requisitos)
3. [Modo de uso](#modo-de-uso)
4. [Notas](#notas)
5. [Tecnologías utilizadas](#tecnolog%C3%ADas-utilizadas)

Este repositorio contiene funciones y un modelo para un sistema de recomendación para recomendar juegos de la plataforma Steam. Además, incluye la creación de una API REST utilizando FastAPI para acceder a las funciones y al sistema de recomendacion, La construcción de la API y la implementación del modelo se llevan a cabo en un entorno Render.



## Requisitos

Asegúrate de tener Python 3.x instalado y las siguientes bibliotecas requeridas:

- pandas
- scikit-learn
- fastapi
- numpy

Puedes instalar las dependencias con el siguiente comando:

```
pip install pandas scikit-learn fastapi numpy
```

## Modo de uso

1. Clona este repositorio en tu sistema local.

2. Asegúrate de tener los siguientes archivos de datos disponibles en la carpeta `data/` en el directorio del proyecto:

3. Ejecuta el archivo `main.py` para iniciar el servidor FastAPI:

```
python main.py
```

4. Una vez que el servidor esté en funcionamiento, puedes acceder a las siguientes rutas en tu navegador o cliente de API (por ejemplo, Postman):

- `/developer`: Cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.
- `/userdata`: Debe devolver cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a reviews.recommend y cantidad de items.
- `/UserForGenre`: Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.
- `/best_developer_year`: Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado.
- `/developer_reviews_analysis`: Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.
- `/recomendacion_juego`: Ingresando el id de un usuario, deberíamos recibir una lista con 5 juegos recomendados para dicho usuario.

## Notas

El Sistma de recomendacion utiliza un modelo que  tiene una relación ítem-ítemde el input es un juego y el output es una lista de juegos recomendados, para ello se aplico la similitud del cosenoregresión. Tenga en cuenta que se dimunuyo el tamaño de lla Matriz, debido a que era de un tamaño que no permitia subirse a github. por lo que se selecciono las filas un numero menor de filas al azar .

## Contacto



## Tecnologías utilizadas

Python | Pandas | Matplotlib | Scikit-Learn | FastAPI | Render

---