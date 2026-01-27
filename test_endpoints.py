#!/usr/bin/env python
"""Script rápido para probar endpoints"""
import requests
import json
from time import sleep

BASE_URL = "http://localhost:8000"

print("\n" + "="*80)
print("PROBANDO ENDPOINTS")
print("="*80)

# Test 1: Health Check
print("\n[1] Health Check...")
try:
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    print(f"✓ Status: {response.status_code}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 2: Clientes
print("\n[2] GET /api/clientes...")
try:
    response = requests.get(f"{BASE_URL}/api/clientes", params={"skip": 0, "limit": 3}, timeout=5)
    if response.status_code == 200:
        clientes = response.json()
        print(f"✓ Status: {response.status_code}")
        print(f"✓ Clientes obtenidos: {len(clientes)}")
        if clientes:
            print(f"\nPrimer cliente:")
            print(json.dumps(clientes[0], indent=2, ensure_ascii=False))
    else:
        print(f"✗ Status: {response.status_code}")
        print(f"✗ Error: {response.json()}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 3: Cliente específico
print("\n[3] GET /api/clientes/{id}...")
try:
    # Primero obtener un cliente
    response = requests.get(f"{BASE_URL}/api/clientes", params={"limit": 1}, timeout=5)
    if response.json():
        cliente_id = response.json()[0]['CodigoCuenta']
        response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}", timeout=5)
        if response.status_code == 200:
            print(f"✓ Status: {response.status_code}")
            print(f"✓ Cliente {cliente_id} obtenido")
        else:
            print(f"✗ Status: {response.status_code}")
            print(f"✗ Error: {response.json()}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 4: Productos
print("\n[4] GET /api/productos...")
try:
    response = requests.get(f"{BASE_URL}/api/productos", params={"skip": 0, "limit": 3}, timeout=5)
    if response.status_code == 200:
        productos = response.json()
        print(f"✓ Status: {response.status_code}")
        print(f"✓ Productos obtenidos: {len(productos)}")
        if productos:
            print(f"\nPrimer producto:")
            print(json.dumps(productos[0], indent=2, ensure_ascii=False))
    else:
        print(f"✗ Status: {response.status_code}")
        print(f"✗ Error: {response.json()}")
except Exception as e:
    print(f"✗ Error: {e}")

# Test 5: Contactos
print("\n[5] GET /api/clientes/{id}/contactos...")
try:
    response = requests.get(f"{BASE_URL}/api/clientes", params={"limit": 1}, timeout=5)
    if response.json():
        cliente_id = response.json()[0]['CodigoCuenta']
        response = requests.get(f"{BASE_URL}/api/clientes/{cliente_id}/contactos", timeout=5)
        if response.status_code == 200:
            contactos = response.json()
            print(f"✓ Status: {response.status_code}")
            print(f"✓ Contactos para {cliente_id}: {len(contactos)}")
            if contactos:
                print(f"\nPrimer contacto:")
                print(json.dumps(contactos[0], indent=2, ensure_ascii=False))
        else:
            print(f"✗ Status: {response.status_code}")
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "="*80)
print("PRUEBAS COMPLETADAS")
print("="*80 + "\n")
