
import streamlit as st

from warehouse_grid import create_warehouse_grid, get_warehouse_locations
import main

st.set_page_config(
    page_title="Warehouse Robot Route Finder",
    page_icon="",
    layout="wide"
)

st.title(" Warehouse Robot Route Finder")
st.write(
    "Find the best route for a warehouse robot "
    "using BFS, UCS, and A* search algorithms."
)

st.divider()

# Load warehouse data
grid = create_warehouse_grid()
locations = get_warehouse_locations()

start = locations["start"]
storage_zones = locations["storage_zones"]
charging_stations = set(locations["charging_stations"].values())

# User preferences
st.subheader("Search Preferences")

priority = st.radio(
    "1. What is your main priority?",
    options=["steps", "cost"],
    format_func=lambda x: (
        "Shortest Path (Fewest Steps)"
        if x == "steps"
        else "Lowest Movement Cost"
    )
)

use_heuristic = False

if priority == "cost":
    approach = st.radio(
        "2. Would you like to use a heuristic to guide the search?",
        options=["yes", "no"],
        format_func=lambda x: (
            "Yes, use heuristic guidance (A*)"
            if x == "yes"
            else "No, use actual movement costs only (UCS)"
        )
    )
    use_heuristic = approach == "yes"

# Target selection
goal_name = st.selectbox(
    "Select Target Storage Zone",
    options=list(storage_zones.keys())
)

goal = storage_zones[goal_name]

find_route = st.button("🔍 Find Route", type="primary")


def display_warehouse(grid, start, goal, locations, path=None):
    st.subheader("🏭 Warehouse Map")

    storage_zones = set(locations["storage_zones"].values())
    charging_stations = set(locations["charging_stations"].values())
    path = set(path or [])

    for row_index, row in enumerate(grid):
        cols = st.columns(10, gap="small")

        for col_index, cell in enumerate(row):
            position = (row_index, col_index)

            symbol = "·"
            background = "#e5e7eb"

            if cell == -1:
                symbol = "🚧"
                background = "#fecaca"

            elif cell == 3:
                symbol = "3"
                background = "#fed7aa"

            if position in charging_stations:
                symbol = "🔋"
                background = "#bfdbfe"

            if position in storage_zones:
                symbol = "📦"
                background = "#ddd6fe"

            if position in path:
                if cell == 3:
                 symbol = " 3🔹"
                elif cell == 0:
                 symbol = "🟦"
                background = "#93c5fd"

            if position == start:
                symbol = "🤖"
                background = "#bbf7d0"

            if position == goal:
                symbol = "🎯"
                background = "#fef08a"

            with cols[col_index]:
                st.markdown(
                    f"""
                    <div style="
                        background-color: {background};
                        height: 42px;
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        border-radius: 6px;
                        font-size: 20px;
                        margin-bottom: 5px;
                    ">
                        {symbol}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.caption(
        "🤖 Start | 🎯 Goal | 📦 Storage | 🔋 Charging "
        "| 🚧 Obstacle | 3 High-Cost Cell | 🟦 Route | · Free Cell"
    )


# Run selected algorithm
if find_route:
    result = main.run_algorithm(
        priority,
        grid,
        start,
        goal,
        use_heuristic
    )

    st.divider()
    st.subheader("Search Results")

    if result["found"]:
        st.success(
            f"Route found using {result['algorithm']}!"
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Cost", result["cost"])
        col2.metric("Steps", result["steps"])
        col3.metric("Expanded Nodes", result["expanded_nodes"])
        col4.metric(
            "Execution Time",
            f"{result['execution_time']:.6f} sec"
        )

        st.write("**Selected Algorithm:**", result["algorithm"])
        st.write("**Route:**", " → ".join(map(str, result["path"])))

        display_warehouse(
            grid, start, goal, locations, result["path"]
        )

    else:
        st.error("No valid route exists.")

        display_warehouse(
            grid, start, goal, locations
        )

else:
    display_warehouse(
        grid, start, goal, locations
    )
