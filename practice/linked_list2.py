class LinkedList:
  def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(data=nodes.pop(0))
      self.head = node
      for elem in nodes:
        node.next = Node(data=elem)
        node = node.next

  def __repr__(self):
    node = self.head
    nodes = []
    while node is not None:
      nodes.append(node.data)
      node = node.next
    
    nodes.append("None")
    return " -> ".join(nodes)

  def __iter__(self):
    node = self.head
    while node is not None:
      yield node
      node = node.next

  def add_first(self, node):
    node.next = self.head
    self.head = node

  def add_last(self, node):
    if self.head is None:
      self.head = node
      return
    for current_node in self:
      pass
    current_node.next = node
  
  def add_after(self, target_node_data, new_node):
    if self.head is None:
      raise Exception("List is empty")
    
    for node in self:
      if node.data == target_node_data:
        new_node.next = node.next
        node.next = new_node
        return
      
    raise Exception(f"Node with data {target_node_data} not found")
  
  def add_before(self, target_node_data, new_node):
    if self.head is None:
      raise Exception("List is empty")
    
    if self.head.data == target_node_data:
      return self.add_first(new_node)

    prev_node = self.head
    for node in self:
      if node.data == target_node_data:
        prev_node.next = new_node
        new_node.next = node
        return
      prev_node = node

    raise Exception("Node with data '%s' not found" %target_node_data)

  def remove_node(self, target_node_data):
    if self.head is None:
      raise Exception("List is empty")
    
    if self.head.data == target_node_data:
      self.head = self.head.next
      return

    prev_node = self.head

    for node in self:
      if node.data == target_node_data:
        prev_node.next = node.next
        return
      prev_node = node

    raise Exception("Node with data '%s' not found" %target_node_data)


#NODE CLASS
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  def __repr__(self):
    return self.data

llist = LinkedList(["a", "b", "c", "d", "e"])
print(llist)

#add node to beginning of linked list
llist.add_first(Node("1"))
print('\nprint linked list where 1 is added to start')
print(llist)

#add node to the end of a linked list(must traverse whole list)
llist.add_last(Node("f"))
print('\nprint linked list where f is added to end')
print(llist)

#add node after a certain node
llist.add_after("c", Node("x"))
print('\n add "x" after node "c"')
print(llist)

#add node before a certain node
llist.add_before("c", Node("y"))
print('\n add "y" before node "c"')
print(llist)
#for loop to print individual node in list
# print('\nprinted for loop of linked list')
# for node in llist:
#   print(node)