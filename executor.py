import sys
import os
import pytest

print("-----------------------------")
print("Hi! What do you want to execute?")
print("-----------------------------")

# Get all folders in the current directory, excluding unwanted ones
exclude_folders = ['__pycache__', '.pytest_cache', 'venv', '.git']
current_directory = os.getcwd()
folders = [folder for folder in os.listdir(current_directory)
           if os.path.isdir(os.path.join(current_directory, folder)) and folder not in exclude_folders]

# Sort folders alphabetically
folders.sort()

# Display available folders in alphabetical order
for i, folder in enumerate(folders, start=1):
    print(f"{i} {folder}")

print("-----------------------------")

# Folder selection
selected_folder = None
while selected_folder is None:
    try:
        execute = int(input("Select a number to execute: ")) - 1
        if 0 <= execute < len(folders):
            selected_folder = folders[execute]
        else:
            print("❌ Invalid selection. Try again.")
    except ValueError:
        print("❌ Please enter a valid number.")

folder = os.path.join(selected_folder, "orchestrator.py")
sys.path.append(selected_folder)

# If the selected folder is VA_playwright, offer test selection
if selected_folder == "VA_playwright":
    print("-----------------------------")
    print("## TESTS ##")
    tests = [file for file in os.listdir(selected_folder)
             if file.startswith("test_") and file.endswith(".py")]
    tests.sort()
    for i, test in enumerate(tests, start=1):
        print(f"{i} {test}")
    print("A Execute all tests in parallel")
    print("")

    test = None
    while test is None:
        selection = input("Select a test to execute (or 'A' for all in parallel): ").strip()
        if selection.upper() == 'A':
            folder = selected_folder
            test = 'all'
        else:
            try:
                selection = int(selection) - 1
                if 0 <= selection < len(tests):
                    test = tests[selection]
                    folder = os.path.join(selected_folder, test)
                else:
                    print("❌ Invalid test selection. Try again.")
            except ValueError:
                print("❌ Please enter a valid number or 'A' for all.")

print(f"📂 Executing: {folder}\n")

# Run Playwright with real-time logs
if selected_folder == "VA_playwright":
    if test == 'all':
        result = pytest.main(['-s', '-n', 'auto', '--continue-on-collection-errors', '--maxfail=999', selected_folder])
    else:
        result = pytest.main(['-s', folder, '--continue-on-collection-errors', '--maxfail=999'])
    
    print(result)
    if result == 0:
        print("✅ All tests passed successfully")
    else:
        print("❌ Some tests failed")
else:
    with open(folder) as f:
        exec(f.read())


