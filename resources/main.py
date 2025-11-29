from __future__ import annotations

import gzip
from pathlib import Path
import os
import sys

from src.graph import Graph

def extract_nodes() -> None:

    # the database can be found here: https://snap.stanford.edu/data/ego-Gplus.html
    # only download the "gplus_combined.txt.gz" file into the "data" folder.

    # determine relative paths for source and output files
    BASE_DIR = Path(__file__).resolve().parent
    SOURCE_PATH = BASE_DIR / "data" / "gplus_combined.txt"

    # ensure the source dataset exists
    if not SOURCE_PATH.exists():
        raise FileNotFoundError(f"Missing dataset: {SOURCE_PATH}")


    # TODO: When we create a graph structure/adjancency list, we can load it here instead of re-parsing the edge list.
    g = Graph()
    g.load_from_file(SOURCE_PATH)

    
    # nodes: set[str] = set()

    # # Stream the edge list and persist all unique node ids.
    # with gzip.open(SOURCE_PATH, "rt") as fh:
    #     for index, line in enumerate(fh, start=1):
    #         parts = line.strip().split()
    #         if len(parts) != 2:
    #             continue  # Skip malformed lines.

    #         # TODO: Once we have the adjacency list/graph structure we can do the updates here 
    #         nodes.update(parts)

    #         # Print a progress update every million edges processed.
    #         if index % 1_000_000 == 0:
    #             print(
    #                 f"Processed {index:,} edges; found {len(nodes):,} unique nodes",
    #                 end="\r",
    #             )


    # print(
    #     f"\nNodes processed: {len(nodes):,} \n"
    #     f"(source: {SOURCE_PATH})."
    # )





if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(current_dir)
    src_path = os.path.join(current_dir, 'src')
    print(src_path)
    extract_nodes()
