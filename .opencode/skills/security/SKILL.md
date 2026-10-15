---
name: Seguridad y Credenciales
description: Proteger credenciales y evitar exponer claves de cifrado, contrasenas o secretos en el codigo, los commits y la salida de comandos. Usar al manejar claves, cifrado, archivos de almacenamiento o al revisar seguridad.
---

# Seguridad: proteger credenciales y claves

## Principios

- Nunca escribir claves de cifrado, contrasenas ni tokens en el codigo fuente.
- La clave de Fernet se recibe como parametro o se lee de una variable de entorno; no se genera ni se fija dentro de un modulo de produccion.
- No incluir secretos en pruebas, ejemplos, README ni mensajes de commit.
- No imprimir (`print`), registrar ni devolver claves o contrasenas en texto plano salvo que la funcion lo pida de forma explicita.

## Claves de cifrado

- La clave se pasa a `PasswordStorage(file_path, key)` como `bytes`. Mantener ese contrato.
- Si se necesita cargar la clave desde el entorno, usar algo como:
  `key = os.environ["PASSWORD_MANAGER_KEY"].encode("utf-8")`
- Nunca versionar el valor de la clave. `.env` y `.env.*` ya estan ignorados; los secretos reales van en variables de entorno o en el gestor de secretos.
- Si una clave se expone (commit, log, captura), tratarla como comprometida: rotarla y, si aplica, avisar al usuario. No intentar "borrarla" reescribiendo la historia sin confirmacion.

## Contrasenas y datos

- Usar `secrets` (no `random`) para generar contrasenas y aleatoriedad sensible.
- Almacenar solo la contrasena cifrada; el texto plano nunca debe persistirse en disco.
- En pruebas, generar claves desechables con `Fernet.generate_key()` y archivos temporales con `tmp_path`.
- Manejar errores de descifrado con excepciones especificas (`InvalidToken`) sin revelar la clave ni el contenido.

## Higiene antes de commitear

- Revisar el diff (`git diff --staged`) y confirmar que no hay claves, `.env` ni datos sensibles.
- Verificar que los archivos ignorados siguen ignorados: `git status --ignored`.
- No pegar salida de comandos que muestre claves o contrasenas reales.
- Preferir datos de ejemplo evidentemente falsos (por ejemplo `usuario123`, `Clave123!`).

## Revision de seguridad

- Comprobar que no se filtraron secretos en el codigo ni en los commits.
- Confirmar que se usa cifrado simetrico correcto (`Fernet`) y que el texto plano no toca el disco.
- Validar que las entradas vacias o invalidas se rechazan con `ValueError`.
- Reportar cualquier hallazgo con archivo y linea, en orden de severidad.
