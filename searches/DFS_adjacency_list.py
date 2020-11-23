class DFS_Graph_AdjList:
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

    def DFS_visit(self,start,parent,level):
        if not start in self.vertex:
            raise Exception('Vertex is not in graph')
        level += 1
        for adj in self.vertex[start]:
            if not adj[0] in parent:
                parent[adj[0]] = [start,level]
                self.DFS_visit(adj[0],parent,level)
    
    def DFS(self):
        parent = {}
        for vertex in self.vertex:
            if not vertex in parent:
                parent[vertex] = [None,0]
                self.DFS_visit(vertex,parent,0)
        return parent

    def DFS_path(self,start,end,parent={},level=0):
        if not start in self.vertex:
            raise Exception('Vertex is not in graph')
        
        if level == 0:
            parent[start] = None

        if start == end:
            return True
        
        level += 1
        for adj in self.vertex[start]:
            if not adj[0] in parent:
                parent[adj[0]] = start
                if self.DFS_path(adj[0],end,parent,level): # how to escape early from a recursion
                    return parent.keys()
        


dfs_graph = DFS_Graph_AdjList()
dfs_graph.add_vertex('A')
dfs_graph.add_vertex('B')
dfs_graph.add_vertex('C')
dfs_graph.add_vertex('D')
dfs_graph.add_vertex('E')
dfs_graph.add_vertex('F')

dfs_graph.add_edge('A','B')
dfs_graph.add_edge('A','D')
dfs_graph.add_edge('A','E')
dfs_graph.add_edge('B','A')
dfs_graph.add_edge('B','E')
dfs_graph.add_edge('C','E')
dfs_graph.add_edge('C','F')
dfs_graph.add_edge('D','A')
dfs_graph.add_edge('D','E')
dfs_graph.add_edge('E','B')
dfs_graph.add_edge('E','A')
dfs_graph.add_edge('E','D')
dfs_graph.add_edge('E','C')
dfs_graph.add_edge('F','C')

print (dfs_graph.DFS())
print (dfs_graph.DFS_path('A','G'))