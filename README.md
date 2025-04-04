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
4. Ejecutar la aplicación: `python /app/main.py`

## 📡 EndPoints 
- POST /upload/departments/
- POST /upload/jobs/
- POST /upload/employees/
- GET /metrics/quarterly-hires/2021
- GET /metrics/above-average-hiring/2021


## 📊 Ejemplo de uso
curl -X 'POST' \
  'http://127.0.0.1:8000/upload/departments/?batch_size=2000' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@departments.csv;type=text/csv'

curl -X 'GET' \
  'http://127.0.0.1:8000/metrics/quarterly-hires/2021' \
  -H 'accept: application/json'

## Resultado

### Ejecución de API
![alt text][api]

### Carga de tablas desde CSV
![alt text][upload_departments]

### Ejecución de contratados por puesto
![alt text][quarterly-hires]

### Ejecución de contratados por departamento
![alt text][above-average-hiring]

### Ejemplo de tabla en base de datos PostgreSQL
![alt text][database]

[api]: https://github.com/epincay/migration_api/blob/main/img/api.jpg "Ejecución API"
[upload_departments]: https://github.com/epincay/migration_api/blob/main/img/upload_departments.jpg "Carga de tablas desde CSV"
[quarterly-hires]: https://github.com/epincay/migration_api/blob/main/img/quarterly-hires.jpg "Ejecución de contratados por puesto"
[above-average-hiring]: https://github.com/epincay/migration_api/blob/main/img/above-average-hiring.jpg "Ejecución de contratados por departamento"
[database]: https://github.com/epincay/migration_api/blob/main/img/database.jpg "Muestra de tabla en base de datos"