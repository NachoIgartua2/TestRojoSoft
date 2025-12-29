from app.database import execute_query
from app.models import Precio
from typing import List, Optional

class PrecioService:
    @staticmethod
    def obtener_precios(cliente_id: Optional[str] = None, moneda: Optional[str] = None, limit: int = 100) -> List[Precio]:
        """Obtiene precios vigentes de productos"""
        query = """
        SELECT DISTINCT
            CodigoArticulo,
            Articulo,
            Precio,
            CodigoMoneda,
            FechaOrigen,
            UnidadMedida,
            CentroOperativo
        FROM MAESTROFACTURACION
        WHERE Precio > 0
            AND CodigoArticulo IS NOT NULL
            AND CodigoArticulo != ''
        """
        
        params = []
        
        if moneda:
            query += " AND CodigoMoneda = ?"
            params.append(moneda)
        
        query += " ORDER BY FechaOrigen DESC, Articulo"
        
        resultados = execute_query(query, tuple(params) if params else None)
        
        # Agrupar por producto (precio mas reciente)
        precios_dict = {}
        for row in resultados:
            codigo = row[0]
            if codigo not in precios_dict:
                precios_dict[codigo] = Precio(
                    codigo_producto=row[0],
                    nombre_producto=row[1],
                    precio_unitario=float(row[2]) if row[2] else 0,
                    moneda=row[3],
                    fecha_vigencia=str(row[4]) if row[4] else None,
                    unidad_medida=row[5],
                    rubro=row[6]
                )
        
        return list(precios_dict.values())[:limit]
