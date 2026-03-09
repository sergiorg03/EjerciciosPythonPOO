# Comandos de Git y su explicación

Este documento resume los comandos más comunes de Git, explicando qué hacen y cuándo usarlos.

---

## 1️⃣ Estado y log

| Comando | Explicación |
|---------|-------------|
| `git status` | Muestra el estado actual del repositorio: archivos modificados, en staging o sin seguimiento. |
| `git log` | Muestra el historial de commits de la rama actual. |
| `git log --oneline` | Muestra el historial resumido (una línea por commit). |
| `git diff` | Muestra los cambios no confirmados respecto al último commit. |
| `git diff --staged` | Muestra los cambios en staging respecto al último commit. |

---

## 2️⃣ Agregar cambios

| Comando | Explicación |
|---------|-------------|
| `git add <archivo>` | Añade un archivo al staging para el próximo commit. |
| `git add .` | Añade todos los archivos modificados al staging. |
| `git restore <archivo>` | Descarta los cambios locales en un archivo (vuelve al último commit). |
| `git restore .` | Descarta todos los cambios locales. |
| `git restore --staged <archivo>` | Quita un archivo del staging, pero mantiene los cambios locales. |

---

## 3️⃣ Commits

| Comando | Explicación |
|---------|-------------|
| `git commit -m "mensaje"` | Crea un commit con los archivos en staging y un mensaje descriptivo. |
| `git commit -am "mensaje"` | Combina `add` + `commit` para archivos ya rastreados (modificados). |

---

## 4️⃣ Ramas

| Comando | Explicación |
|---------|-------------|
| `git branch` | Lista las ramas locales. |
| `git branch <nombre>` | Crea una nueva rama. |
| `git checkout <rama>` | Cambia a otra rama. |
| `git switch <rama>` | Alternativa moderna a `checkout`. |
| `git checkout -b <rama>` | Crea y cambia a una nueva rama. |
| `git merge <rama>` | Fusiona otra rama en la rama actual. |

---

## 5️⃣ Actualizar y subir cambios

| Comando | Explicación |
|---------|-------------|
| `git push origin <rama>` | Envía commits locales al repositorio remoto en la rama indicada. |
| `git pull` | Trae cambios del remoto y los fusiona en la rama local. |
| `git fetch` | Trae los cambios del remoto sin fusionarlos automáticamente. |

---

## 6️⃣ Revertir y resetear

| Comando | Explicación |
|---------|-------------|
| `git reset --soft HEAD~1` | Borra el último commit, mantiene los cambios en staging. |
| `git reset --mixed HEAD~1` | Borra el último commit, mantiene los cambios **solo en el working directory**, no en staging. |
| `git reset --hard HEAD~1` | Borra el último commit y **todos los cambios locales** (staging + working directory). |
| `git revert HEAD` | Crea un nuevo commit que **deshace los cambios** del commit anterior. Seguro para repositorios compartidos. |
| `git reset --soft HEAD~2 && git push --force` | Borra los últimos 2 commits del remoto, manteniendo los cambios localmente. |

---

## 7️⃣ Descartar cambios locales

| Comando | Explicación |
|---------|-------------|
| `git checkout -- <archivo>` | Descarta los cambios locales en un archivo (antes de Git 2.23). |
| `git clean -fd` | Elimina archivos no rastreados/directorios. ⚠️ Muy peligroso, revisa antes con `-n`. |

---

## 8️⃣ Comparar ramas y commits

| Comando | Explicación |
|---------|-------------|
| `git diff <rama1> <rama2>` | Muestra diferencias entre dos ramas. |
| `git diff <commit1> <commit2>` | Muestra diferencias entre dos commits. |
| `git show <commit>` | Muestra detalles de un commit específico. |

---

## 9️⃣ Otros comandos útiles

| Comando | Explicación |
|---------|-------------|
| `git clone <url>` | Clona un repositorio remoto a tu máquina local. |
| `git remote -v` | Lista los remotos configurados. |
| `git tag <nombre>` | Crea una etiqueta (tag) para marcar versiones. |
| `git stash` | Guarda temporalmente cambios no confirmados para limpiar el working directory. |
| `git stash pop` | Recupera los cambios guardados con `stash`. |
| `git rm <archivo>` | Elimina un archivo del repo y lo prepara para commit. |

---

## 10️⃣ Buenas prácticas

- Siempre revisa `git status` antes de hacer commits o resets.  
- Para eliminar commits ya enviados a remoto, usa **force push** solo si estás seguro.  
- Para deshacer cambios compartidos, **revert** es más seguro que reset.  
- Mantén commits pequeños y descriptivos para facilitar el historial.  

---

💡 Con esto tienes un **manual rápido de Git** que cubre:  

- Estado y log  
- Agregar cambios  
- Commits  
- Ramas  
- Subir y bajar cambios  
- Revertir y resetear commits  
- Comparaciones y stashing  
