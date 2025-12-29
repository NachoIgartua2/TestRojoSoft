from fastapi import APIRouter, HTTPException, Query
from app.models import Cliente
from app.services.cliente_service import ClienteService
from typing import List

router = APIRouter(prefix="/api/clientes", tags=["Clientes"])

@router.get("", response_model=List[Cliente])
def obtener_clientes(
    skip: int = Query(0, ge=0, description="Registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Maximo registros"),
    activo: str = Query(None, description="Filtrar por estado (activo/inactivo)")
):
    """
    Obtiene lista de clientes con paginacion.
    - skip: numero de registros a saltar
    - limit: maximo de registros a retornar
    - activo: filtrar por estado
    """
    try:
        clientes = ClienteService.obtener_clientes(skip, limit, activo)
        return clientes
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@router.get("/{cliente_id}", response_model=Cliente)
def obtener_cliente(cliente_id: str):
    """Obtiene un cliente especifico por su ID"""
    try:
        cliente = ClienteService.obtener_cliente_por_id(cliente_id)
        if not cliente:
            raise HTTPException(status_code=404, detail=f"Cliente {cliente_id} no encontrado")
        return cliente
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
