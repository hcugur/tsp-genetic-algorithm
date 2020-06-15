from tsp.tsp.genetic_algorithm.individual import Individual
import networkx as nx


class Population:
  def __init__(self, pop_size = 25):
    self.population_size = pop_size
    self.individuals = []
    self.fittest = 0


  def initialize_population(self, graph_obj):
    for _ in range(self.population_size):
      individual = Individual(graph_obj)
      individual.create_random_genes()
      self.individuals.append(individual)


  def add_individual(self, individ):
    self.individuals.append(individ)


  def get_gene_list_of_individual(self, index):
    return self.individuals[index].get_genes_list()


  def remove_individual(self, index):
    if index >= 0 and index < len(self.individuals):
      del self.individuals[index]
    else:
      raise Exception("Index out of boundries!")


  def calculate_fitness(self):
    for individual in self.individuals:
      individual.calculate_fitness()


  def get_fittest_individual(self):
    return min(self.individuals, key=lambda x: x.get_fitness())


  def get_population_size(self):
    return self.population_size


  def get_individual_fitnesses(self):
    fitnesses = []
    n = self.get_population_size()
    for i in range(n):
      fitnesses.append(self.individuals[i].fitness)
    return fitnesses

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