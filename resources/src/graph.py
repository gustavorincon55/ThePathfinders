import os
import glob
import heapq
from collections import defaultdict
import time
from math import floor, inf

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

                            # if len( unique_edges_tracker) % 1_000_000 == 0:
                            if floor((len(unique_edges_tracker)/13673453) *100) % 1 == 0:
                                print(
                                    f"Processed {len(unique_edges_tracker):,} edges ({((len(unique_edges_tracker)/13673453) *100):,.1f}%); found {len(self.adjacency_list):,} unique nodes ({((len(self.adjacency_list)/107614)*100):,.1f}%)",
                                    end="\r",
                                    )



                            
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
    

    def _bfs_distances(self, source):
        """Unweighted BFS distances from source to all reachable nodes."""
        dist = {source: 0}
        q = [source]
        for node in q:
            for nbr in self.adjacency_list[node]:
                if nbr not in dist:
                    dist[nbr] = dist[node] + 1
                    q.append(nbr)
        return dist

    def astar_with_landmarks(self, start, goal):
        """
        A* search using a landmark heuristic (ALT).
        landmark_distances: {landmark: {node: distance}} precomputed via _bfs_distances.
        Returns (distance or None, path or message, duration_sec).
        """

        landmarks = [111091089527727420853,
    105237212888595777019,
    106189723444098348646,
    104987932455782713675,
    109813896768294978296,
    107117483540235115863,
    112063946124358686266,
    101261243957067319422,
    101849747879612982297,
    118418436905562612953,
    102476152658204495450,
    113116318008017777871,
    113686253941057080055,
    109412257237874861202,
    109895887909967698705,
    113455290791279442483,
    110286587261352351537,
    100535338638690515335,
    118207880179234484610,
    108176814619778619437,
    109330684746468207713,
    110318982509514011806,
    113612142759476883204,
    102518365620075109973,
    107362628080904735459,
    112374836634096795698,
    100962871525684315897,
    101035196437264488455,
    105076678694475690385,
    105390077271236874234,
    107234826207633309420,
    114536133164105123829,
    113040469867257447555,
    113622835120994907038
    ]

        # Landmarks picked with an algorithm to grab the farthest corners/end points of the graph.
        landmark_distances = {lm: _bfs_distances(lm) for lm in landmarks}




        if start not in self.adjacency_list or goal not in self.adjacency_list:
            return None, "Start or goal not in graph.", 0.0

        def heuristic(node):
            # Triangle inequality: h(n) = max |d(L, goal) - d(L, n)|
            vals = []
            for _, dist_map in landmark_distances.items():
                if goal in dist_map and node in dist_map:
                    vals.append(abs(dist_map[goal] - dist_map[node]))
            return max(vals) if vals else 0

        t0 = time.time()
        open_set = [(heuristic(start), 0, start)]  # (f, g, node)
        g_score = {start: 0}
        came_from = {}

        while open_set:
            f, g, current = heapq.heappop(open_set)
            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return g, path, time.time() - t0

            # Skip stale queue entries
            if g > g_score.get(current, inf):
                continue

            for nbr in self.adjacency_list[current]:
                tentative = g + 1
                if tentative < g_score.get(nbr, inf):
                    came_from[nbr] = current
                    g_score[nbr] = tentative
                    heapq.heappush(open_set, (tentative + heuristic(nbr), tentative, nbr))

        return None, "Path not found.", time.time() - t0


