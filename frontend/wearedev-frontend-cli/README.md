# WeAreDev Challenge - Frontend

## Descripción

Este frontend es una aplicación Angular clásica (NO standalone) que sirve como BackOffice administrativo y base para la app móvil híbrida (Capacitor). Permite gestionar usuarios y tareas, consumiendo la API RESTful del backend.

## Estructura de carpetas

```
src/app/
  app.module.ts
  app-routing.module.ts
  app.component.ts
  app.component.html
  features/
    auth/
      register/
    tasks/
      task-list/
      task-form/
    test/
  core/
    services/
    models/
```

## Instalación y ejecución

1. Instala dependencias:
   ```sh
   npm install
   ```
2. Inicia el servidor de desarrollo:
   ```sh
   ng serve
   ```
3. Accede a [http://localhost:4200](http://localhost:4200)

## Rutas principales
- `/tasks` — Listado y gestión de tareas
- `/register` — Registro de usuario
- `/test` — Componente de prueba

## Notas importantes
- Todos los componentes son clásicos (NO standalone).
- Los servicios y modelos están en `core/`.
- El menú de navegación está en `app.component.html`.
- El proyecto está listo para integración con Capacitor para app móvil.

## Requisitos
- Node.js 18+ (LTS recomendado)
- Angular CLI 17+

## Troubleshooting
- Si tienes errores de `standalone`, elimina cualquier línea `standalone: true` o `standalone: false` en los decoradores `@Component`.
- Si el build falla, elimina `node_modules` y `dist`, luego ejecuta `npm install` y `ng serve`.

---

Para dudas o mejoras, contacta a [tu nombre o email].
