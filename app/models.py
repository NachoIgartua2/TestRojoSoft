from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Union
from decimal import Decimal

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

class ContactosPaginados(BaseModel):
    """Respuesta paginada de contactos"""
    total: int = Field(..., description="Total de contactos")
    cantidad: int = Field(..., description="Cantidad de contactos en esta página")
    tiene_siguiente: bool = Field(..., description="Indica si hay página siguiente")
    skip: int = Field(..., description="Contactos saltados")
    limit: int = Field(..., description="Límite de contactos por página")
    datos: List[Contacto] = Field(..., description="Lista de contactos")

class Cliente(BaseModel):
    CodigoCuenta: str
    NombreCuenta: Optional[str] = None
    TipoCuenta: Optional[str] = None
    RubroActividad: Optional[Union[str, int]] = None
    CUITDocumento: Optional[str] = None
    Telefono: Optional[str] = None
    Email: Optional[str] = None
    DireccionFacturacion: Optional[str] = None
    ZonaComercial: Optional[str] = None
    VendedorAsignado: Optional[str] = None
    CondicionPagoPreferente: Optional[str] = None

class Producto(BaseModel):
    codigo: str
    nombre: str
    rubro: Optional[str] = None
    moneda: Optional[str] = None
    alicuota_iva: Optional[Union[str, float, Decimal]] = None
    nombre_proveedor: Optional[str] = None
    cuenta_proveedor: Optional[str] = None
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
