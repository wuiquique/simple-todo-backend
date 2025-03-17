📌 README.md

# 📝 TODO Backend API con FastAPI

Este es un backend para gestionar tareas y proyectos, construido con **FastAPI** y **SQLAlchemy**, utilizando **SQLite** como base de datos. También está **dockerizado** para facilitar su despliegue.

---

## 🚀 Tecnologías Utilizadas
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Docker](https://www.docker.com/)
- [Uvicorn](https://www.uvicorn.org/)

---

## 🛠️ **Requisitos Previos**
Asegúrate de tener instalado:
- [Python 3.10+](https://www.python.org/downloads/)
- [Docker y Docker Compose](https://docs.docker.com/get-docker/)
- Crear un archivo **todo.db** en la raíz del proyecto

---

## 📂 **Estructura del Proyecto**

```
todo-backend/
│── app/
│   ├── controllers.py
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
│── todo.db (crear al hacer pull)
```

---

## ⚡ **Configuración Local (Sin Docker)**
Si deseas correr el proyecto en tu máquina local sin Docker:

### 1️⃣ **Crear un entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```
2️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```
3️⃣ Configurar la base de datos
```bash
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
```
4️⃣ Iniciar el servidor
```bash
uvicorn app.main:app --reload
```
El servidor estará corriendo en 👉 http://localhost:8000

⸻

## 🐳 **Ejecutar con Docker (Recomendado)**

Si prefieres usar Docker, sigue estos pasos en el directorio:

1️⃣ Construir la imagen
```bash
docker compose build
```
2️⃣ Levantar el contenedor
```bash
docker compose up --build
```


⸻

🔎 Endpoints Disponibles

Después de correr el servidor, puedes acceder a la documentación automática de la API en:

📌 Swagger UI: http://localhost:8000/docs

📌 Redoc UI: http://localhost:8000/redoc

| Método   | Ruta                | Descripción                        |
|----------|---------------------|------------------------------------|
| `GET`    | `/`                 | Verificar si el servidor está corriendo |
| `POST`   | `/login`            | Iniciar sesión                    |
| `POST`   | `/register`         | Registrar un nuevo usuario        |
| `DELETE` | `/user/{userId}`     | Eliminar un usuario               |
| `GET`    | `/projects/{userId}` | Obtener proyectos de un usuario   |
| `POST`   | `/projects`         | Crear un nuevo proyecto           |
| `DELETE` | `/projects/{projectId}` | Eliminar un proyecto        |
| `GET`    | `/tasks/{projectId}` | Obtener tareas de un proyecto     |
| `POST`   | `/tasks`            | Crear una nueva tarea             |
| `DELETE` | `/tasks/{taskId}`    | Eliminar una tarea                |


⸻

🛠 Comandos Útiles

📌 Reiniciar el contenedor Docker
```bash
docker compose down && docker compose up --build -d
```
📌 Acceder al contenedor
```bash
docker compose ps  # Obtener el ID del contenedor
```
📌 Ver logs en tiempo real
```bash
docker compose logs -f
```
