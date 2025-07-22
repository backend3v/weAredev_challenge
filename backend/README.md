# WeAreDev Challenge - Backend

## Arquitectura

Este backend implementa una arquitectura **hexagonal (Ports & Adapters)**, siguiendo principios de Clean Architecture y SOLID. El código está organizado en capas:

- **domain/**: Entidades de negocio puras, interfaces de repositorio y servicios de dominio.
- **application/**: Casos de uso (lógica de aplicación, orquestación de entidades y repositorios).
- **infrastructure/**: Implementaciones concretas de repositorios y modelos ORM (Django), lógica de persistencia.
- **adapters/**: Adaptadores de entrada/salida (API REST con Django REST Framework, serializadores, vistas).

## Estructura de carpetas

```
backend/
  tasks/
    domain/
      entities/
      repositories/
      services/
    application/
      use_cases/
    infrastructure/
      models/
      repository_impl/
    adapters/
      api/
        serializers/
        views/
```

## Requisitos
- Python 3.10+
- Django 5+
- Django REST Framework
- PostgreSQL (usando Docker Compose)
- python-dotenv
- drf-spectacular (para documentación OpenAPI/Swagger)

## Variables de entorno (`.env`)

Coloca este archivo en `backend/.env`:

```
DJANGO_SECRET_KEY=tu_clave_secreta
POSTGRES_DB=wearedev_db
POSTGRES_USER=wearedev_user
POSTGRES_PASSWORD=wearedev_pass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

## Levantar la base de datos con Docker Compose

Desde la carpeta `backend/`:
```sh
docker-compose up -d
```

## Instalación y migraciones

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Documentación interactiva de la API

- **Swagger UI:** [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **Redoc:** [http://localhost:8000/api/redoc/](http://localhost:8000/api/redoc/)
- **Esquema OpenAPI:** [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)

## Endpoints de usuario

### Registrar usuario
- **POST** `/api/users/register/`
```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "SuperSecret123"
}
```

### Login de usuario
- **POST** `/api/users/login/`
```json
{
  "email": "testuser@example.com",
  "password": "SuperSecret123"
}
```

### Listar todos los usuarios
- **GET** `/api/users/users/`

## Endpoints de tareas

### Crear tarea
- **POST** `/api/users/tasks/<user_id>/`
```json
{
  "description": "Comprar leche",
  "due_date": "2024-07-23T18:00:00Z"
}
```

### Listar tareas de un usuario
- **GET** `/api/users/tasks/<user_id>/`

### Obtener detalle de una tarea
- **GET** `/api/users/tasks/detail/<task_id>/`

### Actualizar una tarea
- **PUT** `/api/users/tasks/detail/<task_id>/`
```json
{
  "description": "Comprar leche y pan",
  "due_date": "2024-07-24T18:00:00Z",
  "status": "postponed"
}
```

### Eliminar lógicamente una tarea
- **DELETE** `/api/users/tasks/detail/<task_id>/`

### Cambiar estado de una tarea
- **PATCH** `/api/users/tasks/status/<task_id>/`
```json
{
  "status": "completed"
}
```

## Notas de seguridad y buenas prácticas
- Contraseñas siempre hasheadas, nunca en texto plano.
- Validación y manejo de errores en todos los endpoints.
- Arquitectura desacoplada y testeable.

## Contacto
Para dudas o mejoras, contacta a [tu nombre o email].
