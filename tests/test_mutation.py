from tsp.tsp.genetic_algorithm.mutation import (
  mutate,
  swap
)

import copy


genes = ['N0', 'N1', 'N5', 'N3', 'N4', 'N2']


def test_swap():
  gene_list = copy.copy(genes)
  swap(genes, 3, 5)

  assert genes == ['N0', 'N1', 'N5', 'N2', 'N4', 'N3']


def test_mutate():
  n = len(genes)
  gene_list = copy.copy(genes)
  mutate(gene_list)

  assert gene_list[0] == 'N0'
  assert len(list(set(gene_list))) == n