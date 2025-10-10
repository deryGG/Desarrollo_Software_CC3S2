# Actividad 9: pytest + coverage + fixtures + factories + mocking + TDDvv

## Cómo ejecutar

### Versión de Python
Este proyecto fue desarrollado utilizando **Python 3.12**.

### Pasos para crear el entorno virtual (venv)
Primero, asegúrate de tener Python 3.12 o superior instalado en tu sistema.
Luego, crea un entorno virtual ejecutando:

```bash
python3 -m venv .venv
```

Activa el entorno virtual:

* **En Linux/macOS:**
    ```bash
    source .venv/bin/activate
    ```
* **En Windows:**
    ```bash
    .venv\Scripts\activate
    ```

### Instalación de dependencias
Instala las dependencias del proyecto ejecutando:

```bash
pip install -r requirements.txt
```

### Comandos Makefile
Para facilitar la ejecución de pruebas y otras tareas, hemos utilizado un archivo `Makefile`. Aquí están los comandos más importantes:

* **Instalar las dependencias:**
    ```bash
    make deps
    ```
* **Ejecutar todas las pruebas:**
    Ejecuta todas las pruebas utilizando `pytest`:
    ```bash
    make test_all
    ```
* **Generar informe de cobertura:**
    Para verificar la cobertura de código:
    ```bash
    make cov
    ```

---

## Explicación de la metodología utilizada

### Aserciones
Usamos aserciones en nuestras pruebas para verificar que los métodos de la clase `Account` se comporten como se espera. Aserciones como `assert` y `assertEqual` se emplearon para validar que los valores retornados coinciden con lo esperado en varios métodos (por ejemplo, `push()`, `pop()`, `peek()`, etc.).

### Fixtures
Utilizamos fixtures en `pytest` para gestionar la configuración y limpieza del entorno de pruebas. Esto incluye:
* `setup_database`: Crea la base de datos antes de que se ejecute cualquier prueba.
* `clean_tables`: Elimina todos los registros de las tablas después de cada prueba para mantener la base de datos limpia y aislada entre las pruebas.

### Cobertura de Código
Se utilizó `pytest-cov` para medir la cobertura de código. Esto permite saber qué partes del código fueron ejecutadas durante las pruebas, ayudando a identificar áreas que podrían necesitar más pruebas.

Comando utilizado:
```bash
pytest --cov=models --cov-report term-missing
```

### Factories_Fakes
Usamos **FactoryBoy** para crear datos falsos y evitar tener que escribir manualmente datos de prueba. Esto nos permite generar múltiples instancias de `Account` con datos falsos automáticamente.

En el archivo `factories.py`, creamos una clase `AccountFactory` que genera cuentas con datos aleatorios utilizando la librería `Faker` y `Fuzzy` de FactoryBoy.

### Mocking
Aunque no se utilizó un mocking extenso en este proyecto, se podría implementar para simular comportamientos de dependencias externas, como APIs o bases de datos, si fuera necesario.

### Ciclo TDD
Se siguió el ciclo **TDD (Test Driven Development)** básico, donde primero se escriben las pruebas (con expectativas claras), luego se implementa el código mínimo necesario para hacer pasar las pruebas, y finalmente se refactoriza el código. Este ciclo se repitió para cada parte de la clase `Account`.

---

## Resultados

* **Número total de pruebas:** 10 pruebas en total.
* **Cobertura:** 100% de cobertura de código en los archivos `models/__init__.py` y `models/account.py`.

### Hallazgos relevantes:
* Todas las pruebas pasaron sin errores.
* El código está completamente cubierto por las pruebas, lo que asegura que todas las funciones de la clase `Account` han sido validadas.
* Se realizaron pruebas exhaustivas, incluyendo la creación, actualización, eliminación, y la conversión de objetos `Account` a diccionarios y viceversa.
