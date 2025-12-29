from fastapi import APIRouter, HTTPException, Query
from app.models import Contacto
from app.services.contacto_service import ContactoService
from typing import List

router = APIRouter(prefix="/api/clientes", tags=["Contactos"])

@router.get("/{cliente_id}/contactos", response_model=List[Contacto])
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
