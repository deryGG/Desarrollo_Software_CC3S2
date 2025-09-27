# Actividad 6: Introducción a Git - Conceptos básicos y operaciones esenciales

Este repositorio contiene la evidencia de los comandos y operaciones básicas de Git, incluyendo configuración, manejo de ramas, fusiones y manipulación del historial.

## Resumen de temas y comandos

- **git config:** Configura el usuario y correo global/local.  
  _Comando:_ `git config --list` → [`logs/config.txt`](logs/config.txt)

- **git init:** Inicializa un repositorio Git en el directorio actual.  
  _Comando:_ `git init` → [`logs/init-status.txt`](logs/init-status.txt)

- **git add / git commit:** Prepara y registra cambios en el historial.  
  _Comando:_ `git add .` y `git commit -m "mensaje"` → [`logs/add-commit.txt`](logs/add-commit.txt)

- **git log:** Muestra el historial de commits.  
  _Comando:_ `git log --oneline` → [`logs/log-oneline.txt`](logs/log-oneline.txt)

- **Ramas:**  
  - Crear: `git branch <nombre>`  
  - Cambiar: `git checkout <nombre>` o `git switch <nombre>`  
  - Fusionar: `git merge <rama>`  
  - Eliminar: `git branch -d <rama>`  
  _Comando:_ `git branch -vv` → [`logs/branches.txt`](logs/branches.txt)  
  _Comando:_ `git merge ...` → [`logs/merge-o-conflicto.txt`](logs/merge-o-conflicto.txt)

- **Resolución de conflictos:**  
  Se resolvió manualmente editando el archivo en conflicto, luego `git add` y `git commit`.

- **Comandos opcionales:**  
  Si se usaron(no se aplico):  
- `git revert`: Revierte un commit creando uno nuevo que deshace los cambios.
- `git rebase`: Reaplica commits sobre otra base, reescribiendo el historial.
- `git cherry-pick <commit>`: Aplica un commit específico de otra rama en la actual.
- `git stash`: Guarda temporalmente cambios no confirmados para recuperarlos después.

  ------
Sin remoto.

Cada archivo en `logs/` fue generado ejecutando el comando correspondiente y redirigiendo la salida, por ejemplo:  
`git --version > logs/git-version.txt`


## Trabajar con ramas: La piedra angular de la colaboración

## Preguntas

- **¿Cómo te ha ayudado Git a mantener un historial claro y organizado de tus cambios?**  
  Git permite registrar cada cambio realizado en el proyecto, con mensajes descriptivos y fechas, lo que facilita identificar cuándo y por qué se hicieron modificaciones. Esto ayuda a mantener un historial ordenado y fácil de consultar.

- **¿Qué beneficios ves en el uso de ramas para desarrollar nuevas características o corregir errores?**  
  El uso de ramas permite trabajar en nuevas funcionalidades o correcciones de errores de forma aislada, sin afectar la rama principal. Así se pueden probar cambios y fusionarlos solo cuando estén listos, evitando conflictos y manteniendo la estabilidad del proyecto.

- **Revisión final del historial de commits:**  
  Se realizó una revisión con `git log --oneline` para asegurar que todos los cambios y commits estén correctamente registrados en el historial.

- **Revisión del uso de ramas y merges:**  
  Se verificó el uso de ramas y fusiones con `git branch -vv` y `git log --graph --oneline`, comprobando cómo Git maneja múltiples líneas de desarrollo y la integración de cambios de diferentes ramas.
