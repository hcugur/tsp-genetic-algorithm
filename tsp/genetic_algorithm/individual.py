import random

from tsp.tsp.xml_parser import graph_obj_assemble


class Individual:
  def __init__(self, graph_obj):
    self.fitness = 0
    self.graph_obj = graph_obj
    self.genes = []
  

  def get_genes_list(self):
    return self.genes


  def get_fitness(self):
    return self.fitness


  def create_random_genes(self, *args): 
    if len(self.graph_obj.nodes) > 0:
      genes = []
      node_list = self.graph_obj.nodes

      genes = random.sample(node_list, len(node_list))
      # starting node is 'N0' so added to the beginning and the
      # end of the genes list
      genes.remove('N0')
      genes.insert(0, 'N0')
      genes.append('N0')
      self.genes = genes


  def create_custom_genes(self, gene_list):
    self.genes = gene_list


  def calculate_fitness(self):
    self.fitness = 0
    i = 0
    while i != len(self.genes) - 1:
      cost = self.graph_obj.get_edge_data(self.genes[i], self.genes[i + 1])['weight']
      self.fitness += round(float(cost))
      i += 1
