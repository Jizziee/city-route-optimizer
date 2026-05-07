
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
# STEP 4: OPTIMISATION  (DIJKSTRA'S ALGORITHM)      # This function finds the SHORTEST path between two cities.
# ============================================================
# WHY IS THIS OPTIMISATION?
#   Optimisation means finding the BEST solution from many possible options. Here we have hundreds of possible routes between two cities. Dijkstra finds the one with the MINIMUM total distance — that is optimisation.
#
# HOW IT WORKS:
#   1. Start at the source city with distance = 0
#   2. All other cities start with distance = infinity (unknown)
#   3. Always visit the UNVISITED city with SMALLEST distance
#   4. Check if going through this city gives shorter paths to its neighbours — if yes, update their distance
#   5. Repeat until we reach the destination
#   This GUARANTEES we find the true shortest path.
 
def dijkstra(start, end):
    """
    Finds the shortest path between two cities.
 
    Parameters:
        start : index number of the starting city
        end   : index number of the destination city
 
    Returns:
        total_distance : shortest distance in km
        path           : list of city names on the route
    """
 
    n = len(cities)  # Total number of cities (10)
 
    # dist is a NumPy VECTOR — one distance value per city
    # We start with infinity for all cities (distances unknown)
    # Then set the start city distance to 0
    dist = np.full(n, np.inf)  # [inf, inf, inf, inf, inf, ...]
    dist[start] = 0            # [0,   inf, inf, inf, inf, ...]
 
    # visited tells us which cities we have finalised
    # False = not yet visited, True = shortest distance confirmed
    visited = np.zeros(n, dtype=bool)  # [False, False, False, ...]
 
    # previous stores which city we came from to reach each city
    # We use this at the end to trace back the full route
    previous = np.full(n, -1, dtype=int)  # [-1, -1, -1, ...]
 
    # ---- MAIN LOOP: runs once for each city ----
    for _ in range(n):
 
        # OPTIMISATION STEP: find unvisited city with smallest distance
        # This is the KEY step — always pick the MINIMUM
        # We use NumPy to do this efficiently
        unvisited_distances = np.where(visited, np.inf, dist)
        u = np.argmin(unvisited_distances)  # Index of closest city
 
        # If smallest distance is infinity, no more reachable cities
        if dist[u] == np.inf:
            break
 
        # Mark this city as visited — its shortest distance is final
        visited[u] = True
 
        # If we just reached our destination, we can stop early
        if u == end:
            break
 
        # UPDATE STEP: check all neighbours of city u
        for v in range(n):
            # Only look at cities with a direct flight (distance > 0)
            # and that we haven't finalised yet
            if distance_matrix[u][v] > 0 and not visited[v]:
 
                # Calculate distance if we go through city u
                new_distance = dist[u] + distance_matrix[u][v]
 
                # If this new distance is SHORTER, update it
                # This is the RELAXATION step in optimisation
                if new_distance < dist[v]:
                    dist[v] = new_distance
                    previous[v] = u  # Remember we came from u
 
    # ---- RECONSTRUCT THE ROUTE ----
    # We trace backwards from destination to source
    # using the 'previous' array we built above
    path = []
    current = end
    while current != -1:
        path.append(cities[current])  # Add city name to path
        current = previous[current]   # Move to previous city
    path.reverse()  # Flip it so it reads start → end
 
    # Check if a valid path was found
    if not path or path[0] != cities[start]:
        return np.inf, []
 
    return dist[end], path
 
 
# ============================================================
# STEP 5: GET CITY INPUT FROM USER
# ============================================================
# This function asks the user to type a city name or number.
# It handles mistakes gracefully — if the user types something
# wrong, it simply asks again instead of crashing.
 
def get_city_input(prompt):
    """
    Asks the user to enter a city by name or number.
 
    Parameters:
        prompt : the question to show the user
 
    Returns:
        index of the chosen city
    """
    while True:
        user_input = input(prompt).strip()
 
        # Check if user typed a number (e.g. "0" for London)
        if user_input.isdigit():
            index = int(user_input)
            if 0 <= index < len(cities):
                return index
            else:
                print(f"  ⚠ Please enter a number between 0 and {len(cities)-1}")
 
        # Check if user typed a city name (case insensitive)
        # e.g. "london", "LONDON" and "London" all work
        else:
            matches = [i for i, c in enumerate(cities)
                      if c.lower() == user_input.lower()]
            if matches:
                return matches[0]
            else:
                print(f"  ⚠ '{user_input}' not found. Try again or use a number.")
 
# ============================================================
# STEP 6: DISPLAY THE ROUTE RESULTS
# ============================================================
# This function prints the results in a clear, readable format.
# It shows the route, total distance and each leg of the journey.
 
def display_results(path, total_distance):
    """
    Displays the shortest path results to the user.
 
    Parameters:
        path           : list of city names on the route
        total_distance : total distance in km
    """
    print("\n  " + "=" * 50)
    print("   SHORTEST ROUTE FOUND")
    print("  " + "-" * 50)
    print(f"  From     : {path[0]}")
    print(f"  To       : {path[-1]}")
    print(f"  Route    : {' → '.join(path)}")
    print(f"  Distance : {total_distance:,.0f} km")
    print("  " + "-" * 50)
 
    # Show leg by leg breakdown
    # A "leg" is one direct flight between two cities
    if len(path) > 2:
        print("  LEG BY LEG BREAKDOWN:")
        for i in range(len(path) - 1):
            city_a = cities.index(path[i])
            city_b = cities.index(path[i + 1])
            leg_km = distance_matrix[city_a][city_b]
            print(f"    {path[i]:<15} → {path[i+1]:<15} {leg_km:>6.0f} km")
        print(f"    {'TOTAL DISTANCE':>33} {total_distance:>6.0f} km")
    print("  " + "=" * 50)
 
# ============================================================
# STEP 7: MAIN PROGRAM — PUTTING IT ALL TOGETHER
# ============================================================
# This is where everything connects.
# We show the cities, take user input, run Dijkstra,
# and display the results. The user can search again
# as many times as they want.
 
def main():
    print("\n" + "=" * 60)
    print("   ✈  SMART CITY ROUTE OPTIMIZER")
    print("=" * 60)
    print("   Find the shortest flight route between any two cities")
    print("=" * 60)
 
    # Keep running until user says no
    while True:
 
        # Show available cities
        show_cities()
 
        # Get start city from user
        print()
        start = get_city_input("  Enter START city (name or number): ")
 
        # Get destination city from user
        end = get_city_input("  Enter DESTINATION city (name or number): ")
 
        # Check they didn't pick the same city twice
        if start == end:
            print(f"\n  ⚠ You are already in {cities[start]}! Pick a different destination.")
            continue
 
        # Run Dijkstra's algorithm to find shortest path
        print(f"\n  Searching for shortest route from "
              f"{cities[start]} to {cities[end]}...")
 
        total_distance, path = dijkstra(start, end)
 
        # Check if a route was found
        if total_distance == np.inf or not path:
            print(f"\n  ✗ No route found between {cities[start]} "
                  f"and {cities[end]}.")
            print("  These cities may not be connected in our network.")
        else:
            # Display the results
            display_results(path, total_distance)
            display_fuel_cost(total_distance)
            display_travel_time(total_distance)
 
        # Ask if user wants to search again
        print()
        again = input("  Search another route? (yes / no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n  Thank you for using Smart City Route Optimizer!")
            print("  " + "=" * 60)
            break
 
# ============================================================
# STEP 8: FUEL COST ESTIMATOR (Probability - Week 8 & 9)
# ============================================================
# REAL WORLD PROBLEM:
#   Fuel prices are never fixed — they vary daily due to oil prices, seasons, and demand. So instead of one fixed price we use PROBABILITY to give a realistic cost RANGE.

# MATHEMATICAL CONCEPT — Normal Distribution:
#   In real life, most values cluster around an average (mean) with fewer values far away. This is called a Normal Distribution — the famous "bell curve" shape.

#   For fuel costs:
#   - We calculate the MEAN cost based on distance
#   - We calculate the STANDARD DEVIATION (how much it varies)
#   - We then use these to give a 90% probability price range
#
# FORMULA USED:
#   mean     = distance × cost_per_km
#   std_dev  = mean × variation_rate
#   low  estimate = mean - (1.645 × std_dev)  ← 5th percentile
#   high estimate = mean + (1.645 × std_dev)  ← 95th percentile
#
#   1.645 is the Z-score for a 90% confidence interval
#   from the Standard Normal Distribution table (Week 8)
#
# This means: "We are 90% confident the fuel cost will fall
#              between the low and high estimate"
 
def estimate_fuel_cost(distance_km):
    """
    Estimates the fuel cost using Normal Distribution.
 
    Parameters:
        distance_km : total flight distance in kilometres
 
    Returns:
        mean_cost : average expected cost in USD
        low_cost  : lower bound (5th percentile)
        high_cost : upper bound (95th percentile)
    """
 
    # ---- Constants ----
    COST_PER_KM   = 0.085   # Average fuel cost per km in USD
    VARIATION     = 0.12    # Fuel prices vary by ~12% (standard deviation)
    Z_SCORE_90    = 1.645   # Z-score for 90% confidence interval
                            # From Normal Distribution table (Week 8)
 
    # ---- Step 1: Calculate the MEAN (expected average cost) ----
    # This is a simple linear relationship: cost = distance × rate
    mean_cost = distance_km * COST_PER_KM
 
    # ---- Step 2: Calculate STANDARD DEVIATION ----
    # Standard deviation tells us how spread out the prices are
    # A 12% variation means prices typically vary by 12% of the mean
    std_dev = mean_cost * VARIATION
 
    # ---- Step 3: Calculate the PROBABILITY RANGE ----
    # Using the Normal Distribution formula:
    # Lower bound = mean - (Z × std_dev) → 5th percentile
    # Upper bound = mean + (Z × std_dev) → 95th percentile
    # This gives us a 90% confidence interval
    low_cost  = mean_cost - (Z_SCORE_90 * std_dev)
    high_cost = mean_cost + (Z_SCORE_90 * std_dev)
 
    return mean_cost, low_cost, high_cost
 
 
def display_fuel_cost(distance_km):
    """
    Displays the fuel cost estimate with probability explanation.
 
    Parameters:
        distance_km : total flight distance in kilometres
    """
    mean_cost, low_cost, high_cost = estimate_fuel_cost(distance_km)
 
    print("\n  FUEL COST ESTIMATE (Normal Distribution)")
    print("  " + "-" * 50)
    print(f"  Average expected cost : ${mean_cost:>8,.2f} USD")
    print(f"  90% confidence range  : ${low_cost:>7,.2f} - ${high_cost:,.2f} USD")
    print(f"  Cost per km           : $0.085 USD")
    print(f"  Price variation       : ±12% (std deviation)")
    print("  " + "-" * 50)
    print("   Interpretation:")
    print(f"  There is a 90% probability that the fuel cost")
    print(f"  for this {distance_km:,.0f} km journey will fall")
    print(f"  between ${low_cost:,.2f} and ${high_cost:,.2f} USD.")
    print("  (Based on Normal Distribution, Z-score = 1.645)")
    print("  " + "-" * 50)

# ============================================================
# STEP 9: TRAVEL TIME ESTIMATOR (Linear Regression)
# ============================================================
# REAL WORLD PROBLEM:
#   A passenger needs to know how long their journey will take.
#   We use Linear Regression to predict travel time from distance.
#
# MATHEMATICAL CONCEPT — Linear Regression:
#   Linear Regression finds the best straight line relationship
#   between two variables. The formula is:
#
#       y = mx + c
#
#   Where:
#     y = travel time (what we want to predict)
#     x = distance in km (what we know)
#     m = slope (how much time increases per km)
#     c = intercept (base time e.g. boarding, taxiing)
#
#   We calculate m and c using the Linear Regression formula:
#
#       m = Σ((x - x_mean)(y - y_mean)) / Σ((x - x_mean)²)
#       c = y_mean - m × x_mean
#
#   This finds the line that BEST fits our known flight data.
#   NumPy vectors are used for all calculations.

# Known flight data (distance km, time hours) — training data
# These are real approximate flight times for reference
FLIGHT_DATA = np.array([
    [344,   1.5],   # London  → Paris
    [878,   2.5],   # Paris   → Berlin
    [1105,  2.8],   # Paris   → Rome
    [1184,  2.9],   # Berlin  → Rome
    [2065,  4.5],   # Rome    → Cairo
    [2092,  4.2],   # London  → Casablanca
    [2900,  6.0],   # Casablanca → Lagos
    [3200,  6.5],   # Paris   → Cairo
    [3626,  7.5],   # Cairo   → Nairobi
    [3900,  8.0],   # Nairobi → Johannesburg
    [3982,  8.2],   # Lagos   → Nairobi
])

def linear_regression(data):
    """
    Calculates slope (m) and intercept (c) for y = mx + c.

    Parameters:
        data : NumPy array with columns [distance, time]

    Returns:
        m : slope (hours per km)
        c : intercept (base hours)
    """
    # Split data into x (distance) and y (time) vectors
    x = data[:, 0]  # First column  — distances
    y = data[:, 1]  # Second column — times

    # Calculate means using NumPy
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate slope m using Linear Regression formula
    # m = Σ((x - x_mean)(y - y_mean)) / Σ((x - x_mean)²)
    numerator   = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    m = numerator / denominator

    # Calculate intercept c
    # c = y_mean - m × x_mean
    c = y_mean - m * x_mean

    return m, c

def estimate_travel_time(distance_km):
    """
    Predicts travel time using Linear Regression y = mx + c.

    Parameters:
        distance_km : total flight distance in kilometres

    Returns:
        hours : predicted travel time in hours
    """
    m, c = linear_regression(FLIGHT_DATA)

    # Apply the Linear Regression formula: y = mx + c
    hours = m * distance_km + c

    return hours, m, c

def display_travel_time(distance_km):
    """
    Displays the travel time prediction with explanation.

    Parameters:
        distance_km : total flight distance in kilometres
    """
    hours, m, c = estimate_travel_time(distance_km)
    full_hours  = int(hours)
    minutes     = int((hours - full_hours) * 60)

    print("\n  TRAVEL TIME ESTIMATE (Linear Regression)")
    print("  " + "-" * 50)
    print(f"  Formula used    : y = mx + c")
    print(f"  Slope (m)       : {m:.6f} hours per km")
    print(f"  Intercept (c)   : {c:.4f} hours (boarding time)")
    print(f"  Calculation     : {m:.6f} x {distance_km:,.0f} + {c:.4f}")
    print(f"  Estimated time  : {full_hours}h {minutes}min")
    print("  " + "-" * 50)
    print(f"  A {distance_km:,.0f} km journey is predicted to take")
    print(f"  approximately {full_hours} hours and {minutes} minutes.")
    print(f"  (Using Linear Regression trained on real flight data)")
    print("  " + "-" * 50)
 
if __name__ == "__main__":
    main()
 