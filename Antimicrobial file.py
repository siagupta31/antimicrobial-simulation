# Antimicrobial Resistance Simulation using OD600
# B.Tech Biotechnology Mini Project

import matplotlib.pyplot as plt
import random

print("🧫 ANTIBIOTIC RESISTANCE SIMULATOR (OD600 MODEL)")
print("------------------------------------------------")

# Time points (hours)
time = list(range(0, 13))  # 0 to 12 hours

# Function to simulate bacterial growth
def bacterial_growth(rate, antibiotic_effect):
    od_values = []
    od = 0.05  # initial OD600

    for t in time:
        noise = random.uniform(-0.01, 0.01)
        od = od + (rate * od * (1 - antibiotic_effect)) + noise

        if od < 0:
            od = 0

        od_values.append(round(od, 3))

    return od_values

# Input section
print("\nChoose bacterial strain:")
print("1. Sensitive strain")
print("2. Resistant strain")

choice = input("Enter choice (1 or 2): ")

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

# Print results
print(f"\n🧫 Strain Selected: {strain}")
print("\nTime (hrs)  |  OD600")
print("----------------------")

for t, od in zip(time, od_data):
    print(f"{t:>3}        |  {od}")

# Plot growth curve
plt.figure(figsize=(8, 5))
plt.plot(time, od_data, marker="o", linewidth=2, color="blue")
plt.title(f"OD600 Growth Curve - {strain} strain")
plt.xlabel("Time (hours)")
plt.ylabel("OD600")
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n✅ Simulation complete!")