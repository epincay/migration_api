# migration_api
Data Engineering Coding Challenge
API REST para migrar datos de archivos CSV a una base de datos PostgreSQL con capacidades de procesamiento por lotes.

## Características
- Subir archivos CSV para rellenar las tablas de la base de datos
- Inserción por lotes de hasta 1000 registros con una sola solicitud
- Base de datos PostgreSQL
- Interfaz RESTful basada en fastapi

## 📦 Requisitos previos

- Python 3.8+
- PostgreSQL 12+

## Instalación

1. Clonar el repositorio
2. Instalar las dependencias: `pip install -r requirements.txt`
3. Ejecutar la aplicación: `python app.py`
