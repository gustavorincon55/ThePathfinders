from __future__ import annotations
import os
from pathlib import Path
from flask import Flask, request, jsonify, send_file

from src.graph import Graph

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
SOURCE_PATH = BASE_DIR / "data" / "gplus_combined.txt"

if not SOURCE_PATH.exists():
    raise FileNotFoundError(f"Missing dataset: {SOURCE_PATH}")

g = Graph()
g.load_from_file(SOURCE_PATH)

@app.route('/', methods=['GET'])
def home():
    return send_file(os.path.join(BASE_DIR, 'static', 'index.html'))

@app.route('/api/search', methods=['POST'])
def search_helper():


    data = request.json
    start_node = data.get('start')
    end_node = data.get('goal')
    mode = data.get('mode')
    algorithm = data.get('algorithm')

    if not start_node:
        return jsonify({"Error": "Start node are required."}), 400

    if mode == 'farthest':
        result = g.find_eccentricity(start_node)

        return jsonify(result)
    
    elif mode == 'shortest':
        if not end_node:
            return jsonify({"Error": "End node is required for shortest path search."}), 400
        
        if algorithm == 'astar':
            result = g.astar_with_landmarks(start_node, end_node)
        elif algorithm == 'dijkstra':
            result = g.dijkstra_shortest_path(start_node, end_node)


        return jsonify(result)
    


        


if __name__ == "__main__":
    
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=8899, debug=True)

import gzip
from pathlib import Path
