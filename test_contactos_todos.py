import requests
import json

BASE_URL = "http://localhost:8000"

print("=" * 80)
print("PRUEBA DE ENDPOINT: GET /api/contactos")
print("=" * 80)

try:
    # Obtener todos los contactos (default: limit=10000)
    response = requests.get(f"{BASE_URL}/api/contactos")
    response.raise_for_status()
    
    data = response.json()
    
    print(f"\n✓ Status: {response.status_code}")
    print(f"\n📊 METADATA:")
    print(f"  - Total de contactos: {data['total']}")
    print(f"  - Cantidad en esta página: {data['cantidad']}")
    print(f"  - ¿Hay página siguiente?: {data['tiene_siguiente']}")
    print(f"  - Skip: {data['skip']}")
    print(f"  - Limit: {data['limit']}")
    
    print(f"\n📋 PRIMEROS 5 CONTACTOS:")
    for i, contacto in enumerate(data['datos'][:5], 1):
        print(f"\n  {i}. {contacto['contacto']}")
        print(f"     Cliente: {contacto['cliente']}")
        print(f"     Código: {contacto['codigo_cliente']}")
        print(f"     Email: {contacto['email']}")
        print(f"     Vendedor: {contacto['vendedor']}")
    
    print(f"\n✓ Prueba exitosa!")
    
except requests.exceptions.ConnectionError:
    print("❌ No se puede conectar a http://localhost:8000")
    print("   Asegúrate de que el servidor FastAPI está corriendo")
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print(f"\n{json.dumps(response.json(), indent=2)}")
