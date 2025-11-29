from __future__ import annotations

import gzip
from pathlib import Path
import os
import sys

from src.graph import Graph

def simple_CLI() -> None:
    
    while True:
        print("\nOptions: [1] Dijkstra  [2] A*  [q] quit")
        choice = input("Select: ").strip().lower()
        if choice == "q":
            break

        start = input("Start node: ").strip()
        goal = input("Goal node: ").strip()

        try:

            if choice == "1":
                dist, path, dur = g.dijkstra_shortest_path(start, goal)
                print(f"Dijkstra dist={dist}, time={dur:.3f}s, path_len={len(path) if isinstance(path, list) else 'N/A'}")
            elif choice == "2":
                dist, path, dur = g.astar_with_landmarks(start, goal)
                print(f"A* dist={dist}, time={dur:.3f}s, path_len={len(path) if isinstance(path, list) else 'N/A'}")
            else:
                print("Invalid choice")

        except Exception as exc:
            print(f"Error: {exc}")
            continue  # skips to next iteration





if __name__ == "__main__":
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    # print(current_dir)
    # src_path = os.path.join(current_dir, 'src')
    # print(src_path)
    # # extract_nodes()


    # determine relative paths for source and output files
    BASE_DIR = Path(__file__).resolve().parent
    SOURCE_PATH = BASE_DIR / "data" / "gplus_combined.txt"

    # ensure the source dataset exists
    if not SOURCE_PATH.exists():
        raise FileNotFoundError(f"Missing dataset: {SOURCE_PATH}")


    g = Graph()

    g.load_from_file(SOURCE_PATH)

    simple_CLI()
