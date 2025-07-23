#!/bin/bash

echo "Verificando estructura y archivos críticos de Angular CLI..."

# Archivos y carpetas requeridos
REQUIRED=(
  "src/app/app.module.ts"
  "src/app/app-routing.module.ts"
  "src/app/app.component.ts"
  "src/app/app.component.html"
  "src/app/features/auth/register/register.component.ts"
  "src/app/features/tasks/task-list/task-list.component.ts"
)

ALL_OK=true

for FILE in "${REQUIRED[@]}"; do
  if [ ! -f "$FILE" ]; then
    echo "❌ Falta el archivo: $FILE"
    ALL_OK=false
  else
    echo "✅ $FILE"
  fi
done

# Verifica que los decoradores NO tengan standalone
echo
echo "Buscando 'standalone:' en decoradores @Component..."
grep -r 'standalone:' src/app/ && FOUND=true || FOUND=false

if [ "$FOUND" = true ]; then
  echo "❌ ¡Al menos un componente tiene 'standalone:' en el decorador! Elimínalo."
  ALL_OK=false
else
  echo "✅ Ningún decorador @Component tiene 'standalone:'."
fi

# Verifica que los componentes estén declarados en app.module.ts
echo
echo "Verificando declaraciones en app.module.ts..."
for COMP in "AppComponent" "RegisterComponent" "TaskListComponent"; do
  grep "$COMP" src/app/app.module.ts > /dev/null
  if [ $? -ne 0 ]; then
    echo "❌ $COMP no está declarado en app.module.ts"
    ALL_OK=false
  else
    echo "✅ $COMP declarado en app.module.ts"
  fi
done

if [ "$ALL_OK" = true ]; then
  echo
  echo "🎉 Estructura y archivos críticos verificados correctamente."
else
  echo
  echo "⚠️  Hay problemas en la estructura o archivos. Revisa los mensajes anteriores."
fi