import numpy as np
import matplotlib.pyplot as plt
import random
"""
Antimicrobial Resistance Simulation using OD600
B.Tech Biotechnology Mini Project

This project simulates bacterial growth in presence of antibiotics
and compares sensitive vs resistant strains using OD600 values.
"""
print("ANTIBIOTIC RESISTANCE SIMULATOR (OD600 MODEL)")
print("B.Tech Biotechnology Mini Project")
print("------------------------------------------------")
# ===============================
# TIME SETTINGS (0–12 hours)
# ===============================
time = list(range(0, 13))  # 0 to 12 hours
# ===============================
# BACTERIAL GROWTH SIMULATION FUNCTION
# ===============================
def bacterial_growth(rate, antibiotic_effect):
    od_values = []
    od = 0.05  # initial OD600

    for t in time:
        noise = random.uniform(-0.01, 0.01)

        # Growth calculation with antibiotic effect
        od = od + (rate * od * (1 - antibiotic_effect)) + noise

        if od < 0:
            od = 0

        od_values.append(round(od, 3))

    return od_values
    # ===============================
# INPUT SECTION
# ===============================
print("\nChoose bacterial strain:")
print("1. Sensitive strain")
print("2. Resistant strain")
choice = input("Enter choice (1 or 2): ")
if choice not in ["1", "2"]:
    print("Invalid choice. Defaulting to Sensitive strain.")
    choice = "1"
# Parameters
if choice == "1":
    strain = "Sensitive"
    growth_rate = 0.35
    antibiotic_effect = 0.60
else:
    strain = "Resistant"
    growth_rate = 0.35
    antibiotic_effect = 0.15
# Generate OD600 curve
od_data = bacterial_growth(growth_rate, antibiotic_effect)    
# ===============================
# RESULTS OUTPUT
# ===============================
print(f"\nStrain Selected: {strain}")
print("\nTime (hrs)  |  OD600")
print("----------------------")
for t, od in zip(time, od_data):
    print(f"{t:>3}        |  {od}")
 # Plot growth curve
plt.figure(figsize=(8, 5))
plt.plot(time, od_data, marker="o", linewidth=2)
plt.title(f"OD600 Growth Curve - {strain} strain")
plt.xlabel("Time (hours)")
plt.ylabel("OD600")
plt.grid(True)
plt.tight_layout()
plt.show() 
print("\nSimulation completed successfully.")
print("OD600-based bacterial growth analysis finished.")
