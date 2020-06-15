from tsp.tsp.genetic_algorithm.individual import Individual
from tsp.tsp.genetic_algorithm.population import Population
from tsp.tsp.genetic_algorithm.edge_recombination_crossover import (
  get_neighbors,
  assemble_child_chromosome
)
from tsp.tsp.genetic_algorithm.mutation import mutate



#import networkx as nx
import random
import numpy as np


class GeneticAlgorithm:
  def __init__(self, mutation_rate=0.1, population_size=75):
    self.population = Population(pop_size=population_size)
    self.generation = 0
    self.parents = []
    self.mutation_rate = mutation_rate


  def initialize_population(self, graph_obj):
    self.graph_obj = graph_obj
    self.population.initialize_population(self.graph_obj)


  def calculate_fitness(self):
    self.population.calculate_fitness()
    #print('fitnesses:', self.population.get_individual_fitnesses())


  def selection(self):
    self.population.individuals.sort(key=lambda x: x.get_fitness())
    weights = self._generate_parent_selection_weights()
    for i in range(self.population.get_population_size() - 1):
      #print('weigts: ', len(weights))
      #print('individuals: ', len(self.population.individuals))
      parent = np.random.choice(self.population.individuals, 2, p=weights)
      parent = parent.tolist()
      self.parents.append(parent)
    


  def crossover(self):
    children = self._generate_child_chromosome()
    self._remove_parents()
    self._remove_individuals()
    for i in range(len(children)):
      individual = Individual(self.graph_obj)
      individual.create_custom_genes(children[i])
      self.population.add_individual(individual)
    

  
  def mutation(self):
    n = self.population.get_population_size()
    for i in range(1, n):
      if random.random() < self.mutation_rate:
        individual = self.population.get_gene_list_of_individual(i)
        mutate(individual)


  def get_fittest_individual_fitness_val(self):
    return self.population.get_fittest_individual().get_fitness()


  def get_fittest_individual_genes(self):
    return self.population.get_fittest_individual().get_genes_list()

  def increase_generation(self):
    self.generation += 1


  def _remove_individuals(self):
    n = self.population.get_population_size()
    for i in range(n - 1, 0, -1):
      self.population.remove_individual(i)


  def _remove_parents(self):
    self.parents = []


  def _generate_child_chromosome(self):
    children = []
    for i in range(len(self.parents)):
      parent_1 = self.parents[i][0].get_genes_list()
      parent_2 = self.parents[i][1].get_genes_list()
      neighbor_list = get_neighbors(parent_1, parent_2)
      child = assemble_child_chromosome(neighbor_list, 'N0')
      children.append(child)
    return children
  

  def _generate_parent_selection_weights(self):
    population_size = self.population.get_population_size()
    result = []
    prob_sum = 1
    #result.append(0.25)
    for i in range(population_size):
      if prob_sum > 0:
        weight_value = self._weight_function(i)
        if weight_value < prob_sum:
          prob_sum -= weight_value
        else:
          weight_value = prob_sum
          prob_sum -= prob_sum
      else:
        weight_value = 0
      result.append(weight_value)
    for i in range(2):
      result[i] += prob_sum / 2
    return result


  def _weight_function(self, index):
    pop_size = self.population.get_population_size()
    return (1 / (index + 2) ** 2)  


'''   
if __name__ == "__main__":
  G = nx.Graph()
  nodes = ['N0', 'N1', 'N2', 'N3']
  weighted_edges = [('N0', 'N1', 1), ('N0', 'N2', 2), ('N0', 'N3', 3),
                    ('N1', 'N2', 4), ('N1', 'N3', 5), ('N2', 'N3', 6)]
  G.add_nodes_from(nodes)
  G.add_weighted_edges_from(weighted_edges)

  g_a = GeneticAlgorithm()
  g_a.selection(G)
  print(g_a.parents)
'''
