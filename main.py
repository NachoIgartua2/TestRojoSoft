from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import logging
import os
from dotenv import load_dotenv

load_dotenv()

# Import routes
from app.routes import clientes, contactos, productos, precios
from app.database import check_connection

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear app FastAPI
app = FastAPI(
    title="API RojoSoft ↔ Salesforce",
    description="Integracion bidireccional entre RojoSoft y Salesforce CRM",
    version=os.getenv("API_VERSION", "1.0.0"),
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(clientes.router)
app.include_router(contactos.router)
app.include_router(productos.router)
app.include_router(precios.router)

@app.get("/health", tags=["Sistema"])
def health_check():
    """Verifica estado de la API y conexion a BD"""
    try:
        api_version = os.getenv("API_VERSION", "1.0.0")
        if check_connection():
            return {
                "status": "healthy",
                "database": "connected",
                "timestamp": datetime.now().isoformat(),
                "version": api_version
            }
        else:
            return {
                "status": "unhealthy",
                "database": "disconnected",
                "timestamp": datetime.now().isoformat()
            }
    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

@app.get("/", tags=["Info"])
def info():
    """Informacion de la API"""
    api_version = os.getenv("API_VERSION", "1.0.0")
    return {
        "nombre": "API RojoSoft ↔ Salesforce",
        "version": api_version,
        "descripcion": "Integracion bidireccional entre RojoSoft (ERP) y Salesforce (CRM)",
        "arquitectura": "MVC - Servicios separados por capa",
        "endpoints": {
            "GET": [
                "GET /api/clientes - Listar clientes con paginacion",
                "GET /api/clientes/{id} - Obtener cliente especifico",
                "GET /api/clientes/{id}/contactos - Contactos de un cliente",
                "GET /api/productos - Listar productos disponibles",
                "GET /api/precios - Obtener listas de precios vigentes"
            ],
            "Sistema": [
                "GET /health - Verificar estado de API y BD",
                "GET /docs - Documentacion interactiva (Swagger UI)",
                "GET /redoc - Documentacion alternativa (ReDoc)"
            ]
        },
        "base_de_datos": {
            "servidor": "Azure SQL Server",
            "base": "app_bi_Orellano",
            "tablas": [
                "MAESTROCLIENTES (925 registros)",
                "MAESTROCONTACTOS (379 registros)",
                "MAESTROFACTURACION (9,806 registros)"
            ]
        },
        "caracteristicas": [
            "Sincronizacion de clientes desde RojoSoft",
            "Lectura de contactos de clientes",
            "Catalogo de productos",
            "Precios vigentes",
            "Documentacion auto-generada con Swagger",
            "Manejo de errores robusto",
            "Logging completo"
        ]
    }

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", "8000"))
    uvicorn.run(app, host=host, port=port, log_level="info")
