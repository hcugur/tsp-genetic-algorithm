from tsp.tsp.genetic_algorithm.genetic_algorithm import GeneticAlgorithm
from tsp.tsp.xml_parser import graph_obj_assemble

import sys

filename = sys.argv[1]
try:
  iteration_count = int(sys.argv[2])
except:
  iteration_count = 750

try:
  mut_rate = float(sys.argv[3])
except:
  pass

try:
  pop_size = int(sys.argv[4])
except:
  pass
'''
print('Filename: ', filename)
print('Iteration count: ', iteration_count)

'''
graph_obj = graph_obj_assemble(filename)


if mut_rate:
  ga = GeneticAlgorithm(mutation_rate=mut_rate)
else:
  ga = GeneticAlgorithm()

if pop_size:
  ga = GeneticAlgorithm(population_size=pop_size)
else:
  ga = GeneticAlgorithm()

ga.initialize_population(graph_obj)
ga.calculate_fitness()
print('Initial generation fittest individual: ', ga.get_fittest_individual_fitness_val())


for _ in range(iteration_count):
  ga.selection()
  ga.crossover()
  ga.mutation()
  ga.calculate_fitness()
  fittest = ga.get_fittest_individual_fitness_val()
  ga.increase_generation()
  print('Generation {gen} fittest individual fitness value: {value}'.format(gen=ga.generation, value=fittest))

print('Generation {gen} fittest individual: {value}'.format(gen=ga.generation, value=ga.get_fittest_individual_genes()))