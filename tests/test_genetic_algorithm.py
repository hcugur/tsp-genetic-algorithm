import networkx as nx 
import numpy as np
from tsp.tsp.genetic_algorithm.genetic_algorithm import GeneticAlgorithm


G = nx.Graph()
nodes = ['N0', 'N1', 'N2', 'N3']
weighted_edges = [('N0', 'N1', 1), ('N0', 'N2', 2), ('N0', 'N3', 3),
                  ('N1', 'N2', 4), ('N1', 'N3', 5), ('N2', 'N3', 6)]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(weighted_edges)


genetic_algorithm = GeneticAlgorithm()


def test_genetic_algorithm_class():

  assert genetic_algorithm


def test_initialize_population():
  genetic_algorithm.initialize_population(G)

  assert genetic_algorithm.graph_obj
  assert len(genetic_algorithm.population.individuals) > 0


def test_parent_selection():
  genetic_algorithm = GeneticAlgorithm()
  genetic_algorithm.initialize_population(G)
  genetic_algorithm.calculate_fitness()
  genetic_algorithm.selection()

  assert len(genetic_algorithm.parents) > 24