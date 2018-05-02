"""
This file should store all the functions that you write which will be needed
in the steps of Prim's algorithm"
"""

from Weighted_Graph import*
G = Weighted_Graph("test.txt")

G.draw_graph()

#Variables for the function
V = G.vertex_set()      #Vertecies
E = G.edge_set()        #Edges
cost = G.edge_dict()    #weight
VT = {0}
ET = []

def incident_edges(VT, ET):     
    
    edges = []
    for v in VT:
        for e in E:
            if v in e and e not in ET:
                edges.append(e)
                
    E_valid = []
    for e in edges:
        if e[0] not in VT or e[1] not in VT:
            E_valid.append(e)
            
    return E_valid

print(incident_edges(VT, ET))

def min_incident_edges(incident_edges):
    min_cost_edge = incident_edges[0]
    for i in range(len(incident_edges)):
        if cost[incident_edges[i]] < cost[min_cost_edge]:
            min_cost_edge = incident_edges[i]
            
    return min_cost_edge
possible_edges = incident_edges(VT, ET)

print(min_incident_edges(possible_edges))

def add_valid_edge(VT, ET): #test to see if the graph plots
    incident_valid = incident_edges(VT, ET)
    min_edge = min_incident_edges(incident_valid)
    if min_edge[0] not in VT:
        VT.add(min_edge[0])
    if min_edge[1] not in VT:
        VT.add(min_edge[1])
    ET.append(min_edge)
    print('Result: ',VT,ET)
    return cost[min_edge]

total = 0
while VT != V:
    current = add_valid_edge(VT,ET)
    total = total + current
    print('Total :', total)
    
