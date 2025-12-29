from fastapi import APIRouter, HTTPException, Query
from app.models import Precio
from app.services.precio_service import PrecioService
from typing import List, Optional

router = APIRouter(prefix="/api", tags=["Precios"])

@router.get("/precios", response_model=List[Precio])
def obtener_precios(
    cliente_id: Optional[str] = Query(None, description="Codigo de cliente (opcional)"),
    moneda: Optional[str] = Query(None, description="Filtrar por moneda (ARS/USD)")
):
    """Obtiene precios vigentes de productos"""
    try:
        precios = PrecioService.obtener_precios(cliente_id, moneda)
        return precios
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
