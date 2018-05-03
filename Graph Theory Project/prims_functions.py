"""This file should store all the functions taht you write which will be needed 
 in the steps of Prim's algorithm"""
 
from Weighted_Graph import*
                                 #This is importing the weighted graph
G = Weighted_Graph('test.txt')
G.draw_graph()


def cost(G, e): #Determines the cost for Edges
    return G.edge_dict()[e]
#print("cost function at (0,1)", cost(G, (0,1))) -- Example 
    
def initial_tree(initial_vertex): #This will pick where the inital vertex is
    return ({initial_vertex}, [])


def incident_edges(G, T): #This finds any incident edges
    
    edges = []
    for e in G.edge_set():
        for V in T[0]:
            if V in e: 
                edges.append(e)
    
    return [e for e in edges if e not in T[1]]

def valid_incident_edges(G, T): #This returns out the valid incident edges
    edges = []
    for e in incident_edges(G,T):
        if e[0] not in T[0] or e[1] not in T[0]:
            edges.append(e)
            
    return edges

def min_valid_incident_edge(G, T):  #This calculates the minimum cost     
    valid_edges = valid_incident_edges(G, T)
    min_edge = valid_edges[0]
    
    for e in valid_edges: 
        if cost(e) < cost(min_edge):
            min_edge = e
            
    return min_edge


    
#do not add edges that make a cycle in the tree function 

"""
Want (v,W)
if V and W not in V(T)
7(V e V(T) and W e V(T))
"""
