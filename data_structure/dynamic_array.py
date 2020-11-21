import ctypes

class DynamicArray:
    def __init__(self):
        self.cap = 1
        self.n = 0
        self.arr = self._make_array(self.cap)

    def __getitem__(self,index):
        if not index < self.n:
            raise Exception("Index out of number of elements in array")
        else:
            return self.arr[index]

    def __len__(self):
        return self.n

    def __repr__(self):
        return str(self.arr)

    def capacity(self):
        return self.cap

    def is_empty(self):
        if self.n == 0:
            return True
        else: return False

    def append(self,ele):
        if self.n == self.cap:
            self._grow_array(self.cap,2)
        self.arr[self.n] = ele
        self.n += 1

    def push(self,ele):
        self.insert_at(ele,0)

    def pop(self):
        pop_ele = self.arr[self.n - 1]
        self.remove_at(self.n - 1)
        return pop_ele

    def insert_at(self,ele,index):
        if not index < self.cap:
            raise Exception('Index out of capacity of the array')
        if self.n == self.cap:
            self._grow_array(self.cap,2)
        for i in range(self.n - 1,index - 1,-1):
            self.arr[i + 1] = self.arr[i]
        self.arr[index] = ele
        self.n += 1

    def remove_at(self,index):
        if not index < self.cap:
            raise Exception('Index out of capacity of the array')
        # only need to traverse to the penultimate element; because by then it will swap with the last element anyways
        for i in range(index,self.n - 1):
            self.arr[i], self.arr[i+1] = self.arr[i+1],self.arr[i]
        # self.n - 1: the index to the last element in the dynamic array
        self.arr[self.n - 1] = None
        self.n -= 1

    def find(self,ele):
        for i in range(self.n):
            if self.arr[i] == ele:
                return i
        return -1

    def remove(self,ele):
        for i in range(self.n):
            if self.arr[i] == ele:
                self.remove_at(i)

    def _grow_array(self,cap,g_coeff):
        big_arr = self._make_array(cap * g_coeff)
        for i in range(self.n):
            big_arr[i] = self.arr[i]
        self.arr = big_arr
        self.cap = cap * g_coeff
    
    def _make_array(self,cap):
        return [None] * cap

d_arr = DynamicArray()
d_arr.append(1)
d_arr.append(3)
d_arr.append(2)
d_arr.push(3)
d_arr.remove(3)
print (repr(d_arr))