# BMI Calculator for multiple people

# Invented data: name, weight (kg), height (meters)
people = [
    {"name": "Alice", "weight": 60, "height": 1.65},
    {"name": "Bob", "weight": 85, "height": 1.80},
    {"name": "Charlie", "weight": 72, "height": 1.75},
    {"name": "Diana", "weight": 55, "height": 1.60},
    {"name": "Emma", "weight": 95, "height": 1.70}
]

# Calculate BMI for each person
for person in people:
    bmi = person["weight"] / (person["height"] ** 2)

