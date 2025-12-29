from pydantic import BaseModel
from typing import Optional, List

class Cliente(BaseModel):
    cuenta: str
    nombre: Optional[str] = None
    cuit: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    domicilio: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    zona: Optional[str] = None
    lista_precio: Optional[str] = None
    condicion_pago: Optional[str] = None
    vendedor: Optional[str] = None
    activo: Optional[str] = None

class Contacto(BaseModel):
    id: int
    codigo_cliente: Optional[str] = None
    cliente: Optional[str] = None
    contacto: str
    cargo: Optional[str] = None
    telefono: Optional[str] = None
    telefono_movil: Optional[str] = None
    email: Optional[str] = None
    vendedor: Optional[str] = None

class Producto(BaseModel):
    codigo: str
    nombre: str
    rubro: Optional[str] = None
    moneda: Optional[str] = None
    unidad_medida: Optional[str] = None

class Precio(BaseModel):
    codigo_producto: str
    nombre_producto: str
    precio_unitario: float
    moneda: str
    fecha_vigencia: Optional[str] = None
    unidad_medida: Optional[str] = None
    rubro: Optional[str] = None

class OrdenVentaProducto(BaseModel):
    codigo: str
    nombre: str
    cantidad: float
    precio_unitario: float
    moneda: str

class OrdenVentaRequest(BaseModel):
    cliente_id: str
    productos: list[OrdenVentaProducto]
    monto_total: float
    condicion_pago: str
    fecha_entrega_estimada: Optional[str] = None
    observaciones: Optional[str] = None

class OrdenVentaResponse(BaseModel):
    numero_orden: str
    cliente_id: str
    cliente_nombre: str
    monto_total: float
    cantidad_productos: int
    estado: str
    fecha_creacion: str
    mensaje: str
