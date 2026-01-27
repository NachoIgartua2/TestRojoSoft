import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_health():
    """Prueba health check"""
    print("\n" + "="*80)
    print("PROBANDO: Health Check")
    print("="*80)
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status: {response.status_code}")
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {str(e)}")

def test_obtener_clientes():
    """Prueba GET /api/clientes"""
    print("\n" + "="*80)
    print("PROBANDO: GET /api/clientes")
    print("="*80)
    
    try:
        params = {"skip": 0, "limit": 5}
        response = requests.get(f"{BASE_URL}/api/clientes", params=params)
        print(f"Status: {response.status_code}")
        print(f"Clientes obtenidos: {len(response.json())}")
        print("\nPrimeros 3 clientes:")
        for cliente in response.json()[:3]:
            print(f"\n   ID: {cliente['CodigoCuenta']}")
            print(f"   Nombre: {cliente['NombreCuenta']}")
            print(f"   CUIT: {cliente['CUITDocumento']}")
            print(f"   Email: {cliente['Email']}")
            print(f"   Zona: {cliente['ZonaComercial']}")
    except Exception as e:
        print(f"Error: {str(e)}")

def test_obtener_cliente_especifico():
    """Prueba GET /api/clientes/{id}"""
    print("\n" + "="*80)
    print("PROBANDO: GET /api/clientes/{id}")
    print("="*80)
    
    try:
        # Primero obtener un cliente
        response = requests.get(f"{BASE_URL}/api/clientes", params={"limit": 1})
        if response.json():
            cliente_id = response.json()[0]['CodigoCuenta']
            
            response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}")
            print(f"Status: {response.status_code}")
            cliente = response.json()
            print(f"\nCliente encontrado:")
            print(f"   Cuenta: {cliente['CodigoCuenta']}")
            print(f"   Nombre: {cliente['NombreCuenta']}")
            print(f"   CUIT: {cliente['CUITDocumento']}")
            print(f"   Teléfono: {cliente['Telefono']}")
            print(f"   Dirección: {cliente['DireccionFacturacion']}")
            print(f"   Zona: {cliente['ZonaComercial']}")
            print(f"   Vendedor: {cliente['VendedorAsignado']}")
        else:
            print("Sin clientes en la BD")
    except Exception as e:
        print(f"Error: {str(e)}")

def test_obtener_contactos():
    """Prueba GET /api/clientes/{id}/contactos"""
    print("\n" + "="*80)
    print("PROBANDO: GET /api/clientes/{id}/contactos")
    print("="*80)
    
    try:
        # Obtener cliente con contactos
        response = requests.get(f"{BASE_URL}/api/clientes", params={"limit": 10})
        clientes = response.json()
        
        contactos_encontrados = False
        for cliente in clientes:
            cliente_id = cliente['cuenta']
            response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}/contactos")
            
            if response.status_code == 200 and len(response.json()) > 0:
                print(f"Status: {response.status_code}")
                contactos = response.json()
                print(f"\nContactos del cliente {cliente_id}: {len(contactos)}")
                
                for contacto in contactos[:3]:
                    print(f"\n   Contacto: {contacto['contacto']}")
                    print(f"   Cargo: {contacto['cargo']}")
                    print(f"   Teléfono: {contacto['telefono']}")
                    print(f"   Email: {contacto['email']}")
                
                contactos_encontrados = True
                break
        
        if not contactos_encontrados:
            print("Sin contactos para probar")
    except Exception as e:
        print(f"Error: {str(e)}")

def test_obtener_productos():
    """Prueba GET /api/productos"""
    print("\n" + "="*80)
    print("PROBANDO: GET /api/productos")
    print("="*80)
    
    try:
        response = requests.get(f"{BASE_URL}/api/productos", params={"limit": 5})
        print(f"Status: {response.status_code}")
        productos = response.json()
        print(f"Productos obtenidos: {len(productos)}")
        
        print("\nPrimeros 3 productos:")
        for producto in productos[:3]:
            print(f"\n   Código: {producto['codigo']}")
            print(f"   Nombre: {producto['nombre']}")
            print(f"   Rubro: {producto['rubro']}")
            print(f"   Moneda: {producto['moneda']}")
            print(f"   Alícuota IVA: {producto['alicuota_iva']}")
            print(f"   Proveedor: {producto['nombre_proveedor']}")
            print(f"   Unidad: {producto['unidad_medida']}")
            print(f"   Moneda: {producto['moneda']}")
            print(f"   Unidad: {producto['unidad_medida']}")
    except Exception as e:
        print(f"Error: {str(e)}")

def test_obtener_precios():
    """Prueba GET /api/precios"""
    print("\n" + "="*80)
    print("PROBANDO: GET /api/precios")
    print("="*80)
    
    try:
        # Probar sin filtros
        response = requests.get(f"{BASE_URL}/api/precios", params={"limit": 5})
        print(f"Status: {response.status_code}")
        precios = response.json()
        print(f"Precios obtenidos: {len(precios)}")
        
        print("\nPrimeros 3 precios:")
        for precio in precios[:3]:
            print(f"\n   Producto: {precio['nombre_producto']}")
            print(f"   Código: {precio['codigo_producto']}")
            print(f"   Precio: {precio['precio_unitario']} {precio['moneda']}")
            print(f"   Vigencia: {precio['fecha_vigencia']}")
            print(f"   Rubro: {precio['rubro']}")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    """Ejecuta todas las pruebas"""
    print("\n")
    print("╔" + "="*78 + "╗")
    print("║" + " "*20 + "PRUEBAS DE API ROJOSOFT - SALESFORCE" + " "*22 + "║")
    print("╚" + "="*78 + "╝")
    print(f"Fecha/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Base URL: {BASE_URL}")
    
    test_health()
    test_obtener_clientes()
    test_obtener_cliente_especifico()
    test_obtener_contactos()
    test_obtener_productos()
    test_obtener_precios()
    
    print("\n" + "="*80)
    print("PRUEBAS COMPLETADAS")
    print("="*80)

if __name__ == "__main__":
    main()
