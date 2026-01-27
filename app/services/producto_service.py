from app.database import execute_query
from app.models import Producto
from typing import List

class ProductoService:
    @staticmethod
    def obtener_productos(skip: int = 0, limit: int = 100) -> List[Producto]:
        """Obtiene lista de productos unicos desde facturas"""
        query = """
        SELECT DISTINCT
            CodigoArticulo,
            Articulo,
            CentroOperativo,
            CodigoMoneda,
            AlicuotaIVAArticulo,
            NombreProveedorCosto,
            CuentaProveedorCosto,
            UnidadMedida
        FROM MAESTROFACTURACION
        WHERE CodigoArticulo IS NOT NULL 
            AND CodigoArticulo != ''
        ORDER BY Articulo
        OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        """
        
        resultados = execute_query(query, (skip, limit))
        
        productos = []
        for row in resultados:
            producto = Producto(
                codigo=row[0],
                nombre=row[1],
                rubro=row[2],
                moneda=row[3],
                alicuota_iva=float(row[4]) if row[4] is not None else None,
                nombre_proveedor=row[5],
                cuenta_proveedor=row[6],
                unidad_medida=row[7]
            )
            productos.append(producto)
        
        return productos
    
    @staticmethod
    def contar_productos() -> int:
        """Cuenta productos unicos en la BD"""
        query = """
        SELECT COUNT(DISTINCT CodigoArticulo) 
        FROM MAESTROFACTURACION
        WHERE CodigoArticulo IS NOT NULL AND CodigoArticulo != ''
        """
        resultados = execute_query(query)
        return resultados[0][0] if resultados else 0
