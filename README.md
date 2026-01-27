# API RojoSoft - Salesforce

Integración bidireccional entre el ERP RojoSoft y el CRM Salesforce.

## Requisitos

- Docker y Docker Compose
- Credenciales de Azure SQL Server
- Puerto 8000 disponible en el host

## Quick Start

### 1. Clonar repositorio
```bash
git clone <repo-url>
cd rojosoft-salesforce-bridge
```

### 2. Configurar variables de entorno
```bash
cp .env.example .env
```

Editar `.env` con tus datos:
```env
DB_SERVER=tu_servidor.database.windows.net
DB_NAME=tu_base_datos
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña

API_VERSION=1.0.0
API_HOST=0.0.0.0
API_PORT=8000
```

### 3. Ejecutar con Docker
```bash
docker build -t rojosoft-salesforce-bridge .
docker run -d \
  --name rojosoft-bridge \
  -p 8000:8000 \
  --env-file .env \
  rojosoft-salesforce-bridge
```

La API estará disponible en `http://localhost:8000`

## Documentación

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Health Check

```bash
curl http://localhost:8000/health
```

## Pruebas

Ejecutar tests dentro del contenedor:
```bash
docker exec rojosoft-bridge python test_api.py
```

## Estructura

```
rojosoft-salesforce-bridge/
├── Dockerfile           # Configuracion de contenedor
├── .dockerignore        # Archivos excluidos de imagen
├── main.py              # Punto de entrada
├── requirements.txt     # Dependencias Python
├── .env                 # Variables (no subir)
├── .env.example         # Template
├── app/
│   ├── database.py      # Conexion a BD
│   ├── models.py        # Modelos de datos
│   ├── routes/          # Endpoints HTTP
│   │   ├── clientes.py
│   │   ├── contactos.py
│   │   ├── productos.py
│   │   └── precios.py
│   └── services/        # Logica de negocio
│       ├── cliente_service.py
│       ├── contacto_service.py
│       ├── producto_service.py
│       └── precio_service.py
└── test_api.py          # Tests
```

## Endpoints

GET /api/clientes - Lista de clientes con paginacion
GET /api/clientes/{id} - Cliente especifico
GET /api/clientes/{id}/contactos - Contactos de cliente
GET /api/productos - Catalogo de productos
GET /api/precios - Precios vigentes
GET /health - Estado de API y BD
GET / - Informacion de API

## Arquitectura

Patron MVC con servicios desacoplados:

Routes (HTTP) -> Services (Logica) -> Database (Acceso a datos) -> Azure SQL Server

## Deployment

### Docker Hub

Construccion y push a Docker Hub:

```bash
docker build -t tuusuario/rojosoft-salesforce-bridge:1.0.0 .
docker push tuusuario/rojosoft-salesforce-bridge:1.0.0
```

### Digital Ocean

Crear droplet con Docker instalado y ejecutar:

```bash
docker run -d \
  --name rojosoft-bridge \
  -p 8000:8000 \
  --env-file .env \
  tuusuario/rojosoft-salesforce-bridge:1.0.0
```

## Verificacion

Estado del contenedor:
```bash
docker ps
```

Ver logs:
```bash
docker logs rojosoft-bridge
```

Detener contenedor:
```bash
docker stop rojosoft-bridge
```

## Variables de Entorno

DB_SERVER - Servidor Azure SQL
DB_NAME - Nombre de base de datos
DB_USER - Usuario de BD
DB_PASSWORD - Contrasena de BD
API_VERSION - Version de API (default: 1.0.0)
API_HOST - Host de escucha (default: 0.0.0.0)
API_PORT - Puerto de escucha (default: 8000)

## Seguridad

Credenciales se pasan via variables de entorno, no en codigo
Archivo .env no se incluye en control de versiones
CORS configurado (ajustar en produccion si es necesario)
Manejo de errores en todos los endpoints
Archivo .dockerignore excluye archivos innecesarios de imagen

## Base de Datos

Servidor: Azure SQL Server
Tablas principales:
- MAESTROCLIENTES (clientes)
- MAESTROCONTACTOS (contactos)
- MAESTROFACTURACION (facturas)

Conexion mediante ODBC con pyodbc

## Contribuir

1. Crear rama: git checkout -b feature/tu-feature
2. Hacer cambios: git commit -m 'Descripcion del cambio'
3. Push: git push origin feature/tu-feature
4. Pull request

## Licencia

Propietario - RojoSoft / Salesforce Integration
