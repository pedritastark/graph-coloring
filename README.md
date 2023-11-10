# Graph Coloring
# Description
This repository is dedicated to the development of a tool and associated resources for encoding a Turing machine into binary sequences, and binary sequences to Turing machine.

# Motivation

In graph theory class, looking at graph coloring, We saw the greedy coloring algorithm and were asked to implement it in Python. This repository takes that implementation to the next level.

# Topics
You need basic knowledge in graph theory and have a clear understanding of the following:
## k-coloring

A k-coloring of a graph G is a labeling function
    
  - f: V(G) → S, where |S| = k.

The elements of S are the "colors."
Vertices with the same color form a color class.

## propper k-coloring
A k-coloring is proper if adjacent vertices have different labels:
      
  -  (∀u, v ∈ V(G))(u↔v → f(u) ≠ f(v))

