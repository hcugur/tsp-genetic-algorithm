from tsp.tsp.genetic_algorithm.population import Population
import networkx as nx

G = nx.Graph()
nodes = ['N0', 'N1', 'N2', 'N3']
weighted_edges = [('N0', 'N1', 1), ('N0', 'N2', 2), ('N0', 'N3', 3),
                  ('N1', 'N2', 4), ('N1', 'N3', 5), ('N2', 'N3', 6)]
G.add_nodes_from(nodes)
G.add_weighted_edges_from(weighted_edges)


def test_population_class():
  p = Population()

  assert p 


def test_initialize_population():
  p = Population()
  p.initialize_population(G)

  assert len(p.individuals) > 0


def test_calculate_fitness():
  p = Population()
  p.initialize_population(G)
  p.calculate_fitness()

  assert all(individual.fitness > 0 for (individual) in p.individuals)


def test_get_fittest_individual():
  p = Population()
  p.initialize_population(G)
  p.calculate_fitness()

  fittest = p.get_fittest_individual()

  assert fittest == min(p.individuals, key=lambda x: x.get_fitness()).get_fitness()