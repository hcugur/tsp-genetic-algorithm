from tsp.tsp.genetic_algorithm.individual import Individual
import networkx as nx


class Population:
  def __init__(self, pop_size = 25):
    self.population_size = pop_size
    self.individuals = []
    self.fittest = 0


  def initialize_population(self, graph_obj):
    for _ in range(self.population_size):
      self.individuals.append(Individual(graph_obj))


  def calculate_fitness(self):
    for individual in self.individuals:
      individual.calculate_fitness()


  def get_fittest_individual(self):
    return min(self.individuals, key=lambda x: x.get_fitness()).get_fitness()

'''
if __name__ == "__main__":
  G = nx.Graph()
  nodes = ['N0', 'N1', 'N2', 'N3']
  weighted_edges = [('N0', 'N1', 1), ('N0', 'N2', 2), ('N0', 'N3', 3),
                    ('N1', 'N2', 4), ('N1', 'N3', 5), ('N2', 'N3', 6)]
  G.add_nodes_from(nodes)
  G.add_weighted_edges_from(weighted_edges)

  p = Population(pop_size=10)
  p.initialize_population(G)
  p.calculate_fitness()
  p.get_fittest_individual()
'''