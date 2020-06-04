import xml.etree.cElementTree as ET 
import networkx as nx
import os


def graph_obj_init():
  G = nx.Graph()
  return G 


def parse():
  os.chdir('../data/')
  main_tree = ET.parse('a280.xml')
  vertex_list = main_tree.getiterator('vertex')
  
  return vertex_list


def graph_obj_assemble():
  graph_obj = graph_obj_init()
  vertex_list = parse()

  node_list = _create_node_list(vertex_list)
  add_nodes_to_graph(graph_obj, node_list)

  add_edges_to_graph(graph_obj, vertex_list)

  return graph_obj


def add_nodes_to_graph(graph_obj, node_list):
  for node in node_list:
    graph_obj.add_node(node)
  

def _create_node_list(vertex_list):
  number_of_nodes = len(vertex_list)
  return list(map(_node_naming, range(number_of_nodes)))


def add_edges_to_graph(graph_obj, vertex_list):
  n = len(vertex_list)
  for i in range(n):
    element = vertex_list[i]
    for edge in element.iter('edge'):
      node_u = 'N' + str(i)
      node_v = 'N' + edge.text
      weight = edge.attrib['cost']
      graph_obj.add_edge(node_u, node_v, weight=weight)
  
  
def _node_naming(num):
  return 'N' + str(num)

'''
if __name__ == "__main__":
  parse()  
'''