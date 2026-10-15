---
name: Git y GitHub
description: Flujo de trabajo con ramas, Conventional Commits, Issues y Pull Requests para publicar cambios en GitHub. Usar al preparar commits, ramas, pushes o pull requests.
---

# Git y GitHub

## Ramas

- Partir siempre de `develop`, que es la rama de integracion.
- Una rama por tarea, con prefijo segun el tipo de cambio:
  - `feature/<descripcion>` para funcionalidades.
  - `fix/<descripcion>` para correcciones.
  - `docs/<descripcion>` para documentacion.
  - `chore/<descripcion>` o `refactor/<descripcion>` para mantenimiento.
- Descripcion en minusculas y separada por guiones: `feature/password-generator`.

```sh
git switch develop
git pull origin develop
git switch -c feature/mi-cambio
```

## Conventional Commits

Formato: `<tipo>(<alcance opcional>): <descripcion en imperativo>`

Tipos permitidos: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `style`, `perf`, `ci`, `security`.

Ejemplos del proyecto:

- `feat: add secure password generator`
- `fix: guarantee selected password character types`
- `docs: document project workflow`
- `test: add encrypted storage tests`
- `chore: update dependencies`

Reglas:

- Descripcion breve, en minusculas, sin punto final.
- Un commit = un cambio con sentido propio.
- Si el cambio cierra una Issue, referenciarla: `Closes #12` en el cuerpo o en el PR.

## Issues

- Antes de empezar una tarea no trivial, verificar o crear una Issue que describa el objetivo y los criterios de aceptacion.
- Una rama y un PR se vinculan a esa Issue.
- Con GitHub CLI: `gh issue create --title "..." --body "..."`.

## Pull Requests

- Abrir el PR de la rama hacia `develop`.
- Titulo en formato Conventional Commits; cuerpo con resumen, cambios y como se probo.
- Incluir `Closes #<numero>` cuando corresponda.
- Requisitos antes de abrir el PR: suite `py -m pytest` en verde y documentacion actualizada.

```sh
git push -u origin feature/mi-cambio
gh pr create --base develop --title "feat: ..." --body "..."
```

## Antes de commitear

- `git status` y `git diff --staged` para revisar que no haya secretos (ver skill **Seguridad y Credenciales**).
- Mensaje convencional y cambios acotados.
- No hacer `push --force` sobre ramas compartidas sin confirmacion.
- No subir directamente a `develop` ni a `main`: siempre a traves de rama y PR.
