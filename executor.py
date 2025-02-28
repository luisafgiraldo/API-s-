import sys

import os

print("-----------------------------")
print("Hi! What do you want to execute ? ")
print("1 Benchmarks")
print("2 Large Images")
print("3 Smoke-tests")
print("4 Snapshot")
print("5 VA")
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

print(folder)
print("")

with open(folder) as f:
    exec(f.read())
