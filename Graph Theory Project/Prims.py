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

 #michaels attempt for Prims.py

from prims_fucntions import*

def Prims(textfile):
    
    total = 0
    A = []
    n = len(Graph)
    A = [[None for x in range(0, n)] for y in range(1, 4)]
   
    for x in range(1, n):
        A[0][x] = 'Y'
        A[1][x] = 0
        A[2][x] = 0

    for neighbour in Graph[1]: 
        A[1][neighbour-1] = 1
        A[2][neighbour-1] = Graph[1][neighbour]
        
    current = 1
    T = [current]
    MST_edges = {}
    count = 0
    while len(T) < n:
        x = search_min(current, A)
        T.append(x)
        MST_edges[x] = A[1][x]
        A[0][x] = 'N'
        total += A[2][x]
        
        for neighbour in Graph[x]:
            if A[0][neighbour-1] != 'N':
                if Graph[x][neighbour] < A[2][neighbour-1]:
                    A[1][neighbour-1] = x
                    A[2][neighbour-1] = Graph[x][neighbour]
        count += 1
        current = T[count]
    return ('Your MST is', total)
def search_min(current, A):
    minimum_cost = 100
    minimum_vertex = 1
    for x in range(1,len(A[0])):
        if A[1][x] != None and A[0][x] != 'N' and A[2][x] < minimum_cost:
                minimum_cost = A[2][x]
                minimum_vertex = x
                return minimum_vertex
            

    
    
