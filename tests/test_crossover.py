from tsp.tsp.genetic_algorithm.edge_recombination_crossover import (
  get_neighbors, 
  assemble_child_chromosome,
  _populate_key_list,
  _get_minimum_index,
  _find_fewest_neighbor,
  remove_item_from_neighbors
  )

import collections
import copy


parent_1 = ['N0', 'N1', 'N5', 'N3', 'N4', 'N2', 'N0']
parent_2 = ['N0', 'N2', 'N3', 'N5', 'N1', 'N4', 'N0']


neighbors_dict = {
  'N0': ['N2', 'N1', 'N4'],
  'N1': ['N0', 'N5', 'N4'],
  'N2': ['N4', 'N0', 'N3'],
  'N3': ['N5', 'N4', 'N2'],
  'N4': ['N3', 'N2', 'N1', 'N0'],
  'N5': ['N1', 'N3']
}


amounts_1 = [7, 6, 2, 3, 1, 2, 5]
amounts_2 = [7, 6, 1, 3, 1, 2, 5]


def test_get_neighbors():
  neighbors = get_neighbors(parent_1, parent_2)
  
  assert collections.Counter(neighbors['N0']) == collections.Counter(['N2', 'N1', 'N4'])
  assert collections.Counter(neighbors['N5']) == collections.Counter(['N1', 'N3'])
  assert collections.Counter(neighbors['N3']) == collections.Counter(['N5', 'N4', 'N2'])


def test_child_chromosome():
  neighbors = copy.deepcopy(neighbors_dict)
  child_chromosome = assemble_child_chromosome(neighbors, 'N0')

  assert len(list(set(child_chromosome))) == len(neighbors)
  assert collections.Counter(child_chromosome) == collections.Counter(['N0', 'N1', 'N5', 'N3', 'N4', 'N2', 'N0'])


def test_populate_key_lis():
  key_list = _populate_key_list(neighbors_dict)
  control_list = ['N0', 'N1', 'N2', 'N3', 'N4', 'N5']
  assert collections.Counter(key_list) == collections.Counter(control_list)


def test_get_minimum_index():
  minimum_index_1 = _get_minimum_index(amounts_1)
  minimum_index_2 = _get_minimum_index(amounts_2)

  assert minimum_index_1 == 4
  assert minimum_index_2 == 2


def test_find_fewest_neighbor():
  neigbors = copy.deepcopy(neighbors_dict)
  neighbor_1 = _find_fewest_neighbor('N1', neigbors)
  neighbor_2 = _find_fewest_neighbor('N5', neigbors)

  assert neighbor_1 == 'N5'
  assert neighbor_2 == 'N1'


def test_remove_item_from_neighbors():
  neighbors = copy.deepcopy(neighbors_dict)
  removed_1 = remove_item_from_neighbors('N1', neighbors)
  
  for key in removed_1:
    assert 'N1' not in removed_1[key]