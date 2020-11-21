class Node:
    def __init__(self, ele, parent = None, child = None):
        self.ele = ele
        self.next_node = child
        self.previous_node = parent


class QueueLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None,self.head)
        self.head.next_node = self.tail
        self.size = 0
    
    def enqueue(self,ele):
        new_node = Node(ele)
        last_node = self.tail.previous_node
        last_node.next_node = new_node
        new_node.previous_node = last_node
        new_node.next_node = self.tail
        self.tail.previous_node = new_node
        self.size += 1

    def dequeue(self):
        dequeue_ele = self.head.next_node
        self.head.next_node = dequeue_ele.next_node
        dequeue_ele.next_node.parent = self.head
        self.size -= 1
        return dequeue_ele.ele
    
    def empty(self):
        if self.size == 0:
            return True
        else: return False

class QueueArray:
    def __init__(self,cap):
        self.head = 0
        self.tail = 0
        self.q_arr = [None] * cap

    def size(self):
        return self.head - self.tail

    def enqueue(self,ele):
        if self.tail < self.size():
            self.q_arr[self.tail] = ele
            self.tail += 1
        else: raise Exception('Queue is full')
    
    def dequeue(self):
        if self.size() <= 0:
            self.reset()
        else:
            dequeue_ele = self.q_arr[self.head]
            self.head += 1
            return dequeue_ele

    def reset(self):
        self.head = 0
        self.tail = 0
        self.q_arr = [None] * self.size

    def empty(self):
        if self.size() <= 0:
            return True
        else: return False
    
    def full(self):
        if self.tail >= (len(self.q_arr) - 1):
            return True
        else: return False 
