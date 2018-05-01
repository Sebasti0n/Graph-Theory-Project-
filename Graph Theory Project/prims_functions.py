from Weighted_Graph import* 

G = Weighted_Graph('test.text')

G.draw_graph()

def cost(G, e):
    return G.edge_dict()[e]
#print("cost function at (0,1)", cost(G, (0,1)))
    
def initial_tree(initial_vertex):
    return ({initial_vertex}, [])
print(initial_tree(3))

def incident_edges(G, T):
    
    edges = []
    for e in G.edge_set():
        for V in T[0]:
            if V in e: 
                edges.append(e)
    
    return [e for e in edges if e not in T[1]]

print(incident_edges(G, initial_tree(0)))

def valid_incident_edges(G, T):
    edges = []
    for e in incident_edges(G,T):
        if e[0] not in T[0] or e[1] not in T[0]:
            edges.append(e)
            
    return edges

print(valid_incident_edges(G, T))

def min_valid_incident_edge(G, T):
    valid_edges = valid_incident_edges(G, T)
    min_edge = valid_edges[0]
    
    for e in valid_edges: 
        if cost(e) < cost(min_edge):
            min_edge = e
            
    return min_edge

print(min_valid_incident_edge(G,T))
    
    
#do not add edges that make a cycle in the tree function 

"""
Want (v,W)

if V and W not in V(T)
7(V e V(T) and W e V(T))

"""