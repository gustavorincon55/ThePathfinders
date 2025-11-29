import os
import glob
import heapq
from collections import defaultdict
import time

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(set)
        self.num_nodes = 0
        self.nun_edges = 0

    def add_edge(self, u, v):
        self.adjacency_list[u].add(v)
        self.adjacency_list[v].add(u)

    def load_from_file(self, file_path):
        print(f"⌛ Starting graph data consolidation from {file_path}...")
        unique_edges_tracker = set() 
        
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    
                    if len(parts) == 2:
                        u, v = parts[0], parts[1]
                        edge = tuple(sorted((u, v)))
                        
                        if edge not in unique_edges_tracker:
                            self.add_edge(u, v) 
                            unique_edges_tracker.add(edge)
                            
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return
        
        self.num_edges = len(unique_edges_tracker)
        self.num_nodes = len(self.adjacency_list)
        print(f"Total Nodes: **{self.num_nodes:,}**")
        print(f"Total Edges (Undirected): **{self.num_edges:,}**")


    def load_from_directory(self, directory_path):
        print(f"⌛ Starting graph data consolidation from {directory_path}...")
        edge_files = glob.glob(os.path.join(directory_path, '**', '*.edges'), recursive=True)
        unique_edges_tracker = set() 
        
        for file_path in edge_files:
            try:
                with open(file_path, 'r') as f:
                    for line in f:
                        parts = line.strip().split()
                        
                        if len(parts) == 2:
                            u, v = parts[0], parts[1]
                            edge = tuple(sorted((u, v)))
                            
                            if edge not in unique_edges_tracker:
                                self.add_edge(u, v) 
                                unique_edges_tracker.add(edge)
                                
            except Exception as e:
                print(f"Warning: Could not read file {file_path}. Error: {e}")
                continue
        
        self.num_edges = len(unique_edges_tracker)
        self.num_nodes = len(self.adj_list)
        print(f"Total Nodes: **{self.num_nodes:,}**")
        print(f"Total Edges (Undirected): **{self.num_edges:,}**")

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, set())
    
    def is_directed_connected(self, u, v):
        return v in self.adjacency_list.get(u, set())
    
    def dijkstra_shortest_path(self, start_node, target_node):
        """
        Finds the shortest path between start_node and target_node using 
        Dijkstra's Algorithm. Since the graph is unweighted, all edges 
        are treated as weight 1.
        """

        start_time = time.time()

        if start_node not in self.adj_list or target_node not in self.adj_list:
            return None, "Start or target node not in graph."

        # Min-Priority Queue: stores tuples of (distance, node)
        pq = [(0, start_node)]
        
        # Dictionary to store the shortest distance found so far to each node
        distances = {node: float('inf') for node in self.adj_list}
        distances[start_node] = 0
        
        # Dictionary to reconstruct the path: stores {child: parent}
        predecessors = {}

        # 2. Main Loop
        while pq:
            # Extract the node with the smallest distance (O(log V))
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > distances[current_node]:
                continue
            
            if current_node == target_node:
                break

            for neighbor in self.adj_list[current_node]:
                new_distance = current_distance + 1
                
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (new_distance, neighbor))


        if target_node not in predecessors and start_node != target_node:
            return None, "Path not found."

        path = []
        node = target_node
        while node is not None:
            path.append(node)
            node = predecessors.get(node)
            if node == start_node:
                path.append(start_node)
                break
            
        path.reverse()

        end_time = time.time()
        duration = end_time - start_time
        print(f"⏱️ Dijkstra's Algorithm completed in {end_time - start_time:.2f} seconds.")
        
        return distances[target_node], path, duration
    
