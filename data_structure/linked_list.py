class Node:
    def __init__(self,value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head_node = Node(None)
    
    def __len__(self):
        return self.size
    
    def empty(self):
        if self.size == 0:
            return True
        else: return False
    
    def value_at(self,n):
        if not n <= self.size:
            raise Exception('Index out of size of linked list')
        node = self.head_node
        for i in range(n):
            node = node.next_node
        return node.value
    
    def push_front(self,value):
        front_node = Node(value)
        next_node = self.head_node.next_node
        self.head_node.next_node = front_node
        front_node.next_node = next_node
        self.size += 1

    def push_back(self,value):
        node = self.head_node
        for i in range(self.size):
            node = node.next_node
        node.next_node = Node(value)
        self.size += 1
    
    def pop_front(self):
        front_node = self.head_node.next_node
        new_front_node = front_node.next_node
        self.head_node.next_node = new_front_node
        self.size -= 1
        return front_node.value

    def pop_back(self):
        node = self.head_node
        for i in range(self.size - 1):
            node = node.next_node
        last_node = node.next_node.value
        node.next_node = None
        self.size -= 1
        return last_node

    def front(self):
        return self.head_node.next_node.value

    def back(self):
        node = self.head_node
        for i in range(self.size):
            node = node.next_node
        return node.value

    def insert(self,n,value):
        if not n < self.size:
            raise Exception('Index out of size of linked list')
        node = self.head_node
        for i in range(n - 1):
            node = node.next_node
        next_node = node.next_node
        node.next_node = Node(value)
        node.next_node.next_node = next_node
        self.size += 1

    def erase(self,n):
        if not n < self.size:
            raise Exception('Index out of size of linked list')
        node = self.head_node
        for i in range(n - 1):
            node = node.next_node
        node.next_node = node.next_node.next_node
        self.size -= 1

    def value_n_from_end(self,n):
        if not n < self.size:
            raise Exception('Index out of size of linked list')
        node = self.head_node
        for i in range(self.size - n):
            node = node.next_node
        return node.next_node.value

    def reverse(self):
        node = self.head_node
        for i in range(int(self.size/2)):
            front_node = node.next_node
            back_node = node
            for j in range(self.size - i*2 - 1):
                back_node = back_node.next_node
            
            if (self.size - i*2 -1) > 1:
                fronts_next_node = front_node.next_node
            else: # handle if the elements to swap are adjacent to each other
                fronts_next_node = front_node
            backs_next_node = back_node.next_node.next_node
            
            node.next_node = back_node.next_node
            back_node.next_node = front_node
            back_node.next_node.next_node = backs_next_node
            node.next_node.next_node = fronts_next_node
            
            node = node.next_node

    def remove_value(self,value):
        node = self.head_node
        for i in range(self.size):
            if node.next_node.value == value:
                replace_node = node.next_node.next_node
                node.next_node = replace_node
                self.size -= 1
                break
            node = node.next_node


linked_list = LinkedList()
linked_list.push_front(3)
linked_list.push_front(6)
linked_list.push_back(8)
linked_list.push_back(4)
linked_list.push_back(5)
linked_list.push_front(10)
linked_list.insert(3,9)
linked_list.remove_value(4)
linked_list.reverse()
print (linked_list.value_n_from_end(2))

