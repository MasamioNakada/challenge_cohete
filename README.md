# Challenge Data Analytics - Python 

![](https://i0.wp.com/evemuseografia.com/wp-content/uploads/2019/07/EVE31072019B.jpg?w=1276&ssl=1)

## Descripcion
Para resolver este challenge, deberás crear un proyecto que consuma datos desde
3 fuentes distintas para popular una base de datos SQL con información cultural
sobre bibliotecas, museos y salas de cines argentinos.


## Setup

Crear un entorno virtual en python  ```python -m venv venv``` , luego clonar el repositorio ``` git clone https://github.com/MasamioNakada/challenge_cohete.git```.
Ingresar dentro del entorno virtual e instalar las dependencias  ``` pip install -r requirements.txt```. 

Crear una nueva base de datos en PostgreSql y crear una tabla llamada ```table``` con las siguientes nombres y caracaterísticas:
![](https://cdn.discordapp.com/attachments/826683941053399093/1019523894492811295/db.JPG)

Si no cuenta con PostgreSql sobre la raiz del ```docker-compose.yml``` ejecutamos en la terminal:

```bash 
docker-compose up
```


Finalmente para ejecutar la aplicacion:

```bash 
python archivo.py 
```

## Notes

Durante la ejecucíon del Script se creará 2 carpetas ```categoria``` y ```consulta```.
La carpeta ```categoria``` corresponde a los datos extraídos por el enlace proporcionado en el reto

La carpeta ```consulta``` se encuentra las tablas solicitadas en el reto:
![](https://cdn.discordapp.com/attachments/826683941053399093/1019528221122908210/aa.JPG)
![](https://cdn.discordapp.com/attachments/826683941053399093/1019528698644402176/aaa.JPG)
![](https://cdn.discordapp.com/attachments/826683941053399093/1019529117693128734/cine.JPG)


## Notas

El backend aun no está terminado