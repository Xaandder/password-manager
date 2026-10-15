---
name: Pruebas con pytest
description: Ejecutar y mantener las pruebas automatizadas con py -m pytest antes de dar una tarea por terminada. Usar siempre al finalizar cambios de codigo o al crear o modificar pruebas.
---

# Pruebas: ejecutar pytest antes de terminar

## Regla principal

Antes de dar cualquier tarea por terminada, ejecutar en la raiz del proyecto:

```sh
py -m pytest
```

No se considera terminada una tarea si la suite falla. No se reduce ni se comenta una prueba solo para que pase: corregir el codigo o la prueba segun corresponda.

## Ubicacion y nombres

- Las pruebas viven en `tests/`.
- Archivos: `tests/test_<modulo>.py` (por ejemplo `tests/test_storage.py`).
- Funciones de prueba: `test_<comportamiento>()`, sin argumentos salvo fixtures.
- Usar el prefijo `src.password_manager...` en los imports, igual que el resto del proyecto.

## Estilo de las pruebas

- Una prueba verifica un comportamiento; nombres descriptivos en el estilo existente
  (`test_password_can_be_retrieved`, `test_empty_password_is_rejected`).
- Usar fixtures de pytest para montar dependencias, como la fixture `storage` con `tmp_path`.
- Comprobar errores con `pytest.raises(...)` y, cuando aporte, `match=`.
- Para cifrado, usar claves desechables `Fernet.generate_key()` y archivos en `tmp_path`; nunca claves reales.
- Evitar depender del azar: comprobar propiedades (longitud, tipos de caracteres), no valores exactos de una contrasena aleatoria.

## Flujo de trabajo

1. Escribir o actualizar la prueba que cubre el cambio.
2. Ejecutar `py -m pytest`, o solo el archivo afectado con `py -m pytest tests/test_storage.py`.
3. Si falla, leer el error completo, corregir y volver a ejecutar.
4. Repetir hasta que toda la suite pase.
5. Reportar el resultado (pruebas aprobadas y fallidas) al cerrar la tarea.

## Casos a cubrir

- Camino feliz y casos limite (longitud 0, entradas vacias, servicio inexistente).
- Errores esperados: `ValueError`, `KeyError`.
- Seguridad: que la contrasena guardada este cifrada y no aparezca en texto plano.
