'''
    File name: rainbow_example.py
    Author: Kasia Pekala
    Date last modified: 4/19/2018
    Python Version: 3.5
'''

import os
#os.chdir("")
import rainbow_methods as rm
import networkx as nx
import pprint as pp      
from matplotlib import pyplot as plt


#%%

print("Rozważamy graf o 9 wierzchołkach i 4 krawędziach")
print("Dolne ograniczenie liczby kolorów wynosi:",rm.TaoJiang(9,4)[0])
print("Górne ograniczenie liczby kolorów wynosi:",rm.TaoJiang(9,4)[1])
print("(Twierdzenie 4.2.1)")
print("\nImportujemy trzy różne pokolorowania uzyskane za pomocą programowania matematycznego.")
print("Różnicę między kolejnymi pokolorowaniami widać dzięki sprawdzeniu ile razy został użyty każdy kolor.")

#%%
print("Pierwszy przykład pokolorowania")
G = nx.read_edgelist('solution_extracted_21.txt', nodetype=int, data=(('color',int),))
pp.pprint(G.edges(data=True))
print("\nIle razy został wykorzystany dany kolor:")
print(sorted(rm.count_colors_freq(G).values(),reverse=True))
print("\nNa ile różnych kolorów są pokolorowane gwiazdy o zadanym wymiarze:")
print(sorted(rm.stars_colorings(G).values(),reverse=True))

pos = nx.shell_layout(G)
edge_labels = nx.get_edge_attributes(G,'color')
plt.figure(2, figsize=(12,12))
nx.draw(G,pos,node_size=60,font_size=8) 
nx.draw_networkx_edge_labels(G, pos, edge_labels)

#%%

print("Drugi przykład pokolorowania")
G = nx.read_edgelist('solution_extracted_22.txt', nodetype=int, data=(('color',int),))
pp.pprint(G.edges(data=True))
print("\nIle razy został wykorzystany dany kolor:")
print(sorted(rm.count_colors_freq(G).values(),reverse=True))
print("\nNa ile różnych kolorów są pokolorowane gwiazdy o zadanym wymiarze:")
print(sorted(rm.stars_colorings(G).values(),reverse=True))

pos = nx.shell_layout(G)
edge_labels = nx.get_edge_attributes(G,'color')
plt.figure(2, figsize=(12,12))
nx.draw(G,pos,node_size=60,font_size=8) 
nx.draw_networkx_edge_labels(G, pos, edge_labels)

#%%

print("Trzeci przykład pokolorowania")
G = nx.read_edgelist('solution_extracted_23.txt', nodetype=int, data=(('color',int),))
pp.pprint(G.edges(data=True))
print("\nIle razy został wykorzystany dany kolor:")
print(sorted(rm.count_colors_freq(G).values(),reverse=True))
print("\nNa ile różnych kolorów są pokolorowane gwiazdy o zadanym wymiarze:")
print(sorted(rm.stars_colorings(G).values(),reverse=True))

pos = nx.shell_layout(G)
edge_labels = nx.get_edge_attributes(G,'color')
plt.figure(2, figsize=(12,12))
nx.draw(G,pos,node_size=60,font_size=8) 
nx.draw_networkx_edge_labels(G, pos, edge_labels)
