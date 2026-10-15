---
name: Python - Estructura y Estilo
description: Estructura del proyecto Python, estilo de codigo, organizacion de archivos y convenciones del paquete password-manager. Usar al crear o modificar modulos, funciones o la disposicion de archivos.
---

# Python: estructura, estilo y organizacion

## Estructura del proyecto

```
password-manager/
├── src/
│   └── password_manager/      # codigo de la aplicacion (paquete)
│       ├── __init__.py
│       ├── generator.py       # generacion de contrasenas
│       └── storage.py         # almacenamiento cifrado
├── tests/                     # pruebas automatizadas
│   ├── __init__.py
│   ├── test_generator.py
│   └── test_storage.py
├── requirements.txt           # dependencias
├── README.md
└── .gitignore
```

Reglas de organizacion:

- Todo el codigo de la aplicacion vive dentro de `src/password_manager/`.
- Cada modulo expone una responsabilidad clara (generar, almacenar, etc.). No mezclar generacion con persistencia.
- Las pruebas van en `tests/` y reflejan al modulo que prueban: `password_manager/storage.py` -> `tests/test_storage.py`.
- No agregar logica que se ejecute al importar un modulo. Evitar efectos secundarios en `__init__.py`.
- No versionar artefactos generados (`__pycache__/`, `.pytest_cache/`, `*.pyc`): ya estan en `.gitignore`.

## Estilo de codigo

- Python 3 y tipado explicito en firmas publicas:
  `def add_password(self, service: str, username: str, password: str) -> None:`
- Nombres: funciones y variables en `snake_case`, clases en `PascalCase`, constantes en `UPPER_CASE`.
- Indentacion de 4 espacios. Sin tabs.
- Una linea en blanco para separar metodos; dos lineas en blanco entre funciones y clases de nivel superior.
- Orden de imports, separados por grupos y una linea en blanco:
  1. Biblioteca estandar (`json`, `secrets`, `string`, `pathlib`).
  2. Terceros (`cryptography`, `pytest`).
  3. Locales del proyecto (`src.password_manager...`).
- Docstring breve en la primera linea de cada clase y funcion publica.
- Preferir `with` para abrir archivos y cerrar recursos.
- Validar entradas al inicio de la funcion y lanzar `ValueError` con mensaje claro.
- Mantener las lineas por debajo de ~88 caracteres y sin espacios sobrantes al final.

## Convenciones del paquete

- Importar desde el paquete de forma explicita:
  `from src.password_manager.storage import PasswordStorage`.
- Al anadir un modulo nuevo, crear tambien su archivo de pruebas correspondiente.
- Reutilizar las dependencias existentes antes de agregar nuevas a `requirements.txt`.
- Usar `secrets` para valores sensibles y `string` para alfabetos de caracteres.

## Antes de terminar

- Ejecutar `py -m pytest` (ver skill **Pruebas con pytest**).
- Actualizar `README.md` y `requirements.txt` si cambian el uso, las funciones o las dependencias (ver skill **Documentacion**).
