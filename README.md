# Smart City Route Optimizer

## About the program
This program finds the **shortest flight route** between any two cities in a network of 10 European and African cities. It also calculates the **estimated fuel cost** using probability and predicts the **travel time** using linear regression.

## The Problem It Solves
> "What is the shortest flight route between two cities, how much will it cost, and how long will it take?"

This is the same problem solved by **airlines and flight booking systems** every day. Not every city has a direct flight to every other city, sometimes you need to connect through other cities. Therefore, this program finds the optimal path for you.

## How Connections Work
- A **number** between two cities means there is a direct flight between them
- A **0** means there is no direct flight, so the program will find a connecting route
- All distances are in **kilometres (km)**

## Mathematical Concepts Used
| Topic | How It's Used |
|---|---|
| Matrices | 10x10 distance matrix storing all direct flight connections |
| Vectors | NumPy arrays used in Dijkstra and Linear Regression |
| Optimisation | Dijkstra's algorithm finds the minimum distance path |
| Normal Distribution | Fuel cost estimated using a 90% confidence interval and Z-score of 1.645 |
| Linear Regression | Travel time predicted using y = mx + c trained on real flight data |

## Cities in the Network
| Index | City | Continent |
|---|---|---|
| 0 | London | Europe |
| 1 | Paris | Europe |
| 2 | Berlin | Europe |
| 3 | Rome | Europe |
| 4 | Zurich | Europe |
| 5 | Casablanca | Africa |
| 6 | Cairo | Africa |
| 7 | Lagos | Africa |
| 8 | Nairobi | Africa |
| 9 | Johannesburg | Africa |

## Project Structure
```
city-route-optimizer/
│
├── main.py        # The complete Python program
└── README.md      # Project description and instructions
```

## How to Run

### Step 1 - Install requirements
```
pip install numpy
```

### Step 2 - Run the program
```
python main.py
```

### Step 3 - Follow the prompts
Example:
```
Enter START city (name or number): London
Enter DESTINATION city (name or number): Nairobi
```

## Example Output
```
==================================================
   SHORTEST ROUTE FOUND
--------------------------------------------------
From     : London
To       : Nairobi
Route    : London => Rome => Cairo => Nairobi
Distance : 7,125 km
--------------------------------------------------
LEG BY LEG BREAKDOWN:
  London          => Rome               1434 km
  Rome            => Cairo              2065 km
  Cairo           => Nairobi            3626 km
                    TOTAL DISTANCE     7125 km
==================================================

FUEL COST ESTIMATE
--------------------------------------------------
Average expected cost :  $  605.63 USD
90% confidence range  :  $  486.07 - $  725.18 USD
Price variation       :  12% standard deviation
--------------------------------------------------
There is a 90% probability the fuel cost for this
7,125 km journey will fall between $486.07 and $725.18 USD
Based on Normal Distribution, Z-score = 1.645

TRAVEL TIME ESTIMATE
--------------------------------------------------
Formula used   : y = mx + c
Estimated time : 14h 45min
A 7,125 km journey is predicted to take approximately 14 hours and 45 minutes
==================================================
```

## Future Plans
- Add road and rail connections so users can choose their preferred mode of travel
- Expand the city network beyond Europe and Africa
- Add a visual map of the route
 ---
 <div align="right">
  <b><i>Created by J'Isabelle<i></b><br>

</div>
