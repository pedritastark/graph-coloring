#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:43:13 2023

@author: sebastianpedraza
"""

'Module for type annotations'
from typing import Dict, List, Optional, Type


'Module to find chromatic num'
from itertools import permutations


'Library to generate random graphs'
import random




'Libraries to plot graph'
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    
    def __init__(self, G: Dict[int, List[int]]):
        
        self.G = G
        
    
    def __str__(self, show: bool = False) -> Optional[Dict[int, List[int]]]:
        
        if not show:  return str(self.G)
        
        nx.draw(nx.Graph(self.G), nx.spring_layout(nx.Graph(self.G)), with_labels=True, node_color='blue', font_color='white')
        plt.show()
        
        return str(self.G)
        


    def visualize(self: Dict[int, List[int]], coloration: Dict[int, int] ) -> None:
        
        '''
        Description: Using networkx and matplotlib, we represent graphs using plots.
        
        Input: G = {v1: [adjacents node to v1], v2: [adjacents node to v2], ...,  n: [adjacents node to vn]}
        
        Output: graph chart
        
        '''
        
        G = nx.Graph(self.G)
        pos = nx.spring_layout(G)
        colors = [coloration.get(nodo, 0) for nodo in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=colors, cmap=plt.cm.rainbow, font_color='white')
        plt.show()    
        
        return None


    def greedy_coloring(self: Dict[int, List[int]], show = False) -> Dict[int, int]:
        
        '''
        Description: Greedy coloring algorithm
            
        Input: Defining a graph G to use the greedy coloring algorithm as follows: 
            G = {v1: [adjacents node to v1], v2: [adjacents node to v2], ...,  n: [adjacents node to vn]}
            
        Output: Coloring of the graph G in the form 
        coloration(G) = {v1: color, v2: color, vn: color}, where colors will be numbers.
        '''
    
        coloration  =   {}
        color       =   0
    
        while len(coloration) < len(self.G):
            color += 1
    
            for vertice, adjacents in self.G.items():
                if vertice not in coloration and all(coloration.get(x) != color for x in adjacents):
                    coloration[vertice] = color
                    
                    
        if show: self.visualize(coloration)

        return coloration
    
    

    
    
    
    def chromatic(self: Dict[int, List[int]], show: bool = False) -> int:   
    
        '''
        Description: Evaluating the k-coloring with every possible combination of the n vertices,
        we find the chromatic number, as at least one ordering of V(G) produces an optimal coloring.
            
        Input: Coloring of the graph G in the form 
        coloration(G) = {v1: color, v2: color, vn: color}, where colors will be numbers.
            
        Output: The minimum coloring among all orderings using the greedy coloring algorithm to find its coloring.
        '''
        
        sorts               =   [dict(permutation) for permutation in permutations(self.G.items())]
        coloration_results  =   [Graph(sort).greedy_coloring() for sort in sorts]
        chromatic           =   min(max(x.values()) for x in coloration_results)
        index               =   next(k for k, v in enumerate(coloration_results) if max(v.values()) == chromatic)
        coloration          =   coloration_results[index]
        
        if show : self.visualize(coloration)
        return coloration, chromatic


    @staticmethod
    def simple_graph_generator(n: int = 6) -> Type['Graph']:
        
        '''
        Description: We generate a graph in the following way:
        G = {v1: [adjacents node to v1], v2: [adjacents node to v2], ...,  n: [adjacents node to vn]},
        but not in ascending order, but randomly.
        
        Input: |V(G)| default = 7
            
        Output: G = {vi: [adjacents node to v1], vj: [adjacents node to v2], ...,  n: [adjacents node to vn]}
        '''
        
    
        graph   =   {}
        vertices   =   list(range(1, n + 1))
        
        for vertice in vertices:
            
            adjacents   = random.sample([v for v in vertices if v != vertice] + [vertice], min(random.randint(1, n - 1), len([v for v in vertices if v != vertice] + [vertice])))
            graph.setdefault(vertice, [])
            
            for adjacent in adjacents:
                graph.setdefault(adjacent, []).append(vertice)
                if vertice != adjacent: graph[vertice] = list(set(graph[vertice] + [adjacent]))
    
        return  Graph({key: sorted(list(set(value) - {key})) for key, value in sorted(graph.items())})






if __name__ == "__main__":
    
    
    '''
    Construction of some families of graphs for you to test the script , including petersen graph
    
    
    K_n : {i: [j for j in range(1, n + 1) if j != i] for i in range(1, n + 1)}

    C_n : {i: [i + 1, n] if i == 1 else [i - 1, i + 1] if 1 < i < n else [n - 1, 1] for i in range(1, n + 1)}
    
    P_n : {i: [i - 1, i + 1] if 1 < i < n else [n - 1] if i == n else [2] for i in range(1, n + 1)}
    
    
    petersen graph: {1: [2, 4, 3], 2: [1, 5, 9], 3: [1, 7, 8], 4: [1, 6, 10], 5: [2, 6, 8],
                     6: [4, 5, 7], 7: [3, 6, 9], 8: [3, 5, 10], 9: [2, 7, 10], 10: [4, 8, 9]}
    '''
    
    

    
    graph = Graph.simple_graph_generator()
    
    # print(graph.__str__(show=True))    
    # print(graph.greedy_coloring(True))
    graph.chromatic(True)

