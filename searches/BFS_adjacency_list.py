class BFS_Graph_AdjList:
    def __init__(self):
        self.vertex = {} # set up the graph as a dictionary
    
    def __repr__(self):
        print_string = ''
        for v in self.vertex:
            for adj in self.vertex[v]:
                print_string += ("{0} --> {1}; edge weight {2}\n".format(v,adj[0],adj[1]))
        return print_string
        
    def add_vertex(self,v):
        if not v in self.vertex:
            self.vertex[v] = []
        else:
            raise Exception('Vertex already exists')
    
    def add_edge(self,v1,v2,e=1):
        if (not v1 in self.vertex) or (not v2 in self.vertex):
            raise Exception('The vertices do not exist')
        new_edge = [v2,e]
        self.vertex[v1].append(new_edge)

    def BFS(self,start):
        if not start in self.vertex:
            raise Exception('Starting vertex not found in graph')

        visited = {start:0}
        next = [start]
        level = 0
        while next:
            node = next.pop(0)
            level = visited[node] + 1 # traversing through the next step of vertices from the current vertex
            for adj in self.vertex[node]:
                if not adj[0] in visited:
                    next.append(adj[0])
                    visited[adj[0]] = level
        return visited

    def BFS_shortest(self,v1,v2):
        if (not v1 in self.vertex) or (not v2 in self.vertex):
            raise Exception('Vertices are not in the graph')
            
        next = [v1] # queue of the next vertices to reach
        visited = {v1:1} # store the vertices that have reached
        parent = {v1:None} # store the parent vertex of the vertices
        while next: # while there are still outstanding vertices waiting to be reached
            vertex = next.pop(0) # return the top vertice in the next queue (aka next vertice in the level)
            for adj in self.vertex[vertex]:
                if not adj[0] in visited:
                    next.append(adj[0])
                    visited[adj[0]] = 1 # put all adjacent vertices in visited here because you have already reached the vertices by adding them in the next queue
                    parent[adj[0]] = vertex # specify the parent vertex of the adjacent vertices - for finding a shortest path

            if vertex == v2: # that means you have reached the destination vertex; since next queue adds all the vertex that are before the destination vertex
                path = []
                while vertex in parent: # if the vertex has a parent, that means it has not reached the starting vertex yet; keep on finding its parent vertex
                    path.insert(0,vertex) # add the current vertex into the path first, before going to its parent vertex
                    vertex = parent[vertex]
                return path
            if vertex in visited: # skip the vertex that has already been reached, because another vertex already added this vertix to the next queue
                continue

        return -1

bfs_graph = BFS_Graph_AdjList()
bfs_graph.add_vertex('A')
bfs_graph.add_vertex('B')
bfs_graph.add_vertex('C')
bfs_graph.add_vertex('D')
bfs_graph.add_vertex('E')
bfs_graph.add_vertex('F')

bfs_graph.add_edge('A','B')
bfs_graph.add_edge('A','D')
bfs_graph.add_edge('A','E')
bfs_graph.add_edge('B','A')
bfs_graph.add_edge('B','E')
bfs_graph.add_edge('C','E')
bfs_graph.add_edge('C','F')
bfs_graph.add_edge('D','A')
bfs_graph.add_edge('D','E')
bfs_graph.add_edge('E','B')
bfs_graph.add_edge('E','A')
bfs_graph.add_edge('E','D')
bfs_graph.add_edge('E','C')
bfs_graph.add_edge('F','C')

print (bfs_graph)
print (bfs_graph.BFS('A'))
print (bfs_graph.BFS_shortest('A','F'))