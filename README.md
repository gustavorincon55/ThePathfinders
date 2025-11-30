<h1>The Pathfinders</h1>

Members: Yangkai Xiang, Jacob Melendez, Gustavo Rincon.

Project Title: **Guided Search: A Performance Analysis of Dijkstra vs. A\* in Large-Scale Graphs**

---

## Overview
This project provides a comparative exploration of **Dijkstra’s Algorithm** and **A\*** on large-scale graph data. The system exposes a lightweight Flask API that loads a graph dataset, executes pathfinding queries, and returns results such as shortest paths and eccentricity searches.

The implementation is built around a custom `Graph` class and supports:
- Dijkstra shortest-path search
- A\* with landmark heuristics
- Eccentricity (farthest-node) queries
- A simple web interface served via Flask

---

## How to Run the Program
Below is the full setup and execution pipeline.

### **Step 1. Create and activate a virtual environment**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### **Step 2. Install dependencies**
```bash
pip install flask
```

### **Step 3. Project structure**
Your folder should resemble the following:
```
ThePathfinders/
├── main.py
├── src/
│   └── graph.py
├── data/
│   └── gplus_combined.txt
├── static/
│   └── index.html
└── README.md
```
Make sure the dataset file is placed in `data/` with the exact name expected by the code.

### **Step 4. Run the Flask server**
Inside the project directory:
```bash
python main.py
```

If everything loads correctly, the terminal will show the Flask debugger active. Then visit:
```
http://localhost:8899
```
This serves the `static/index.html` interface.

---

## API Endpoints
The backend exposes a small JSON-based API.

### **GET /**
Serves the main web interface.

### **POST /api/search**
Execute a graph search.

Request JSON format:
```json
{
  "start": "node_id",
  "goal": "node_id (optional)",
  "mode": "shortest" or "farthest",
  "algorithm": "dijkstra" or "astar"
}
```

### **Modes**
- **farthest** → returns the eccentricity (the farthest reachable node and distance)
- **shortest** → returns the shortest path; requires both `start` and `goal`

### **Algorithms**
- **dijkstra** → standard Dijkstra shortest-path
- **astar** → A\* with landmark-based heuristic

---

## Notes on Data Loading
The dataset is loaded exactly once at startup:
```python
g = Graph()
g.load_from_file(SOURCE_PATH)
```
This avoids repeated parsing and keeps queries fast.

If the dataset is missing, the server will raise:
```
FileNotFoundError: Missing dataset: data/gplus_combined.txt
```

---

## Future Work
Possible next steps for the project team:
- Expand benchmark tooling for Dijkstra vs. A\*
- Add visualization of paths and heuristics
- Integrate performance metrics in the frontend
- Document the `Graph` class methods in more detail

---

## Acknowledgments
This project was developed as part of The Pathfinders' exploration of algorithmic search performance in large real-world graphs for UF Online's COP 3503 Data Structures & Algorithms Project 3.

