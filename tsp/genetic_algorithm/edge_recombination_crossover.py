import copy
import random


def get_neighbors(parent_1, parent_2):
  result = {}
  parent_1 = copy.copy(parent_1)
  parent_2 = copy.copy(parent_2)
  parent_1.pop()
  parent_2.pop()
  n = len(parent_1)
  
  for i in range(n):
    temp_list = []

    prev_index = (i - 1) % n
    next_index = (i + 1) % n
    
    temp_list.append(parent_1[prev_index])
    temp_list.append(parent_1[next_index])

    result[parent_1[i]] = temp_list
  
  for i in range(n):
    prev_index = (i - 1) % n
    next_index = (i + 1) % n

    result[parent_2[i]].append(parent_2[prev_index])
    result[parent_2[i]].append(parent_2[next_index])

    result[parent_2[i]] = list(set(result[parent_2[i]]))

  return result


def assemble_child_chromosome(neighbor_list, first_element):
  result = []
  neighbors = copy.deepcopy(neighbor_list)
  key_list = _populate_key_list(neighbors)
  element = first_element
  i = 0
  count = len(neighbors)
  
  while i < count:
    i += 1
    result.append(element)
    remove_item_from_neighbors(element, neighbors)
    
    if not neighbors[element]:
        key_list.remove(element)
        if key_list:
          new_element = random.choice(key_list)
        else:
          pass
    else:
      key_list.remove(element)
      new_element = _find_fewest_neighbor(element, neighbors)

    element = new_element

  result.append(first_element)
  
  return result


def _populate_key_list(neighbor_list):
  result = []
  for key in neighbor_list:
    result.append(key)
  return result


def _find_fewest_neighbor(cur_key, neighbor_list):
  neighbors = neighbor_list[cur_key]
  neighbor_numbers = []
  
  for item in neighbors:
    neighbor_numbers.append(len(neighbor_list[item]))
  
  min_index = _get_minimum_index(neighbor_numbers)

  return neighbors[min_index]


def _get_minimum_index(lst):
  n = len(lst)
  min_item = min(lst)
  for i in range(n):
    if lst[i] == min_item:
      return i
  

def remove_item_from_neighbors(item, neighbor_list):
  for key in neighbor_list:
    try:
      neighbor_list[key].remove(item)
    except:
      pass
  return neighbor_list


