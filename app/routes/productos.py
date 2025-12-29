from fastapi import APIRouter, HTTPException, Query
from app.models import Producto
from app.services.producto_service import ProductoService
from typing import List

router = APIRouter(prefix="/api", tags=["Productos"])

@router.get("/productos", response_model=List[Producto])
def obtener_productos(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000)
):
    """Obtiene lista de productos unicos disponibles"""
    try:
        productos = ProductoService.obtener_productos(skip, limit)
        return productos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
