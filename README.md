# Smart City Route Optimizer 

## What This Program Does
This program finds the **shortest flight route** between any two cities
in a network of 10 European and African cities.
It also calculates the **estimated fuel cost** for the journey.

## The Problem It Solves
> "What is the shortest and cheapest flight route between two cities?"

This is the same problem solved by **airlines and flight booking systems** every day.
Not every city has a direct flight to every other city — sometimes you need
to connect through other cities. This program finds the optimal path for you.

## How Connections Work
- A **number** between two cities means there is a direct flight between them
- A **0** means there is no direct flight — the program will find a connecting route
- All distances are in **kilometres (km)**

## Mathematics Used (MFC 2026)
| Topic | How It's Used |
|---|---|
| Matrices | 10×10 distance matrix storing all direct flight connections |
| Vectors | NumPy arrays for distance calculations |
| Optimisation | Dijkstra's algorithm finds the minimum distance path |

## Cities in the Network
🇬🇧 London | 🇫🇷 Paris | 🇩🇪 Berlin | 🇮🇹 Rome | 🇨🇭 Zurich
🇲🇦 Casablanca | 🇪🇬 Cairo | 🇳🇬 Lagos | 🇰🇪 Nairobi | 🇿🇦 Johannesburg

## How to Run
```bash
python main.py
```

## Requirements
```bash
pip install numpy
```

## Example Output
```
Enter START city : London
Enter DESTINATION: Nairobi

SHORTEST PATH FOUND
Route    : London → Rome → Cairo → Nairobi
Distance : 6,469 km
Fuel Cost: $485 - $560
```