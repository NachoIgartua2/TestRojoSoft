from app.database import execute_query, execute_single
from app.models import Cliente
from typing import List

class ClienteService:
    @staticmethod
    def obtener_clientes(skip: int = 0, limit: int = 100, activo: str = None) -> List[Cliente]:
        """Obtiene lista de clientes con paginacion y filtros"""
        query = """
        SELECT 
            Cuenta,
            Nombre,
            CUIT,
            Telefono,
            EMail,
            Domicilio,
            Localidad,
            Provincia,
            Zona,
            ListaPrecio,
            CondicionPago,
            NombreVendedor,
            ActivoInactivo
        FROM MAESTROCLIENTES
        WHERE 1=1
        """
        
        params = []
        
        if activo:
            query += " AND ActivoInactivo = ?"
            params.append(activo)
        
        query += f" ORDER BY Nombre OFFSET {skip} ROWS FETCH NEXT {limit} ROWS ONLY"
        
        resultados = execute_query(query, tuple(params) if params else None)
        
        clientes = []
        for row in resultados:
            cliente = Cliente(
                cuenta=row[0],
                nombre=row[1],
                cuit=row[2],
                telefono=row[3],
                email=row[4],
                domicilio=row[5],
                localidad=row[6],
                provincia=row[7],
                zona=row[8],
                lista_precio=row[9],
                condicion_pago=row[10],
                vendedor=row[11],
                activo=row[12]
            )
            clientes.append(cliente)
        
        return clientes
    
    @staticmethod
    def obtener_cliente_por_id(cliente_id: str) -> Cliente:
        """Obtiene un cliente especifico por su ID"""
        query = """
        SELECT 
            Cuenta,
            Nombre,
            CUIT,
            Telefono,
            EMail,
            Domicilio,
            Localidad,
            Provincia,
            Zona,
            ListaPrecio,
            CondicionPago,
            NombreVendedor,
            ActivoInactivo
        FROM MAESTROCLIENTES
        WHERE Cuenta = ?
        """
        
        resultado = execute_single(query, (cliente_id,))
        
        if not resultado:
            return None
        
        cliente = Cliente(
            cuenta=resultado[0],
            nombre=resultado[1],
            cuit=resultado[2],
            telefono=resultado[3],
            email=resultado[4],
            domicilio=resultado[5],
            localidad=resultado[6],
            provincia=resultado[7],
            zona=resultado[8],
            lista_precio=resultado[9],
            condicion_pago=resultado[10],
            vendedor=resultado[11],
            activo=resultado[12]
        )
        
        return cliente
    
    @staticmethod
    def cliente_existe(cliente_id: str) -> bool:
        """Verifica si un cliente existe"""
        query = "SELECT COUNT(*) FROM MAESTROCLIENTES WHERE Cuenta = ?"
        resultado = execute_single(query, (cliente_id,))
        return resultado[0] > 0 if resultado else False
