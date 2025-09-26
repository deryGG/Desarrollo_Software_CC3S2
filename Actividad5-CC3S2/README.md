# Actividad 5: Pipeline DevOps con Make y Bash

## Resumen del entorno

- **SO:** Ubuntu 22.04 (WSL)
- **Shell:** bash 5.2.21
- **make:** GNU Make 4.3
- **python3:** 3.12.3
- **tar:** GNU tar 1.35
- **sha256sum:** GNU coreutils 9.4

(Ver detalles en `meta/entorno.txt`)

---

## Parte 1 - Construir

## Ejercicios

### 1: Ejecuta `make help` y guarda la salida para análisis. Luego inspecciona `.DEFAULT_GOAL` y `.PHONY` dentro del Makefile.
- **Resultado**: Al ejecutar `make help`, se muestra la lista de objetivos disponibles en el Makefile. `.DEFAULT_GOAL := help` asegura que al ejecutar `make` sin parámetros, se muestre la ayuda por defecto. `.PHONY` es utilizado para evitar que Make busque archivos reales con los nombres de los objetivos (como `clean`, `help`), lo que asegura que siempre se ejecute la receta asociada.

### 2: Comprueba la generación e idempotencia de `build`. Limpia salidas previas, ejecuta `build`, verifica el contenido y repite `build` para constatar que no rehace nada si no cambió la fuente.
- **Resultado**: La primera ejecución de `make build` genera el archivo `out/hello.txt`. En la segunda ejecución, no se rehace el build porque no ha habido cambios en la fuente (`src/hello.py`), lo que demuestra la idempotencia de Make.

### 3: Fuerza un fallo controlado para observar el modo estricto del shell y `.DELETE_ON_ERROR`. Sobrescribe `PYTHON` con un intérprete inexistente y verifica que no quede artefacto corrupto.
- **Resultado**: Al establecer `PYTHON=python4` (un intérprete inexistente), el modo estricto del shell (`set -euo pipefail`) detiene la ejecución. Gracias a `.DELETE_ON_ERROR`, Make no deja artefactos corruptos, lo que asegura que no se genere el archivo `out/hello.txt`.

### 4: Realiza un "ensayo" (dry-run) y una depuración detallada para observar el razonamiento de Make al decidir si rehacer o no.
- **Resultado**: Al ejecutar `make -n`, se realiza un "dry-run" mostrando los comandos que Make ejecutaría sin ejecutarlos realmente. Al usar `make -d`, se obtiene un desglose detallado de las decisiones internas de Make, mostrando cómo decide si rehacer o no los objetivos basándose en las marcas de tiempo de los archivos.

### 5: Demuestra la incrementalidad con marcas de tiempo. Primero toca la fuente y luego el target para comparar comportamientos.
- **Resultado**: Al usar `touch src/hello.py`, Make detecta que el archivo fuente ha cambiado y rehace el build. Sin embargo, al tocar solo el archivo `out/hello.txt`, Make no rehace el objetivo porque el archivo ya está actualizado. Esto demuestra la eficiencia en la incrementalidad de Make.

### 6: Ejecuta verificación de estilo/formato manual (sin objetivos `lint/tools`). Si las herramientas están instaladas, muestra sus diagnósticos; si no, deja evidencia de su ausencia.
- **Resultado**: Si las herramientas `shellcheck` y `shfmt` están instaladas, el script ejecuta estas herramientas para verificar el estilo y formato del código Bash. Si no están instaladas, se deja un mensaje en los logs indicando su ausencia, lo que permite saber qué herramientas faltan en el entorno.

### 7: Construye un paquete reproducible de forma manual, fijando metadatos para que el hash no cambie entre corridas idénticas.
- **Resultado**: Usando `tar` con opciones como `--sort=name`, `--mtime=@0`, `--numeric-owner`, y `gzip -n`, se asegura que el archivo empaquetado (`app.tar.gz`) tenga un hash reproducible, lo que significa que no cambiará entre ejecuciones idénticas del comando.

### 8: Reproduce el error clásico "missing separator" sin tocar el Makefile original. Crea una copia, cambia el TAB inicial de una receta por espacios, y confirma el error.
- **Resultado**: Al reemplazar el TAB inicial por espacios en una receta del Makefile, se reproduce el error clásico "missing separator". Este error ocurre porque Make requiere que las recetas empiecen con un TAB y no con espacios, lo que es una de las reglas más comunes al editar Makefiles.

---

## Parte 2 - Leer

## Ejercicios

### 1: Ejecuta `make -n all` para un dry-run que muestre comandos sin ejecutarlos; identifica expansiones `$@` y `$<`, el orden de objetivos y cómo `all` encadena `tools`, `lint`, `build`, `test`, `package`.
- **Resultado**: Ejecutar `make -n all` muestra los comandos que Make ejecutaría sin ejecutarlos. Las expansiones:
  - `$@` representa el archivo objetivo.
  - `$<` representa la primera dependencia.
- El objetivo `all` ejecuta los objetivos en el siguiente orden: `tools`, `lint`, `build`, `test`, `package`, encadenándolos para que se verifiquen las herramientas, el código sea lintado, compilado, probado y empaquetado.

### 2: Ejecuta `make -d build` y localiza líneas "Considerando el archivo objetivo" y "Debe deshacerse", explica por qué recompila o no `out/hello.txt` usando marcas de tiempo y cómo `mkdir -p $(@D)` garantiza el directorio.
- **Resultado**: `make -d build` muestra que Make decide recompilar `out/hello.txt` si la fuente `src/hello.py` es más reciente. `mkdir -p $(@D)` garantiza que el directorio de salida exista antes de escribir el archivo, evitando errores si el directorio no ha sido creado previamente.

### 3: Fuerza un entorno con BSD tar en PATH y corre `make tools`; comprueba el fallo con "Se requiere GNU tar" y razona por qué `--sort`, `--numeric-owner` y `--mtime` son imprescindibles para reproducibilidad determinista.
- **Resultado**: Si `tar` no es GNU, se genera un fallo con el mensaje "Se requiere GNU tar". Las opciones `--sort`, `--numeric-owner`, y `--mtime` son necesarias para asegurar que el empaquetado sea reproducible, es decir, que el archivo empaquetado tenga un hash consistente entre ejecuciones idénticas.

### 4: Ejecuta `make verify-repro`; observa que genera dos artefactos y compara `SHA256_1` y `SHA256_2`. Si difieren, hipótesis: zona horaria, versión de tar, contenido no determinista o variables de entorno no fijadas.
- **Resultado**: Al ejecutar `make verify-repro`, se generan dos artefactos y se comparan sus hashes SHA256. Si los hashes difieren, puede ser por diferencias en la zona horaria, versión de `tar`, metadatos no controlados o variables de entorno no fijadas, lo que afecta la reproducibilidad del artefacto.

### 5: Corre `make clean && make all`, cronometrando; repite `make all` sin cambios y compara tiempos y logs. Explica por qué la segunda es más rápida gracias a timestamps y relaciones de dependencia bien declaradas.
- **Resultado**: La primera ejecución de `make all` realiza todo el trabajo, mientras que la segunda ejecución es más rápida porque Make detecta que los archivos ya están actualizados gracias a las marcas de tiempo. Esto reduce el trabajo de compilación y prueba, aprovechando la relación entre las dependencias.

### 6: Ejecuta `PYTHON=python3.12 make test` (si existe). Verifica con `python3.12 --version` y mensajes que el override funciona gracias a `?=` y a `PY="${PYTHON:-python3}"` en el script; confirma que el artefacto final no cambia respecto al intérprete por defecto.
- **Resultado**: Al ejecutar `make test` con `PYTHON=python3.12`, se utiliza la versión de Python especificada gracias a la expansión de la variable `PY="${PYTHON:-python3}"`. El artefacto final no cambia, ya que el intérprete de Python no afecta el contenido del artefacto.

### 7: Ejecuta `make test`; describe cómo primero corre `scripts/run_tests.sh` y luego `python -m unittest`. Determina el comportamiento si el script de pruebas falla y cómo se propaga el error a la tarea global.
- **Resultado**: Primero se ejecuta `scripts/run_tests.sh`, que realiza un test sobre `src/hello.py`. Luego, `python -m unittest` ejecuta las pruebas unitarias. Si alguna prueba falla, el error se propaga a través de `make`, deteniendo la ejecución de la tarea global.

### 8: Ejecuta `touch src/hello.py` y luego `make all`; identifica qué objetivos se rehacen (`build`, `test`, `package`) y relaciona el comportamiento con el timestamp actualizado y la cadena de dependencias especificada.
- **Resultado**: Al usar `touch src/hello.py`, se actualiza la marca de tiempo de la fuente, lo que provoca que `make` rehaga el objetivo `build`. Esto también desencadena `test` y `package` porque esos objetivos dependen de `build`. Las dependencias y marcas de tiempo aseguran que solo se rehaga lo necesario.

### 9: Ejecuta `make -j4 all` y observa ejecución concurrente de objetivos independientes; confirma resultados idénticos a modo secuencial y explica cómo `mkdir -p $(@D)` y dependencias precisas evitan condiciones de carrera.
- **Resultado**: Al ejecutar `make -j4`, los objetivos independientes se ejecutan en paralelo, lo que acelera el proceso. `mkdir -p $(@D)` asegura que los directorios de salida estén creados correctamente antes de cualquier intento de escritura, evitando condiciones de carrera. El comportamiento es el mismo que en la ejecución secuencial porque las dependencias están bien definidas.

### 10: Ejecuta `make lint` y luego `make format`; interpreta diagnósticos de `shellcheck`, revisa diferencias aplicadas por `shfmt` y, si está disponible, considera la salida de `ruff` sobre `src/` antes de empaquetar.
- **Resultado**: `make lint` ejecuta `shellcheck` para verificar errores en los scripts de shell y `shfmt` para revisar el formato. Si `ruff` está instalado, también realiza un chequeo de estilo de Python en `src/`. Después de `make format`, el código es reformateado según las reglas de `shfmt`. Los diagnósticos muestran advertencias y sugerencias para mejorar el código.

---


## Parte 3 - Extender

## Ejercicios

### 1: Usa **GNU tar** para reproducibilidad: `--sort=name`, `--numeric-owner`, `--owner=0`, `--group=0`, `--mtime='UTC 1970-01-01'`. Verifica artefactos con `sha256sum` (GNU coreutils). Evita BSD tar: carece de estos flags y rompe hashes en CI portables.
- **Resultado**: Usar **GNU tar** con las opciones `--sort=name`, `--numeric-owner`, `--owner=0`, `--group=0`, y `--mtime='UTC 1970-01-01'` asegura que el empaquetado sea determinista, es decir, que el orden de los archivos y sus metadatos sean consistentes en cada ejecución. El uso de estas opciones evita problemas con el BSD tar, que no soporta estos parámetros y puede generar diferencias en el hash del archivo empaquetado entre ejecuciones.

### 2: Mantén `ruff` como opcional mediante *guard clause*: `command -v ruff >/dev/null && ruff check src || echo "ruff no instalado"`; evita fallos cuando no está disponible y continúa la build, reportando su ausencia.
- **Resultado**: Usando una guard clause en el Makefile (`command -v ruff >/dev/null && ruff check src || echo "ruff no instalado"`), podemos hacer que `ruff` sea opcional. Si no está instalado, el script continúa sin fallar, y se reporta su ausencia sin interrumpir el proceso de build.

### 3: En WSL, trabaja en `~/proyecto` (o cualquier ruta Linux). Evita `/mnt/c` por I/O lento y diferencias de permisos; mejora tiempos y estabilidad de herramientas.
- **Resultado**: Al trabajar en rutas nativas de Linux (por ejemplo, `~/proyecto` en WSL), se evita la lentitud de I/O y problemas de permisos asociados con `/mnt/c`. Esto mejora el rendimiento y la estabilidad de las herramientas, como `make`, al operar en el sistema de archivos de Linux.

### 4: El paralelismo con `make -j` es seguro porque cada receta crea su directorio objetivo con `mkdir -p $(@D)` y las dependencias evitan carreras.
- **Resultado**: El uso de `make -j` para ejecución paralela es seguro porque las recetas crean sus propios directorios objetivo usando `mkdir -p $(@D)`. Las dependencias están bien definidas, evitando condiciones de carrera, lo que garantiza que cada tarea pueda ejecutarse de forma independiente sin conflictos.

### 5: Incluye `out/`, `dist/`, `.ruff_cache/` y `**/__pycache__/` en `.gitignore` para evitar artefactos generados en commits y reducir ruido en diffs.
- **Resultado**: Es esencial agregar las carpetas como `out/`, `dist/`, `.ruff_cache/`, y `__pycache__/` al archivo `.gitignore`. Esto evita que los artefactos generados (archivos temporales, binarios y cachés) se incluyan en los commits, lo que reduce el ruido en los diffs y mantiene el repositorio limpio.

### 6: Define (si te interesa CI) un objetivo `ci` que encadene `tools`, `check`, `package` y `verify-repro`; así validas dependencias, pruebas, empaquetado y reproducibilidad antes de subir cambios o crear tags.
- **Resultado**: Se puede definir un objetivo `ci` en el Makefile para asegurar que todas las tareas necesarias se realicen antes de subir cambios o crear un tag: 
ci: tools check package verify-repro


### 7: Para probar determinismo y detectar variables "fantasma", usa entornos mínimos: `env -i LC_ALL=C LANG=C TZ=UTC make ...`.**
   - **Resultado**: Usar `env -i LC_ALL=C LANG=C TZ=UTC make ...` establece un entorno limpio y controlado, lo que ayuda a probar la reproducibilidad y detectar cualquier variable de entorno no controlada que pueda introducir diferencias entre ejecuciones.

---

## Incidencias y mitigaciones

- No tenía `ruff` instalado, así que el Makefile lo omitió sin romper la build (ver `logs/lint-shellcheck.txt`).
- En WSL, evité `/mnt/c` para mejorar el rendimiento de I/O.
- Un error clásico de Make ("missing separator") se reprodujo y diagnosticó fácilmente con el mensaje de error.

---

## Conclusión operativa

El pipeline es robusto, reproducible y seguro para CI/CD: detecta errores temprano, asegura builds deterministas y permite limpieza y rollback automáticos. La ayuda autodocumentada y los checks de dependencias facilitan el onboarding y la integración continua.
