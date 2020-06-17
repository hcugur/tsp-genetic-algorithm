import random

def mutate(gene_list):
  n = len(gene_list)
  swap_index_1 = random.randint(1, n - 2)
  swap_index_2 = random.randint(1, n - 2)
  
  while swap_index_1 == swap_index_2:
    swap_index_2 = random.randint(1, n - 2)

  swap(gene_list, swap_index_1, swap_index_2)


def swap(lst, index_1, index_2):
  temp = lst[index_1]
  lst[index_1] = lst[index_2]
  lst[index_2] = temp