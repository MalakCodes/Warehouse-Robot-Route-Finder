# Warehouse Robot Route Finder

## 1. Project Overview

Warehouse Robot Route Finder is an Artificial Intelligence project that simulates a robot navigating through a warehouse represented as a 10 × 10 grid.

The robot must find a valid route from its starting position to a selected storage zone while avoiding obstacles and considering different movement costs.

The project implements three search algorithms:
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search

The system selects the appropriate algorithm based on the user's preferences and provides an interactive interface using Streamlit.

## 2. Project Objectives

- Implement BFS, UCS, and A* search algorithms.
- Find valid routes while avoiding obstacles.
- Consider different movement costs.
- Allow users to select their search priorities.
- Compare algorithm performance.
- Evaluate the algorithms using different test cases.

## 3. Project Features

- 10 × 10 warehouse grid.
- Robot starting position.
- Three storage zones.
- Two charging stations.
- Obstacle cells that cannot be traversed.
- High-cost cells with a movement cost of 3.
- Automatic algorithm selection based on user preferences.
- Interactive warehouse visualization.
- Route reconstruction.
- Performance metrics and algorithm comparison.
- Detection of unreachable destinations.
- Input validation.

## 4. Search Algorithms

### 4.1 Breadth-First Search (BFS)

BFS explores the warehouse level by level and finds a path with the minimum number of steps.

### 4.2 Uniform Cost Search (UCS)

UCS considers the movement cost of each cell and finds a path with the minimum total movement cost.

### 4.3 A* Search

A* combines the actual movement cost with a heuristic function to guide the search toward the goal.

The project uses Manhattan Distance as its heuristic function.

## 5. Algorithm Selection

The system selects an algorithm based on the user's preferences:

- **Minimum Number of Steps:** Selects BFS.
- **Minimum Movement Cost:** The user chooses whether to use heuristic guidance:
  - Yes: Selects A*.
  - No: Selects UCS.

The selected algorithm is executed to find the route.

The system also runs all three algorithms separately in the performance comparison section.

## 6. Warehouse Grid Representation

The warehouse is represented as a 10 × 10 grid.

| Cell Type | Representation | Movement Cost |
|---|---|---|
| Ordinary Cell | 0 | 1 |
| High-Cost Cell | 3 | 3 |
| Obstacle | -1 | Not allowed |

The robot can move in four directions:
- Up
- Down
- Left
- Right

All positions use zero-based indexing and are represented as (row, column).

### Main Warehouse Locations

- Starting Position: (0, 1)
- Storage Zone S1: (0, 9)
- Storage Zone S2: (5, 9)
- Storage Zone S3: (9, 9)
- Charging Station C1: (0, 0)
- Charging Station C2: (9, 0)

## 7. Technologies Used

- Python
- Streamlit
- Pandas
- Breadth-First Search
- Uniform Cost Search
- A* Search
- Manhattan Distance Heuristic

## 8. Project Structure

```text
Warehouse-Robot-Route-Finder/
│
├── app.py
├── main.py
├── warehouse_grid.py
├── input_validation.py
├── path_reconstruction.py
│
├── bfs.py
├── ucs.py
├── a_star.py
│
├── test_bfs.py
├── test_a_star.py
├── test_input_validation.py
├── test_no_route.py
├── test_obstacle_density.py
│
└── README.md
```

### Main Files

- `app.py`: Provides the interactive Streamlit interface.
- `main.py`: Handles algorithm selection and execution.
- `warehouse_grid.py`: Defines the warehouse grid and its locations.
- `input_validation.py`: Validates user positions.
- `path_reconstruction.py`: Reconstructs the resulting path.
- `bfs.py`: Implements Breadth-First Search.
- `ucs.py`: Implements Uniform Cost Search.
- `a_star.py`: Implements A* Search.

### Test Files

- `test_bfs.py`: Tests BFS using reachable, weighted-cell, and same-start-and-goal cases.
- `test_a_star.py`: Tests A* using reachable, weighted, no-route, and UCS comparison cases.
- `test_input_validation.py`: Tests valid and invalid input positions.
- `test_no_route.py`: Tests how all three algorithms handle unreachable destinations.
- `test_obstacle_density.py`: Evaluates algorithm behavior under different obstacle counts.

## 9. Installation and Setup

### 9.1 Clone the Repository

```bash
git clone https://github.com/MalakCodes/Warehouse-Robot-Route-Finder.git
```

### 9.2 Navigate to the Project Directory

```bash
cd Warehouse-Robot-Route-Finder
```

### 9.3 Install Dependencies

```bash
python -m pip install streamlit pandas
```

## 10. How to Run the Application

Run the following command from the project directory:

```bash
python -m streamlit run app.py
```

The application will open in a web browser.

## 11. Running the Tests

Run the test files individually:

```bash
python test_bfs.py
python test_a_star.py
python test_input_validation.py
python test_no_route.py
python test_obstacle_density.py
```

The tests evaluate pathfinding behavior, movement costs, input validation, unreachable destinations, and different obstacle configurations.

## 12. Performance Metrics

The system measures and displays the following indicators:

- **Total Cost:** Total movement cost of the resulting path.
- **Steps:** Number of movements required to reach the destination.
- **Expanded Nodes:** Number of nodes expanded during the search.
- **Execution Time:** Time taken by the algorithm to find the route.

The application provides a comparison table and visualizations for BFS, UCS, and A*.

## 13. Project Team

- Malak Alotaibi
- Reem Alharthi
- Layal Albahsani
- Retaj Alansari
- Nouf Alotaibi
- Noura Alsalomi

## 14. Future Improvements

- Explore additional pathfinding algorithms.
- Improve warehouse visualization.
- Evaluate performance using more warehouse configurations.
- Extend the warehouse environment with additional scenarios.

## 15. Repository

GitHub Repository:

https://github.com/MalakCodes/Warehouse-Robot-Route-Finder
