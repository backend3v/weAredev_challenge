# WeAreDev Challenge - Fullstack

## Descripción

Este proyecto es una solución fullstack para la gestión de tareas, con backend en Django/PostgreSQL y frontend en Angular clásico (listo para integración móvil con Capacitor).

## Estructura del repositorio

```
wearedev_challenge/
  backend/        # Backend Django + PostgreSQL
  frontend/
    wearedev-frontend-cli/   # Frontend Angular clásico
  README.md       # Este archivo
```

## Instalación y ejecución

### Backend
1. Ve a la carpeta `backend/`.
2. Instala dependencias y variables de entorno (ver `backend/README.md`).
3. Levanta la base de datos con Docker Compose:
   ```sh
   docker-compose up -d
   ```
4. Aplica migraciones y ejecuta el servidor:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```

### Frontend
1. Ve a la carpeta `frontend/wearedev-frontend-cli/`.
2. Instala dependencias:
   ```sh
   npm install
   ```
3. Inicia el servidor de desarrollo:
   ```sh
   ng serve
   ```
4. Accede a [http://localhost:4200](http://localhost:4200)

## Requisitos
- Node.js 18+ (LTS recomendado)
- Angular CLI 17+
- Python 3.10+
- Docker (para PostgreSQL)

## Notas
- El frontend es Angular clásico, todos los componentes son NO standalone.
- El backend expone una API RESTful documentada con Swagger/Redoc.
- Incluye colección de Postman para pruebas.

---

Para dudas o mejoras, contacta a [tu nombre o email]. 