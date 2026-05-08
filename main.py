
# ============================================================
# SMART CITY ROUTE OPTIMIZER
# ============================================================

import numpy as np  
 
# ============================================================
# STEP 1: DEFINED THE CITIES        # This stores our 10 cities in a Python LIST.
# ============================================================
 
 
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
# STEP 2: BUILT THE DISTANCE MATRIX                           # This stores the distances between cities in a 10x10 matrix
# ============================================================

# distance_matrix[i][i] = 0 (a city is 0 km from itself), 0 elsewhere means NO direct connection between those cities

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
# STEP 3: DISPLAY THE CITIES TO THE USER                     # This function prints the list of available cities.
# ============================================================

def show_cities():
    print("\n  AVAILABLE CITIES:")
    print("  " + "-" * 35)
   
    for i, city in enumerate(cities):
        print(f"  [{i}] {city}")
    print("  " + "-" * 35)
 

# ============================================================
# STEP 4: OPTIMISATION  (DIJKSTRA'S ALGORITHM)      # This function finds the SHORTEST path between two cities.
# ============================================================
 
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
 
    # We start with infinity for all cities (distances unknown), Then set the start city distance to 0
    dist = np.full(n, np.inf)  
    dist[start] = 0            
 
    # visited tells us which cities we have finalised and False = not yet visited, True = shortest distance confirmed

    visited = np.zeros(n, dtype=bool) 
 
    # previous stores which city we came from to reach each city. We use this at the end to trace back the full route

    previous = np.full(n, -1, dtype=int)  
 
    # ---- MAIN LOOP: runs once for each city ----
    for _ in range(n):       # We use NumPy to find unvistited city with the smallest distance and always pick the minimum
 
        unvisited_distances = np.where(visited, np.inf, dist)
        u = np.argmin(unvisited_distances)  # Index of closest city
 
        if dist[u] == np.inf:
            break

        visited[u] = True

        if u == end:
            break
 
        # UPDATE STEP: check all neighbours of city u
        for v in range(n):
            if distance_matrix[u][v] > 0 and not visited[v]:
 
                new_distance = dist[u] + distance_matrix[u][v]
 
                if new_distance < dist[v]:
                    dist[v] = new_distance
                    previous[v] = u  
 
    # ---- RECONSTRUCT THE ROUTE ----
    path = []
    current = end
    while current != -1:
        path.append(cities[current])  
        current = previous[current]   
    path.reverse()  
 
    if not path or path[0] != cities[start]:
        return np.inf, []
 
    return dist[end], path
 
 
# ============================================================
# STEP 5: GET CITY INPUT FROM USER                         # This function asks the user to type a city name or number. It also prevent crashes when uses type wrong inputs
# ============================================================

 
def get_city_input(prompt):
    
    while True:
        user_input = input(prompt).strip()
 
        if user_input.isdigit():
            index = int(user_input)
            if 0 <= index < len(cities):
                return index
            else:
                print(f"   Please enter a number between 0 and {len(cities)-1}")
 
        else:
            matches = [i for i, c in enumerate(cities)
                      if c.lower() == user_input.lower()]
            if matches:
                return matches[0]
            else:
                print(f"   '{user_input}' not found. Try again or use a number.")
 
# ============================================================
# STEP 6: DISPLAY THE ROUTE RESULTS                            #This function prints the results by showing the route, total distance and each leg of the journey.
# ============================================================
 
def display_results(path, total_distance):

    print("\n  " + "=" * 50)
    print("   SHORTEST ROUTE FOUND")
    print("  " + "-" * 50)
    print(f"  From     : {path[0]}")
    print(f"  To       : {path[-1]}")
    print(f"  Route    : {' → '.join(path)}")
    print(f"  Distance : {total_distance:,.0f} km")
    print("  " + "-" * 50)
 
   
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
# STEP 7: MAIN PROGRAM — WE PUT IT ALL TOGETHER AND ALLOW USER TO SEARCH AS MANY TIMES AS THEY WANT
# ============================================================

 
def main():
    print("\n" + "=" * 60)
    print("    SMART CITY ROUTE OPTIMIZER")
    print("=" * 60)
    print("   Find the shortest flight route between any two cities")
    print("=" * 60)
 
    
    while True:
 
        
        show_cities()
 

        print()
        start = get_city_input("  Enter START city (name or number): ")
 
        
        end = get_city_input("  Enter DESTINATION city (name or number): ")
 
        # Check they didn't pick the same city twice
        if start == end:
            print(f"\n  ⚠ You are already in {cities[start]}! Pick a different destination.")
            continue
 
        
        print(f"\n  Searching for shortest route from "
              f"{cities[start]} to {cities[end]}...")
 
        total_distance, path = dijkstra(start, end)
 
        
        if total_distance == np.inf or not path:
            print(f"\n  ✗ No route found between {cities[start]} "
                  f"and {cities[end]}.")
            print("  These cities may not be connected in our network.")
        else:
            
            display_results(path, total_distance)
            display_fuel_cost(total_distance)
            display_travel_time(total_distance)
 
        
        print()
        again = input("  Search another route? (yes / no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\n  Thank you for using Smart City Route Optimizer!")
            print("  " + "=" * 60)
            break
 
# ============================================================
# STEP 8: FUEL COST ESTIMATOR                              # Using normal distribution to estimante fuel cost
# ============================================================

 
def estimate_fuel_cost(distance_km):
   
 
    # ---- Constants ----
    COST_PER_KM   = 0.085   # Average fuel cost per km in USD
    VARIATION     = 0.12    # Fuel prices vary by ~12% (standard deviation)
    Z_SCORE_90    = 1.645   # Z-score for 90% confidence interval
                           
 
   
    mean_cost = distance_km * COST_PER_KM
 
  
    std_dev = mean_cost * VARIATION
 
    # THE PROBABILITY RANGE ----
    
    low_cost  = mean_cost - (Z_SCORE_90 * std_dev)
    high_cost = mean_cost + (Z_SCORE_90 * std_dev)
 
    return mean_cost, low_cost, high_cost
 
 
def display_fuel_cost(distance_km):
    
    mean_cost, low_cost, high_cost = estimate_fuel_cost(distance_km)
 
    print("\n  FUEL COST ESTIMATE")
    print("  " + "-" * 50)
    print(f"  Average expected cost : ${mean_cost:>8,.2f} USD")
    print(f"  90% confidence range  : ${low_cost:>7,.2f} - ${high_cost:,.2f} USD")
    print(f"  Cost per km           : $0.085 USD")
    print(f"  Price variation       : ±12% (std deviation)")
    print("  " + "-" * 50)
    print("   Interpretation:")
    print(f"  There is a 90% probability that the fuel cost for this {distance_km:,.0f} km journey will fall between ${low_cost:,.2f} and ${high_cost:,.2f} USD. Based on Normal Distribution, Z-score = 1.645")
    print("  " + "-" * 50)

# ============================================================
# STEP 9: TRAVEL TIME ESTIMATOR ( I used Linear Regression)
# ============================================================

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
    
    
    x = data[:, 0]  # First column  — distances, Second column — time
    y = data[:, 1]  

  
    x_mean = np.mean(x)
    y_mean = np.mean(y)

   
    numerator   = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)
    m = numerator / denominator

    
    c = y_mean - m * x_mean

    return m, c

def estimate_travel_time(distance_km):
    
    m, c = linear_regression(FLIGHT_DATA)

    
    hours = m * distance_km + c

    return hours, m, c

def display_travel_time(distance_km):
    
    hours, m, c = estimate_travel_time(distance_km)
    full_hours  = int(hours)
    minutes     = int((hours - full_hours) * 60)

    print("\n  TRAVEL TIME ESTIMATE ")
    print("  " + "-" * 50)
    print(f"  Formula used    : y = mx + c")
    print(f"  Slope (m)       : {m:.6f} hours per km")
    print(f"  Intercept (c)   : {c:.4f} hours (boarding time)")
    print(f"  Calculation     : {m:.6f} x {distance_km:,.0f} + {c:.4f}")
    print(f"  Estimated time  : {full_hours}h {minutes}min")
    print("  " + "-" * 50)
    print(f"  Using Linear Regression trained on real flight data,")
    print(f"  A {distance_km:,.0f} km journey is predicted to take approximately {full_hours} hours and {minutes} minutes.")
    print("  " + "-" * 50)
 
if __name__ == "__main__":
    main()
 