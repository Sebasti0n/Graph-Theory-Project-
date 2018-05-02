""" This ifle should implement Prim's algorithm."""
from prims_functions import cost, min_valid_incident_edge


 # Calling sets from weighted graph
VT = G.vertex_set()
ET = G.edge_set()


def Prims(G):
   
    # Initalization
    T = {0}  
    E = []
    Tree =(T, E) #tuple

total = 0
while Tree[0] != VT:
   #Finding min cost edge incident to vertex. 
    min_edge = min_valid_incident_edge(G, Tree)
    
    if min_edge[0] not in VT:
        VT.add(min_edge[0]) #Finding new vertex 
        
    if min_edge[1] not in VT: # Finding next vertex 
        VT.add(min_edge[1])
    ET.append(min_edge)
    
print('Result: ',VT,ET)

G.draw_subgraph(Tree)
#return cost[min_edge]


    
    
