import pyodbc
from typing import Optional
import logging
import os

logger = logging.getLogger(__name__)

def get_database_config() -> dict:
    """Lee configuración de BD desde variables de entorno"""
    return {
        'server': os.getenv('DB_SERVER', 'replicas-db.database.windows.net'),
        'database': os.getenv('DB_NAME', 'app_bi_Orellano'),
        'username': os.getenv('DB_USER', 'app_bi_Orellano'),
        'password': os.getenv('DB_PASSWORD', ''),
    }

def get_connection_string() -> str:
    """Construye el string de conexion a SQL Server"""
    config = get_database_config()
    return (
        f"Driver={{ODBC Driver 18 for SQL Server}};"
        f"Server=tcp:{config['server']},1433;"
        f"Database={config['database']};"
        f"Uid={config['username']};"
        f"Pwd={config['password']};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

def get_connection():
    """Obtiene una conexion a la BD"""
    try:
        conn = pyodbc.connect(get_connection_string())
        return conn
    except Exception as e:
        logger.error(f"Error de conexion a BD: {str(e)}")
        raise Exception(f"Error de conexion a base de datos: {str(e)}")

def execute_query(query: str, params: tuple = None):
    """Ejecuta una query SELECT"""
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        resultados = cursor.fetchall()
        return resultados
    finally:
        conn.close()

def execute_single(query: str, params: tuple = None):
    """Ejecuta una query SELECT que retorna un solo registro"""
    resultados = execute_query(query, params)
    return resultados[0] if resultados else None

def check_connection() -> bool:
    """Verifica que la conexion a BD funcione"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM MAESTROCLIENTES")
        resultado = cursor.fetchone()
        conn.close()
        return resultado[0] > 0
    except Exception as e:
        logger.error(f"Error verificando conexion: {str(e)}")
        return False
