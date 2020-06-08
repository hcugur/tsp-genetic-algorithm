#from tsp.tsp.xml_parser import graph_obj_assemble
from tsp.tsp.genetic_algorithm.individual import Individual
import networkx as nx


G = nx.Graph()
nodes = ['N0', 'N1', 'N2', 'N3']
weighted_edges = [('N0', 'N1', 1), ('N0', 'N2', 2), ('N0', 'N3', 3),
                  ('N1', 'N2', 4), ('N1', 'N3', 5), ('N2', 'N3', 6)]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(weighted_edges)
  
def test_individual_class():
  graph_obj = G

  individual = Individual(graph_obj)

  assert individual


def test_create_genes():
  graph_obj = G

  individual = Individual(graph_obj)
  genes_list = individual.create_genes()

  assert genes_list.count('N1') == 1 and genes_list.count('N2') == 1 and genes_list.count('N3') == 1 and genes_list.count('N0') == 2
  assert genes_list[0] == 'N0' and genes_list[-1] == 'N0'


def test_calculate_fitness():
  graph_obj = G

  individual = Individual(graph_obj)
  individual.calculate_fitness()

  assert individual.fitness > 0


def test_get_genes_list():
  graph_obj = G

  individual = Individual(graph_obj)
  genes_list = individual.get_genes_list()

  assert genes_list.count('N1') == 1 and genes_list.count('N2') == 1 and genes_list.count('N3') == 1 and genes_list.count('N0') == 2
  assert genes_list[0] == 'N0' and genes_list[-1] == 'N0'


def test_get_fitness():
  graph_obj = G

  individual = Individual(graph_obj)
  individual.calculate_fitness()
  fitness = individual.get_fitness()

  assert fitness > 0