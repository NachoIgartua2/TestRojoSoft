from fastapi import APIRouter, HTTPException, Query
from app.models import Contacto, ContactosPaginados
from app.services.contacto_service import ContactoService
from typing import List

router = APIRouter(tags=["Contactos"])

@router.get("/api/contactos", response_model=ContactosPaginados)
def obtener_todos_contactos(
    skip: int = Query(0, ge=0, description="Cantidad de registros a saltar"),
    limit: int = Query(10000, ge=1, le=50000, description="Límite de registros por página")
):
    """Obtiene TODOS los contactos con información de paginación
    
    Respuesta incluye:
    - **total**: Total de contactos en la BD
    - **cantidad**: Cantidad de contactos en esta página
    - **tiene_siguiente**: Si hay más registros después de estos
    - **skip**: Registros saltados
    - **limit**: Límite usado
    - **datos**: Array de contactos
    """
    try:
        resultado = ContactoService.obtener_todos_contactos(skip, limit)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.get("/api/clientes/{cliente_id}/contactos", response_model=List[Contacto])
def obtener_contactos_cliente(
    cliente_id: str,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000)
):
    """Obtiene contactos de un cliente especifico"""
    try:
        contactos = ContactoService.obtener_contactos_por_cliente(cliente_id, skip, limit)
        return contactos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
