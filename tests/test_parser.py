import pytest
from tsp.tsp.xml_parser import (
  graph_obj_init,
  parse,
  _create_node_list,
  _node_naming,
  graph_obj_assemble
)


def test_graph_obj_init():
  obj = graph_obj_init()
  assert obj is not None


def test_parse():
  vertex_list = parse()
  assert len(vertex_list) > 0
  assert vertex_list[0].tag == 'vertex'


def test_create_node_list():
  vertex_list = parse()
  node_list = _create_node_list(vertex_list)
  number_of_nodes = len(node_list)
  lower_bound = 'N' + str(0)
  upper_bound = 'N' + str(number_of_nodes - 1)
  assert lower_bound in node_list
  assert upper_bound in node_list


def test_node_naming():
  num_1 = 5
  num_2 = 10

  assert _node_naming(num_1) == 'N5'
  assert _node_naming(num_2) == 'N10'


def test_graph_obj_assemble():
  graph_obj = graph_obj_assemble()
  assert graph_obj.has_node('N0')
  assert graph_obj.has_node('N279')
  assert graph_obj.has_edge('N0', 'N1')
  assert graph_obj.has_edge('N0', 'N279')
  