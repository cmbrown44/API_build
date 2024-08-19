class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self) -> None:
        self.head = None # first node in a linked list
        self.last_node = None

    def print_linked_list(self):
        """
        Print a string representation of the linked list
        """
        linked_list_string = ""
        node = self.head # start with the first node
        if node is None:
            print(None)
        while node:
            linked_list_string += f" {str(node.data)} ->"
            node = node.next_node # after first node, move to next node in linked list
            
        linked_list_string += " None" # next_node pointer of last node will be None
        print(linked_list_string)
        
linked_list = LinkedList()
node5 = Node("node 5 data", None)
node4 = Node("node 4 data", node5)
node3 = Node("node 3 data", node4)
node2 = Node("node 2 data", node3)
node1 = Node("node 1 data", node2)

linked_list.head = node1

linked_list.print_linked_list()