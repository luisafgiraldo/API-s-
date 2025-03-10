import sys
import os
import pytest

print("-----------------------------")
print("Hi! What do you want to execute?")
print("-----------------------------")

# Get all folders in the current directory, excluding unwanted folders
excluir_carpetas = ['__pycache__', '.pytest_cache', 'venv', '.git']
directorio_actual = os.getcwd()
carpetas = [carpeta for carpeta in os.listdir(directorio_actual)
            if os.path.isdir(os.path.join(directorio_actual, carpeta)) and carpeta not in excluir_carpetas]

# Sort folders alphabetically
carpetas.sort()

# Display available folders in alphabetical order
for i, carpeta in enumerate(carpetas, start=1):
    print(f"{i} {carpeta}")

print("-----------------------------")

# Select the folder using a while loop
carpeta_seleccionada = None
while carpeta_seleccionada is None:
    try:
        execute = int(input("Select a number to execute: ")) - 1
        if 0 <= execute < len(carpetas):
            carpeta_seleccionada = carpetas[execute]
        else:
            print("❌ Invalid selection. Try again.")
    except ValueError:
        print("❌ Please enter a valid number.")

folder = os.path.join(carpeta_seleccionada, "orchestrator.py")
sys.path.append(carpeta_seleccionada)

# If the folder is VA_playwright, offer test selection
if carpeta_seleccionada == "VA_playwright":
    print("-----------------------------")
    print("## TESTS ##")
    tests = [archivo for archivo in os.listdir(carpeta_seleccionada)
             if archivo.startswith("test_") and archivo.endswith(".py")]
    tests.sort()
    for i, test in enumerate(tests, start=1):
        print(f"{i} {test}")
    print("A Execute all tests in parallel")
    print("")

    test = None
    while test is None:
        seleccion = input("Select a test to execute (or 'A' for all in parallel): ").strip()
        if seleccion.upper() == 'A':
            folder = carpeta_seleccionada
            test = 'all'
        else:
            try:
                seleccion = int(seleccion) - 1
                if 0 <= seleccion < len(tests):
                    test = seleccion
                    folder = os.path.join(carpeta_seleccionada, tests[test])
                else:
                    print("❌ Invalid test selection. Try again.")
            except ValueError:
                print("❌ Please enter a valid number or 'A' for all.")

print(f"📂 Executing: {folder}\n")

if carpeta_seleccionada == "VA_playwright":
    if test == 'all':
        result = pytest.main(['-n', 'auto', '--continue-on-collection-errors', '--maxfail=999', carpeta_seleccionada])
    else:
        result = pytest.main([folder, '--continue-on-collection-errors', '--maxfail=999'])
    print(result)
    if result == 0:
        print("✅ All tests passed successfully")
    else:
        print("❌ Some tests failed")
else:
    with open(folder) as f:
        exec(f.read())
