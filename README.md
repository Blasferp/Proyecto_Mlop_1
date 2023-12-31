# Machine Learning Operations:
 ### Análisis de Datos y Recomendacion de juegos de la Plataforma Steam

![Precios por fechas](Image/Steam.png)

# Índice

1. [Análisis de Datos y Recomendacion de juegos de la Plataforma Steam](#an%C3%A1lisis-de-datos-y-predicci%C3%B3n-de-precios-de-juegos-de-steam)
2. [Requisitos](#requisitos)
3. [Modo de uso](#modo-de-uso)
4. [Notas](#notas)
5. [Contacto](#contacto)
6. [Tecnologías utilizadas](#tecnolog%C3%ADas-utilizadas)

Este repositorio contiene funciones y un modelo para un sistema de recomendación para juegos de la plataforma Steam. Además, incluye la creación de una API REST utilizando FastAPI para acceder a los Endpoints y al sistema de recomendacion, La construcción de la API y la implementación del modelo se llevan a cabo en un entorno Render.



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

2. Asegúrate de tener los siguientes archivos de datos disponibles en la carpeta `Data/` en el directorio del proyecto:

3. Ejecuta el archivo `main.py` para iniciar el servidor FastAPI:

```
python main.py
```

4. Una vez que el servidor esté en funcionamiento, puedes acceder a las siguientes rutas en tu navegador o cliente de API (por ejemplo, Postman):

- `/Genero_por_Año`: Devuelve el año con más horas jugadas del género ingresado.
- `/Usuario_por_Genero`: Devuelve el usuario que acumula mas horas jugadas, con las horas por cada año para el genero ingresado.
- `/Usuario_Recomendacion`: Devuelve el top 3 de juegos mas recomendados por usuarios para el año ingresado.
- `/Dearrollador_menos_recomendado`: Devuelve el top 3 de desarrolladoras con juegos menos recomendados por usuarios para el año ingresado.
- `/Desarrollador_Sentimiento`: Devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo, neutro o negativo.
- `/Recomenadcion_Item_Item`: Ingresando el ID_Item de un usuario, Devuelve una lista con 5 juegos recomendados para dicho Item.

## Notas

El Sistma de recomendacion utiliza un modelo que  tiene una relación ítem-ítem donde el input es el Id_Item y el output es una lista de  5 juegos recomendados(con sus respectivos nombres e Id_Item), para ello se aplico la similitud del coseno. Tenga en cuenta que se dismunuyo el tamaño de la Matriz (por lo que se selecciono 5000 items al azar), debido al tamaño que posee, genera inconvenientes en el deployement  .

## Contacto

### Blas Fernando Pacios

[![LinkedIn](Image/icons8-linkedin-48.png)](https://www.linkedin.com/in/blas-fernando-pacios-14a46a280/) [![WhatsApp](Image/icons8-whatsapp-48.png)](https://wa.me/5493815467488)

## Tecnologías utilizadas

Python | Pandas | Matplotlib | Scikit-Learn | FastAPI | Render

---