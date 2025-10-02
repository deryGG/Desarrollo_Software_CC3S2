
# Actividad 7: Estrategias de fusión en Git

## Ejercicios guiados (responde en `README.md`)

### A) Evitar (o no) `--ff`

* Ejecuta una fusión FF real (ver 1).
* **Pregunta:** ¿Cuándo **evitarías** `--ff` en un equipo y por qué?

  * Evitaría `--ff` cuando se requiere mantener un historial claro de las integraciones. El uso de `--no-ff` es mejor para equipos, ya que crea un commit de merge que documenta explícitamente cuándo se integraron cambios, lo cual es útil para auditoría y trazabilidad. Ya que con `--ff` pdriamos perder el contexto de las ramas


### B) Trabajo en equipo con `--no-ff`

* Crea dos ramas con cambios paralelos y **fusiónalas con `--no-ff`**.
* **Preguntas:** ¿Qué ventajas de trazabilidad aporta? ¿Qué problemas surgen con **exceso** de merges?

  * **Ventajas:** Usar `--no-ff` preserva la trazabilidad al crear un commit de merge, lo cual permite identificar cuándo se integraron las ramas.

    **Problemas:** El exceso de merges puede hacer que el historial se vuelva desordenado, especialmente si se realizan demasiadas fusiones sin necesidad.

### C) Squash con muchos commits

* Haz 3-4 commits en `feature-3` y aplánalos con `--squash`.
* **Preguntas:** ¿Cuándo conviene? ¿Qué se **pierde** respecto a merges estándar?

  * Cuándo conviene: `--squash` es útil cuando queremos mantener un historial limpio y evitar commits de prueba o intermedios innecesarios.
  Qué se pierde: Se pierde la granularidad de los cambios intermedios, ya que todo se aplana en un solo commit. Además, el historial no muestra cómo se desarrolló la funcionalidad paso a paso.


## Conflictos reales con **no-fast-forward**

### **Pregunta:** 
#### ¿Qué pasos adicionales hiciste para resolverlo?

**Respuesta:**  
1. Identifiqué los archivos con conflictos usando `git status`.  
2. Utilicé `git diff` para ver las diferencias y entender cómo resolver el conflicto.  
3. Edité los archivos para eliminar los delimitadores de conflicto (`<<<<<<<`, `=======`, `>>>>>>>`) e integré los cambios de manera coherente.  
4. Realicé el commit del merge resuelto con `git add` y `git commit`.

#### ¿Qué prácticas (convenciones, PRs pequeñas, tests) lo evitarían?

**Respuesta:**  
1. **Convenciones claras** para nombrar ramas y estructurar el trabajo evitarían que dos personas editen el mismo archivo o línea.  
2. **Pull Requests pequeñas**: Crear PRs más pequeñas facilita la revisión de código y reduce la posibilidad de conflictos.  
3. **Pruebas automatizadas (tests)**: Asegurarse de que el código se prueba antes del merge puede reducir la probabilidad de conflictos y mejorar la calidad del código.

## Comparar historiales tras cada método

### **Pregunta:** 
#### ¿Cómo se ve el DAG en cada caso?

**Respuesta:**  
1. **Fast-forward (`--ff`)**: El DAG es lineal, sin commit de merge. No hay bifurcaciones, lo que hace que el historial sea limpio, pero pierde la trazabilidad de las integraciones de las ramas.
  
2. **No-fast-forward (`--no-ff`)**: El DAG tiene bifurcaciones debido al commit de merge, lo que ayuda a preservar la trazabilidad de cuándo y cómo se integraron las ramas. Esto puede hacer que el historial sea más visualmente complejo, pero es más claro para auditar.

3. **Squash (`--squash`)**: El DAG es lineal, similar a un **fast-forward**, pero sin el commit de merge. La diferencia es que la rama de características no aparece en el DAG, ya que se aplana todo en un único commit.

#### ¿Qué método prefieres para: trabajo individual, equipo grande, repos con auditoría estricta?

1. **Trabajo individual**: Prefiero **`--ff`** porque mantiene el historial limpio y sencillo, sin commits de merge innecesarios. Ideal cuando no se necesita mantener una trazabilidad detallada de las integraciones.

2. **Equipo grande**: Prefiero **`--no-ff`** porque mantiene el historial claro, con commits de merge que documentan las integraciones. Esto facilita la colaboración en equipos grandes y proporciona trazabilidad sobre cuándo se hicieron las fusiones.

3. **Repos con auditoría estricta**: Prefiero **`--no-ff`** también en este caso, ya que el commit de merge actúa como un punto de control visible para auditoría. Es importante para tener un historial claro de las integraciones y facilitar el análisis posterior de cambios.


## Revertir un commit

#### ¿Cuándo usar `git revert` en vez de `git reset`?

**Respuesta:**  
- **`git revert`** se utiliza para deshacer un commit específico sin modificar el historial. En lugar de eliminar el commit, crea un **nuevo commit** que revierte los cambios. Es ideal cuando trabajas en un repositorio compartido o con historial público, ya que no afectas a otros colaboradores.
- **`git reset`** elimina commits, lo que puede ser útil para corregir errores en el historial local. Sin embargo, **modifica el historial**, lo cual puede causar problemas si ya has compartido esos commits con otros colaboradores. Por eso, **`git reset`** debe usarse con precaución en repositorios públicos.

#### ¿Impacto en un repo compartido con historial público?

**Respuesta:**  
- **`git revert`** es seguro en repositorios públicos porque no cambia el historial, solo agrega un commit que deshace los efectos del commit original. Esto mantiene la coherencia del historial para todos los colaboradores.
- **`git reset`** puede causar problemas en un repositorio compartido porque reescribe el historial, lo que puede hacer que los cambios de otros colaboradores se desincronicen. Si ya has hecho un push de los commits a un repositorio remoto, **usar `git reset` sobrescribe esos commits**, lo que puede provocar conflictos cuando otros intentan sincronizar sus cambios.

