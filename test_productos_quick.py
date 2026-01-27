#!/usr/bin/env python
"""Test productos"""
import requests
import json

BASE_URL = "http://localhost:8000"

print("\n[TEST] GET /api/productos")
response = requests.get(f"{BASE_URL}/api/productos", params={"skip": 0, "limit": 3})
print(f"Status: {response.status_code}")

if response.status_code == 200:
    productos = response.json()
    print(f"✓ Productos obtenidos: {len(productos)}")
    if productos:
        print(f"\nPrimer producto:")
        print(json.dumps(productos[0], indent=2, ensure_ascii=False, default=str))
else:
    print(f"✗ Error: {response.json()}")
