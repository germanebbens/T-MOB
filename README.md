## Ejercicio T-MOB 

Este repositorio tiene como fin resolver el ejercicio técnico planteado por la empresa T-MOB frente a una vacante de Python Developer.

Las consignas del trabajo se indican en el siguiente link. [URL](https://docs.google.com/document/d/1aUztklTqlzx0UIVgYySxeGk2VP1ebwXV/edit?usp=sharing&ouid=109264100590809280879&rtpof=true&sd=true)

Nota: Ejecutar los siguientes comandos dentro de la carpeta del proyecto.

### Iniciar contendores de Docker:

    docker-compose up -d --build


### Migraciones de la base de datos:
    docker-compose run web python manage.py migrate

### Creación de super usuario:

    docker-compose run web python manage.py createsuperuser

### Test (opcional)

    docker-compose run web python manage.py test


Una vez que se tenga el superusuario creado, ingresar al admin de Django: 

http://0.0.0.0:8000/admin

En la sección de Redirect se podrá realizar el ABM de la información, que posteriormente se podrá acceder desde:

http://0.0.0.0:8000/get_from_cache/{KEY}
