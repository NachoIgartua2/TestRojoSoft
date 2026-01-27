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
            ClienteTipo,
            DescTipoActividad,
            CUIT,
            Telefono,
            EMail,
            Direccion,
            Zona,
            NombreVendedor,
            DescCondicionPago
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
                CodigoCuenta=row[0],
                NombreCuenta=row[1],
                TipoCuenta=row[2],
                RubroActividad=row[3],
                CUITDocumento=row[4],
                Telefono=row[5],
                Email=row[6],
                DireccionFacturacion=row[7],
                ZonaComercial=row[8],
                VendedorAsignado=row[9],
                CondicionPagoPreferente=row[10]
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
            ClienteTipo,
            DescTipoActividad,
            CUIT,
            Telefono,
            EMail,
            Direccion,
            Zona,
            NombreVendedor,
            DescCondicionPago
        FROM MAESTROCLIENTES
        WHERE Cuenta = ?
        """
        
        resultado = execute_single(query, (cliente_id,))
        
        if not resultado:
            return None
        
        cliente = Cliente(
            CodigoCuenta=resultado[0],
            NombreCuenta=resultado[1],
            TipoCuenta=resultado[2],
            RubroActividad=resultado[3],
            CUITDocumento=resultado[4],
            Telefono=resultado[5],
            Email=resultado[6],
            DireccionFacturacion=resultado[7],
            ZonaComercial=resultado[8],
            VendedorAsignado=resultado[9],
            CondicionPagoPreferente=resultado[10]
        )
        
        return cliente
    
    @staticmethod
    def cliente_existe(cliente_id: str) -> bool:
        """Verifica si un cliente existe"""
        query = "SELECT COUNT(*) FROM MAESTROCLIENTES WHERE Cuenta = ?"
        resultado = execute_single(query, (cliente_id,))
        return resultado[0] > 0 if resultado else False
