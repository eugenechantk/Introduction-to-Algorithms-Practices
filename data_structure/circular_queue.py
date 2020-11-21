class CircularQueue:
    def __init__(self,cap):
        self.head = 0
        self.tail = 0
        self.MaxSize = cap
        self.q_arr = list()

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.MaxSize - (self.head - self.tail)
    
    def enqueue(self,ele):
        if self.size() >= self.MaxSize:
            raise Exception('Queue is full')
        else:
            self.q_arr.append(ele)
            self.tail = (self.tail + 1) % self.MaxSize
    
    def dequeue(self):
        if self.size() <= 0:
            raise Exception('Queue is empty')
        else:
            dequeue_ele = self.q_arr[self.head]
            self.head = (self.head + 1) % self.MaxSize
        return dequeue_ele

queue = CircularQueue(10)
queue.enqueue(10)
print ('Done')
