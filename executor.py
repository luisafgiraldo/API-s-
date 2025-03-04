import sys
import os
import pytest

print("-----------------------------")
print("Hi! What do you want to execute ? ")
print("1 Benchmarks")
print("2 Large Images")
print("3 Smoke-tests")
print("4 Snapshot")
print("5 VA")
print("6 VA playwright")
print("-----------------------------")

execute = int(input("Select a number to execute: "))
print("")

if execute == 1:
    folder = os.path.join("Benchmarks", "orchestrator.py")
    sys.path.append("Benchmarks")
elif execute == 2:
    folder = os.path.join("Large Images", "orchestrator.py")
    sys.path.append("Large Images")
elif execute == 3:
    folder = os.path.join("Smoke-tests", "orchestrator.py")
    sys.path.append("Smoke-tests")
elif execute == 4:
    folder = os.path.join("Snapshot", "orchestrator.py")
    sys.path.append("Snapshot")
elif execute == 5:
    folder = os.path.join("VA", "orchestrator.py")
    sys.path.append("VA")
elif execute == 6:

    print("## TESTS ##")
    print("1 test_agentic_batsman")
    print("2 OTHER...")
    print("3 OTHER...")

    test = int(input("Select a number to execute: "))
    print("")

    if test == 1:
        folder = os.path.join("VA_playwright", "test_agentic_batsman.py")
    elif test == 2:
        folder = 'example.py'
        
    sys.path.append("VA_playwright")

print(folder)

if execute == 6:
    result = pytest.main([folder])
    print(result)
    # Verificar el resultado de pytest
    if result == 0:
        print("✅ Todas las pruebas pasaron correctamente")
    else:
        print("❌ Algunas pruebas fallaron")
else:
    with open(folder) as f:
        exec(f.read())
