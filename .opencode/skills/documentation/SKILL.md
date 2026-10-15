---
name: Documentacion del Proyecto
description: Mantener actualizados el README.md y las dependencias de requirements.txt junto con cada cambio. Usar al cambiar funcionalidades, uso, tecnologia o dependencias.
---

# Documentacion: README y dependencias

## README.md

Mantener `README.md` sincronizado con el estado real del proyecto. Actualizar cuando cambie alguna de estas secciones:

- **Objetivo** y **Funcionalidades previstas**: marcar lo ya implementado y ajustar lo pendiente.
- **Tecnologias**: reflejar librerias nuevas (por ejemplo `cryptography`).
- **Estado del proyecto**: indicar avance real.
- **Seguridad** y **Flujo de trabajo**: conservar las notas de buenas practicas.
- Anadir una seccion de **Uso** o **Instalacion** con los comandos reales cuando se incorpore codigo ejecutable.

Directrices:

- Escribir en espanol, claro y conciso, en el estilo existente.
- Usar encabezados `##`, listas y bloques de codigo con `sh`.
- Documentar comandos verificables: `py -m pytest`, instalacion de dependencias.
- No inventar funcionalidades que aun no existen; si algo esta previsto, indicarlo como tal.

## Dependencias (requirements.txt)

- Registrar toda dependencia externa realmente importada (por ejemplo `cryptography`).
- Al usar una libreria nueva, agregarla a `requirements.txt` y al README en el mismo cambio.
- Fijar versiones cuando el proyecto lo requiera: `cryptography>=42,<43`.
- Eliminar dependencias que ya no se usen.
- No incluir herramientas de desarrollo que no sean necesarias para ejecutar el proyecto.

## Cuando actualizar

- En el mismo commit o PR que introduce el cambio (no dejarlo para despues).
- Si el cambio afecta pruebas, mencionar en el README como ejecutarlas.
- Si el cambio afecta seguridad o credenciales, reflejarlo en la seccion **Seguridad**.

## Verificacion final

- El README coincide con el codigo y los comandos funcionan tal como se documentan.
- Toda dependencia importada aparece en `requirements.txt`, y viceversa.
- El tipo de commit para estos cambios es `docs:`.
