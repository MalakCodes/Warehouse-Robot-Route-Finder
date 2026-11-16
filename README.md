#Warehouse Robot Route Finder

## Project Overview
Warehouse Robot Route Finder is an Artificial Intelligence project that simulates a warehouse robot navigating through a grid-based warehouse to find a path from its starting position to a selected storage zone.

The project implements three search algorithms: Breadth-First Search (BFS), Uniform Cost Search (UCS), and A* Search. The system selects an algorithm based on the user's search preferences and displays the resulting route and performance metrics through an interactive Streamlit interface.

## Project Objectives
- Implement and compare BFS, UCS, and A* search algorithms.
- Find valid routes while avoiding obstacle cells.
- Consider different movement costs across warehouse cells.
- Allow users to select their preferred search strategy.
- Measure and display algorithm performance.

## Features
- 10 × 10 warehouse grid.
- Robot starting position and three storage zones.
- Two charging stations.
- Obstacle cells that the robot cannot pass through.
- High-cost cells with a movement cost of 3.
- Automatic algorithm selection based on user preferences.
- Interactive warehouse visualization.
- Route reconstruction and performance measurement.
- Handling of cases where no valid route exists.

## Search Algorithms

### 1. Breadth-First Search (BFS)
BFS explores the warehouse level by level and finds a path with the fewest number of steps.

### 2. Uniform Cost Search (UCS)
UCS considers movement costs and finds a path with the lowest total movement cost.

### 3. A* Search
A* combines the actual movement cost with a heuristic function to guide the search toward the target. The project uses Manhattan Distance as its heuristic.

## Algorithm Selection
The system asks the user about their search preferences:

- **Shortest Path (Fewest Steps):** Selects BFS.
- **Lowest Movement Cost:** Asks whether to use heuristic guidance:
  - Yes: Selects A*.
  - No: Selects UCS.

## Warehouse Grid
The warehouse is represented as a 10 × 10 grid with the following cell types:

| Cell Type | Representation | Movement Cost |
|---|---|---:|
| Free Cell | 0 | 1 |
| Obstacle | -1 | Not allowed |
| High-Cost Cell | 3 | 3 |
| Start | Robot position | — |
| Storage Zone | Target position | — |
| Charging Station | Charging location | — |

The robot can move in four directions: up, down, left, and right.

## Technologies Used
- Python
- Streamlit
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search

## Project Structure

```text
Warehouse-Robot-Route-Finder/
│
├── app.py
├── main.py
├── warehouse_grid.py
├── input_validation.py
├── path_reconstruction.py
├── bfs.py
├── ucs.py
├── a_star.py
├── test_a_star.py
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MalakCodes/Warehouse-Robot-Route-Finder.git
```

### 2. Navigate to the Project Directory

```bash
cd Warehouse-Robot-Route-Finder
```

### 3. Install Dependencies

```bash
python -m pip install streamlit
```

## How to Run the Project

Run the following command in the project directory:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Performance Metrics
The system displays the following metrics after executing a search algorithm:

- **Total Cost:** Total movement cost of the selected route.
- **Steps:** Number of movements required to reach the target.
- **Expanded Nodes:** Number of nodes expanded during the search.
- **Execution Time:** Time taken by the algorithm to find the route.

## Project Team
(Add team members' names here.)

## Future Improvements
- Conduct detailed performance comparisons under different obstacle configurations.
- Improve warehouse visualization.
- Explore additional pathfinding algorithms.
