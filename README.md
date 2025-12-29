# API RojoSoft - Salesforce

Integración entre el ERP RojoSoft y el CRM Salesforce.

## Requisitos

- Python 3.9+
- ODBC Driver 18 for SQL Server
- Conexión a Azure SQL Server

## Instalación

### 1. Clonar repositorio
```bash
git clone <repo-url>
cd testrojosoft
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
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

## Ejecutar

```bash
python main.py
```

La API estará disponible en `http://localhost:8000`

## Documentación

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Pruebas

```bash
python test_api.py
```

## Estructura

```
testrojosoft/
├── main.py              # Punto de entrada
├── requirements.txt     # Dependencias
├── .env                 # Variables (no subir)
├── .env.example         # Template
├── app/
│   ├── database.py      # Acceso a datos
│   ├── models.py        # Modelos
│   ├── routes/          # Endpoints
│   │   ├── clientes.py
│   │   ├── contactos.py
│   │   ├── productos.py
│   │   └── precios.py
│   └── services/        # Lógica
│       ├── cliente_service.py
│       ├── contacto_service.py
│       ├── producto_service.py
│       └── precio_service.py
└── test_api.py         # Tests
```

## Endpoints

### Clientes
- `GET /api/clientes` - Lista de clientes con paginación
- `GET /api/clientes/{id}` - Cliente específico

### Contactos
- `GET /api/clientes/{id}/contactos` - Contactos de cliente

### Productos
- `GET /api/productos` - Catálogo de productos

### Precios
- `GET /api/precios` - Precios vigentes

### Sistema
- `GET /health` - Estado de API y BD
- `GET /` - Información de API

## Arquitectura

Patrón MVC con servicios:

```
Routes (Controllers)
    ↓
Services (Lógica)
    ↓
Database (Datos)
    ↓
Azure SQL Server
```

## Seguridad

- Credenciales en variables de entorno
- Archivo `.env` en `.gitignore`
- CORS configurado (ajustar para producción)
- Manejo de errores en todos los endpoints

## Notas

- Sin autenticación (agregar según requerimientos)
- CORS abierto a todos (restringir en producción)
- Sin pooling de conexiones (considerarlo para alta carga)

## Contribuir

1. Crear rama: `git checkout -b feature/tu-feature`
2. Hacer cambios: `git commit -m 'Agrega tu-feature'`
3. Push: `git push origin feature/tu-feature`
4. Pull request

## Licencia

Propietario - RojoSoft / Salesforce Integration
