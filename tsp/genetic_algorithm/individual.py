from tsp.tsp.xml_parser import graph_obj_assemble

import random

class Individual:
  def __init__(self, graph_obj):
    self.fitness = 0
    self.graph_obj = graph_obj
    self.genes = self.create_genes()
  

  def get_genes_list(self):
    return self.genes


  def get_fitness(self):
    return self.fitness


  def create_genes(self, *args): 
    if len(self.graph_obj.nodes) > 0:
      genes = []
      node_list = self.graph_obj.nodes

      genes = random.sample(node_list, len(node_list))
      # starting node is 'N0' so added to the beginning and the
      # end of the genes list
      genes.remove('N0')
      genes.append('N0')
      genes.insert(0, 'N0')
      return genes
    
    #self.genes = ['N0', 'N1', 'N241', 'N242', 'N243', 'N240', 'N239', 'N238', 'N237', 'N236', 'N235', 'N234', 'N233', 'N232', 'N231', 'N230', 'N245', 'N244', 'N246', 'N249', 'N250', 'N229', 'N228', 'N227', 'N226', 'N225', 'N224', 'N223', 'N222', 'N221', 'N220', 'N219', 'N218', 'N217', 'N216', 'N215', 'N214', 'N213', 'N212', 'N211', 'N210', 'N209', 'N206', 'N205', 'N204', 'N203', 'N202', 'N201', 'N200', 'N197', 'N196', 'N195', 'N194', 'N193', 'N192', 'N191', 'N190', 'N189', 'N188', 'N187', 'N186', 'N185', 'N184', 'N183', 'N182', 'N181', 'N180', 'N175', 'N179', 'N178', 'N149', 'N177', 'N176', 'N150', 'N151', 'N155', 'N152', 'N154', 'N153', 'N128', 'N129', 'N130', 'N19', 'N20', 'N127', 'N126', 'N125', 'N124', 'N123', 'N122', 'N121', 'N120', 'N119', 'N118', 'N156', 'N157', 'N158', 'N159', 'N174', 'N160', 'N161', 'N162', 'N163', 'N164', 'N165', 'N166', 'N167', 'N168', 'N169', 'N171', 'N170', 'N172', 'N173', 'N106', 'N105', 'N104', 'N103', 'N102', 'N101', 'N100', 'N99', 'N98', 'N97', 'N96', 'N95', 'N94', 'N93', 'N92', 'N91', 'N90', 'N89', 'N88', 'N108', 'N107', 'N109', 'N110', 'N111', 'N87', 'N86', 'N112', 'N113', 'N114', 'N116', 'N115', 'N85', 'N84', 'N83', 'N82', 'N81', 'N80', 'N79', 'N78', 'N77', 'N76', 'N75', 'N74', 'N73', 'N72', 'N71', 'N70', 'N69', 'N68', 'N67', 'N66', 'N65', 'N64', 'N63', 'N57', 'N56', 'N55', 'N54', 'N53', 'N52', 'N51', 'N50', 'N49', 'N48', 'N47', 'N46', 'N45', 'N44', 'N43', 'N58', 'N62', 'N61', 'N117', 'N60', 'N59', 'N42', 'N41', 'N40', 'N39', 'N38', 'N37', 'N36', 'N35', 'N34', 'N33', 'N32', 'N31', 'N30', 'N29', 'N28', 'N27', 'N26', 'N25', 'N21', 'N24', 'N22', 'N23', 'N13', 'N14', 'N12', 'N11', 'N10', 'N9', 'N8', 'N7', 'N6', 'N5', 'N4', 'N3', 'N276', 'N275', 'N274', 'N273', 'N272', 'N271', 'N270', 'N15', 'N16', 'N17', 'N18', 'N131', 'N132', 'N133', 'N269', 'N268', 'N134', 'N135', 'N267', 'N266', 'N136', 'N137', 'N138', 'N148', 'N147', 'N146', 'N145', 'N144', 'N198', 'N199', 'N143', 'N142', 'N141', 'N140', 'N139', 'N265', 'N264', 'N263', 'N262', 'N261', 'N260', 'N259', 'N258', 'N257', 'N256', 'N253', 'N252', 'N207', 'N208', 'N251', 'N254', 'N255', 'N248', 'N247', 'N277', 'N278', 'N2', 'N279', 'N0']

  def calculate_fitness(self):
    i = 0
    while i != len(self.genes) - 2:
      i += 1
      cost = self.graph_obj.get_edge_data(self.genes[i], self.genes[i + 1])['weight']
      self.fitness += round(float(cost))




'''
if __name__ == "__main__":
  graph_obj = graph_obj_assemble()
  obj = Individual(graph_obj)
  obj.create_genes()
  obj.calculate_fitness()
  print(obj.get_fitness())

'''


  