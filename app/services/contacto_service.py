from app.database import execute_query, execute_single
from app.models import Contacto, ContactosPaginados
from typing import List

class ContactoService:
    @staticmethod
    def obtener_contactos_por_cliente(cliente_id: str, skip: int = 0, limit: int = 100) -> List[Contacto]:
        """Obtiene contactos de un cliente especifico"""
        query = """
        SELECT 
            IDTabla,
            CodigoCliente,
            Cliente,
            Contacto,
            Cargo,
            Telefono,
            TelefonoMovil,
            EMail,
            Vendedor
        FROM MAESTROCONTACTOS
        WHERE CodigoCliente = ?
        ORDER BY Contacto
        OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        """
        
        resultados = execute_query(query, (cliente_id, skip, limit))
        
        contactos = []
        for row in resultados:
            contacto = Contacto(
                id=row[0],
                codigo_cliente=row[1],
                cliente=row[2],
                contacto=row[3],
                cargo=row[4],
                telefono=row[5],
                telefono_movil=row[6],
                email=row[7],
                vendedor=row[8]
            )
            contactos.append(contacto)
        
        return contactos
    
    @staticmethod
    def contar_contactos_cliente(cliente_id: str) -> int:
        """Cuenta cuantos contactos tiene un cliente"""
        query = "SELECT COUNT(*) FROM MAESTROCONTACTOS WHERE CodigoCliente = ?"
        resultado = execute_single(query, (cliente_id,))
        return resultado[0] if resultado else 0
    
    @staticmethod
    def obtener_todos_contactos(skip: int = 0, limit: int = 10000) -> ContactosPaginados:
        """Obtiene TODOS los contactos con paginación"""
        # Contar total
        count_query = "SELECT COUNT(*) FROM MAESTROCONTACTOS"
        total = execute_single(count_query)[0]
        
        # Obtener contactos
        query = """
        SELECT 
            IDTabla,
            CodigoCliente,
            Cliente,
            Contacto,
            Cargo,
            Telefono,
            TelefonoMovil,
            EMail,
            Vendedor
        FROM MAESTROCONTACTOS
        ORDER BY CodigoCliente, Contacto
        OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        """
        
        resultados = execute_query(query, (skip, limit))
        
        contactos = []
        for row in resultados:
            contacto = Contacto(
                id=row[0],
                codigo_cliente=row[1],
                cliente=row[2],
                contacto=row[3],
                cargo=row[4],
                telefono=row[5],
                telefono_movil=row[6],
                email=row[7],
                vendedor=row[8]
            )
            contactos.append(contacto)
        
        cantidad = len(contactos)
        tiene_siguiente = (skip + limit) < total
        
        return ContactosPaginados(
            total=total,
            cantidad=cantidad,
            tiene_siguiente=tiene_siguiente,
            skip=skip,
            limit=limit,
            datos=contactos
        )
