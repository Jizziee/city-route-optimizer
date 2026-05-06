
# ============================================================
# SMART CITY ROUTE OPTIMIZER
#
# ============================================================
# PROBLEM: Given a network of cities, find the shortest route
#          between any two cities and calculate the fuel cost.
#
# REAL WORLD USE: This is how Google Maps, GPS systems, and
#                 delivery companies plan their routes every day.
#
# MATHEMATICAL CONCEPTS USED:
#   - Matrices & Vectors: Store city distances
#   - Optimisation: Find the minimum cost path

# ============================================================

import numpy as np  # NumPy lets us create and work with matrices
 
# ============================================================
# STEP 1: DEFINE THE CITIES
# ============================================================
# We store our 10 cities in a Python LIST.
# A list is just a collection of items in a specific order.
# Each city has an INDEX number (its position in the list):
#   London = 0, Paris = 1, Berlin = 2 ... and so on.
# We use these index numbers to look up distances in the matrix.
 
cities = [
    "London",        # index 0
    "Paris",         # index 1
    "Berlin",        # index 2
    "Rome",          # index 3
    "Zurich",        # index 4
    "Casablanca",    # index 5
    "Cairo",         # index 6
    "Lagos",         # index 7
    "Nairobi",       # index 8
    "Johannesburg"   # index 9
]
 
# ============================================================
# STEP 2: BUILD THE DISTANCE MATRIX (Week 1 - Matrices)
# ============================================================
# This is the mathematical HEART of the program.
#
# A matrix is a table of numbers arranged in rows and columns.
# Our matrix is 10x10 (10 rows, 10 columns) — one row and one
# column for each city.
#
# HOW TO READ IT:
#   distance_matrix[i][j] = distance in km from city i to city j
#   Example: distance_matrix[0][1] = 344 means
#            London (index 0) to Paris (index 1) = 344 km
#
# RULES:
#   - distance_matrix[i][i] = 0 (a city is 0 km from itself)
#   - 0 elsewhere means NO direct connection between those cities
#   - The matrix is SYMMETRIC: distance A→B = distance B→A
#     This means distance_matrix[i][j] = distance_matrix[j][i]
#
# These are approximate real-world distances in kilometres.
 
distance_matrix = np.array([
#         Lon   Par   Ber   Rom   Zur   Cas   Cai   Lag   Nai   Joh
         [0,    344,  932,  1434, 776,  2092, 0,    0,    0,    0   ],  # London
         [344,  0,    878,  1105, 490,  1761, 3200, 0,    0,    0   ],  # Paris
         [932,  878,  0,    1184, 520,  0,    0,    0,    0,    0   ],  # Berlin
         [1434, 1105, 1184, 0,    690,  0,    2065, 0,    0,    0   ],  # Rome
         [776,  490,  520,  690,  0,    0,    0,    0,    0,    0   ],  # Zurich
         [2092, 1761, 0,    0,    0,    0,    3741, 2900, 0,    0   ],  # Casablanca
         [0,    3200, 0,    2065, 0,    3741, 0,    0,    3626, 0   ],  # Cairo
         [0,    0,    0,    0,    0,    2900, 0,    0,    3982, 0   ],  # Lagos
         [0,    0,    0,    0,    0,    0,    3626, 3982, 0,    3900],  # Nairobi
         [0,    0,    0,    0,    0,    0,    0,    0,    3900, 0   ],  # Johannesburg
], dtype=float)
 
# ============================================================
# STEP 3: DISPLAY THE CITIES TO THE USER
# ============================================================
# This function prints the list of available cities nicely.
# A function is a reusable block of code we can call anytime.
 
def show_cities():
    print("\n  AVAILABLE CITIES:")
    print("  " + "-" * 35)
    # Loop through each city and print its number and name
    for i, city in enumerate(cities):
        print(f"  [{i}] {city}")
    print("  " + "-" * 35)
 
# ============================================================
# QUICK TEST - Let's make sure everything works so far
# ============================================================
print("Cities loaded:", len(cities), "cities")
print("Matrix shape :", distance_matrix.shape)
print("Example: London to Paris =", distance_matrix[0][1], "km")
show_cities()