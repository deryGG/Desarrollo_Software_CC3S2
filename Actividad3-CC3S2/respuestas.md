### Actividad 3: Integración de DevOps y DevSecOps con HTTP, DNS, TLS y 12-Factor App

Esta actividad cierra la unidad cubriendo los temas de Introducción a DevOps (qué es y qué no es, del código a producción), el marco CALMS, automatización reproducible con 
Linux/Bash y Make, la visión cultural de DevOps (comunicación y colaboración) y su evolución a DevSecOps, así como los módulos de redes y arquitectura  (HTTP/DNS/TLS, puertos/procesos y metodología 12-Factor App). 

La actividad se divide en una parte teórica (reflexión conceptual) y una parte práctica (ejercicios basados en el laboratorio proporcionado). 

#### Parte teórica
## 1. Introducción a DevOps: ¿Qué es?
es un enfoque que une el desarrollo de software con las operaciones para mejorar la colaboración y la automatización, a diferencia del modelo Waterfall, que es secuencial y más rígido. En DevOps, el lema es "you build it, you run it", lo que significa que los desarrolladores son responsables tanto de la creación como de la ejecución del código.

**¿Qué no es?**

1. No es solo una herramienta 
2. No es solo para desarrolladores
3. No es una metodología de gestión de proyectos tradicional como Waterfall.
4. No es solo automatización


**Realidades:** CALMS (Culture, Automation, Lean, Measurement, Sharing), feedback rápido, métricas de despliegue y gates automáticos.

**Ejemplo de gate de calidad en Makefile:**  
Un target que ejecuta pruebas y bloquea el despliegue si alguna falla


## 2. Marco CALMS en acción

- **Culture:** Colaboración reflejada en el uso compartido de archivos como `Instrucciones.md`.
- **Automation:** Uso de `Makefile` para instalar dependencias y levantar servicios.
- **Lean:** Minimización de pasos manuales, scripts reproducibles.
- **Measurement:** Endpoints de salud (`/health`) y logs para medir disponibilidad.
- **Sharing:** Documentación de runbooks y postmortems en equipo.

**Extensión Sharing:**  
Proponer un runbook en Markdown para incidentes y postmortems colaborativos.

---

## 3. Visión cultural de DevOps y paso a DevSecOps

DevOps rompe silos mediante comunicación y colaboración. DevSecOps integra seguridad desde el inicio:  
- **Cabeceras TLS:** Configuración en Nginx (`nginx.conf`).
- **Escaneo de dependencias:** Target en Makefile para `pip-audit`.
- **Controles sin contenedores:**  
  1. TLS en Nginx (confirma handshake).
  2. Systemd con entorno seguro (variables restringidas).
  3. Firewall restringiendo puertos.

**Justificación:**  
Nginx y systemd permiten aplicar controles de acceso y reinicio seguro.

---

## 4. Metodología 12-Factor App

**Factores elegidos:**  
- **Config por entorno:** Variables en systemd y Makefile (`PORT`, `MESSAGE`).
- **Port binding:** Flask escucha en puerto configurable.
- **Logs como flujos:** Salida estándar, capturable por systemd/journalctl.
- **Statelessness:** La app no guarda estado entre peticiones; depende de backing services.

**Mejoras:**  
- Separar configuración en archivos `.env`.
- Usar backing services externos para persistencia.
- Mejorar manejo de logs centralizados.
