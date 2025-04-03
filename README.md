# migration_api
Data Engineering Coding Challenge.
API REST para migrar datos de archivos CSV a una base de datos PostgreSQL con capacidades de procesamiento por lotes.

## ⚙️ Características
- Subir archivos CSV para rellenar las tablas de la base de datos
- Inserción por lotes de hasta 1000 registros con una sola solicitud
- Base de datos PostgreSQL
- Interfaz RESTful basada en FastAPI

## 📦 Requisitos previos

- Python 3.8+
- PostgreSQL 12+

## 🛠 Instalación

1. Clonar el repositorio `git clone https://github.com/epincay/migration_api.git`
2. cd migracion_api
3. Instalar las dependencias: `pip install -r requirements.txt`
4. Ejecutar la aplicación: `python app.py`

## 📡 EndPoints 
- POST /upload/departments/
- POST /upload/jobs/
- POST /upload/employees/
- GET /metrics/quarterly-hires/2021


## 📊 Ejemplo de uso
curl -X 'POST' \
  'http://127.0.0.1:8000/upload/departments/?batch_size=2000' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@departments.csv;type=text/csv'

curl -X 'GET' \
  'http://127.0.0.1:8000/metrics/quarterly-hires/2021' \
  -H 'accept: application/json'