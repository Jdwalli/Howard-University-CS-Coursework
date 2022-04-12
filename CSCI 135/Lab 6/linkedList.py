from linkedListNode import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_head(self , value:int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def add_tail(self , value:int) -> None:
        self.tail = value
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get_value_at_position(self , location:int) -> int:
        current_node = self.head
        for _ in range(location - 1):
            current_node = current_node.next
        return current_node.value
                
    
    def to_value_list(self) -> list:
        current_node = self.head
        solution = []
        while current_node is not None:
            solution.append(current_node.value)
            current_node = current_node.next
        return solution
    
    def to_node_list(self) -> list:
        current_node = self.head
        solution = []
        while current_node is not None:
            solution.append(current_node)
            current_node = current_node.next
        return solution