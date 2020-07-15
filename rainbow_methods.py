# -*- coding: utf-8 -*-
'''
    File name: methods.py
    Author: Kasia Pekala
    Date last modified: 6/22/2018
    Python Version: 3.5
'''

import numpy as np
import math
import networkx as nx
import pprint as pp      
from matplotlib import pyplot as plt
from collections import Counter

def present_results(n,r):
    GG = find_coloring(n,r)
    lower_bound_TJ = TaoJiang(n,r)[0]
    print("\nGraf pełny o",n,"wierzchołkach.")
    print("Ma",(n*(n-1))/2,"krawędzi.")
    print("Będziemy kolorować na",lower_bound_TJ,"kolorów.")
    print("Tak by nie było gwiazdy TMC o",r+1,"krawędziach.\n")            
    print("WYNIK\n")
    print("Wykorzystano",how_many_colors_in_graph(GG),"kolorów.")
    print("\nPokolorowanie, lista krawędzi:")
    pp.pprint(GG.edges(data=True))
    print("\nPokolorowanie, macierz sąsiedztwa (0 - brak krawędzi):")
    print(matrix_colors(GG))
    print("\nLiczba kolorów na które są pokolorowane wszystkie krawędzie kolejnych wierzchołków")
    pp.pprint(stars_colorings(GG))
    mnod = max(stars_colorings(GG).values())
    print("\nNajwiększy tęczowy podgraf jest pokolorowany na:", mnod, "różnych kolorów.")    
    pos = nx.circular_layout(GG)
    edge_labels = nx.get_edge_attributes(GG,'color')
    plt.figure(figsize=(12,12))
    nx.draw(GG,pos,node_size=60,font_size=8) 
    nx.draw_networkx_edge_labels(GG, pos, edge_labels)
    #plt.savefig("Graph.pdf")
    #for line in nx.generate_edgelist(GG,data=['color']):
        #print(line)
    return

#generowanie pokolorowania zgodnie z metodą użytą w dowodzie twierdzenia    
def find_coloring(n,r):
    if (n<1) or (r>(n-2)):
        raise Exception("Złe parametry!")    
    F = split_nodes(n,r)
    # używamy różnych algorytmów w zależnosci od rodzajów parametrów
    if (n % 2 == 1) and (r % 2 == 0):
        G_res = coloring_C(F,n,r)
    else:
        G_res = coloring_A(F,n,r)
    return G_res

# podział zbioru wierzchołków      
def split_nodes(n,r):
    m = math.floor(n/(n-r+1))   
    K = nx.complete_graph(n)
    F = []
    last_one = n-(m-1)*(n-r+1)
    nodes = [x for x in range(0,last_one)]
    Temp = K.subgraph(nodes)
    F.append(Temp)    
    for i in range(1, m):
        nodes = [x for x in range((i-1)*(n-r+1)+last_one,i*(n-r+1)+last_one)]
        Temp = K.subgraph(nodes)       
        F.append(Temp)
    return F

def coloring_A(LoG,n,r):
    nod = LoG[0].number_of_nodes()
    F = nx.random_regular_graph(n-r,nod)
    for u, v in F.edges():
        F[u][v]['color']=1
    if (len(LoG)>1):
        for i in range(1,len(LoG)):        
            for u, v in LoG[i].edges():
                LoG[i][u][v]['color']=i+1  
        G = nx.union_all(LoG[1:])
        G = nx.union(F,G)
        i = i+2
    else:
        G = F
        i = 2
    K = nx.complete_graph(n)
    R = nx.difference(K,G)    
    for u, v in R.edges():
        R[u][v]['color']=i
        i=i+1
    G = nx.compose(R,G)    
    return G

def coloring_C(LoG,n,r):    
    nod = LoG[0].number_of_nodes()    
    C = nx.Graph()  
    C.add_nodes_from(LoG[0])
    for i in range(nod-1):
        C.add_edge(i,i+1)
    C.add_edge(0,nod-1)
    G = nx.difference(LoG[0],C)
    F = find_factor(G,n-r-1) #F'
    F.add_edge(nod-1,0)
    for i in range(0,nod-2,2):
        F.add_edge(i,i+1)
    for u, v in F.edges():
        F[u][v]['color']=1
    #kolorowanie pozostalych grafow F
    if (len(LoG)>1):
        for i in range(1,len(LoG)):        
            for u, v in LoG[i].edges():
                LoG[i][u][v]['color']=i+1  
        G = nx.union_all(LoG[1:])
        G = nx.union(F,G)
        i = i+2
    else:
        G = F
        i = 2
    K = nx.complete_graph(n)
    R = nx.difference(K,G)
    #kolorowanie pozostalych krawedzi
    for u, v in R.edges():
        R[u][v]['color']=i
        i=i+1
    G = nx.compose(R,G)        
    return G

#znajdowanie faktora (lemat 4.1.2)
def find_factor(G,t):
    n = len(G.nodes()) #liczba wierzchołków    
    m = G.degree(0) #stopień pierwszego wierzchołka
    if not is_graph_regular(G):
        print("graf nie jest regularny")
        return
    if (m % 2 != 0):
        print("stopnie grafu muszą być parzyste")
        return
    if t>m or t<2 or (t % 2 != 0):
        print("nieprawidłowy parametr t")
        return    
    if nx.is_connected(G):
        return find_factor_in_connected_graph(G,t)
    else:
        graphs = list(nx.connected_component_subgraphs(G))
        factor = []
        for i in range(len(graphs)):
            factor.append(find_factor_in_connected_graph(graphs[i],t))
        return(nx.union_all(factor[:]))    

#znajdywanie faktora w spójnym grafie
def find_factor_in_connected_graph(G,t):
    n = len(G.nodes()) #liczba wierzchołków    
    m = G.degree(G.nodes()[0]) #stopień pierwszego wierzchołka
    if not nx.is_connected(G):
        print("nie jest spójny")
        return        
    C = nx.eulerian_circuit(G)
    start = min(G.nodes())
    
    X = nx.Graph()  
    X.add_nodes_from(G)
    mapping_dict = {}
    for i in range(start,n+start):
        mapping_dict[i] = "x_"+str(i)
    X = nx.relabel_nodes(X,mapping_dict)

    Y = nx.Graph()  
    Y.add_nodes_from(G)
    mapping_dict = {}
    for i in range(start,n+start):
        mapping_dict[i] = "y_"+str(i)
    Y = nx.relabel_nodes(Y,mapping_dict)
    B = nx.union(X,Y)   
    
    for i, j in C: 
        B.add_edge("x_"+str(i),"y_"+str(j))

    H = [] #tworzymy m grafów H_i
    for i in range(B.degree(B.nodes()[0])):
        temp = nx.Graph()
        temp.add_nodes_from(B)
        H.append(temp)
    Bdiff = B
    E = nx.bipartite.maximum_matching(B)
    for k in range(B.degree(B.nodes()[0])):
        for i, j in E.items(): 
            H[k].add_edge(i,j)
        Bdiff = nx.difference(Bdiff,H[k])
        E = nx.bipartite.maximum_matching(Bdiff)
    
    res = nx.Graph()
    res.add_nodes_from(G)
    for k in range(int(t/2)):
        for i in H[k].nodes_iter():
            tmp = H[k].neighbors(i)[0]
            res.add_edge(int(i[2:]),int(tmp[2:]))
    return res

def is_graph_regular(G):
    graph_degrees = [d for n,d in G.degree_iter()]
    is_regular = all(graph_degrees[0] == item for item in graph_degrees)
    return(is_regular)

# wynik twierdzenia Tao Jiang
def TaoJiang(n,r):
    if (n<1) or (r>(n-2)):
        raise Exception("Złe parametry!")
    t = math.floor((2*n) / (n-r+1))
    if (n % 2 == 1) and (r % 2 == 0) and (t % 2 == 1):
        epsilon = 1
    else:
        epsilon = 0 
    lower_bound = math.floor(0.5*n*(r-1)) + math.floor((n/(n-r+1)))
    upper_bound = lower_bound + epsilon
    return (lower_bound,upper_bound)

# ile kolorów w pokolorowanym grafie
def how_many_colors_in_graph(G):
    graph_colors = nx.get_edge_attributes(G, 'color').values()
    number_of_colors = len(set(graph_colors))
    return number_of_colors

# macierz pokolorowania
def matrix_colors(G):
    n = len(G.nodes())    
    res = np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
            if (i!=j):
                res[i,j]=G.edge[i][j]['color']
    return res

# Liczba kolorów na które są pokolorowane wszystkie krawędzie 
# kolejnych wierzchołków
def stars_colorings(G):
    n_of_colors_per_node = {}
    for node in G.nodes():
        cols = []
        for u in G.neighbors(node):
            cols.append(G.edge[node][u]['color']) 
        nr_of_colors = len(set(cols))
        n_of_colors_per_node[node] = nr_of_colors
    return n_of_colors_per_node

def is_rainbow_star_included(G,r):
    is_included = False
    for i in range(len(stars_colorings(G).values())):
        if list(stars_colorings(G).values())[i]>r:
            is_included = True        
    return is_included

def count_colors_freq(G):    
    edge_list = G.edges(data=True)
    list_of_colors = list([d['color'] for d in [row[2] for row in edge_list]])
    return Counter(list_of_colors)

def describe_graph(G):
    print("\n",G.nodes())
    print("\n",G.edges(data=True))
    print("\n###","wierzchołki =", len(G.nodes()),"### krawędzie:",len(G.edges()))
    return 



    


    