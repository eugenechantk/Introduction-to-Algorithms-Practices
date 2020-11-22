class Node:
    def __init__(self,k,p=None,lc=None,rc=None):
        self.key = k
        self.parent =  p
        self.left = lc
        self.right = rc
    
class BST:
    def __init__(self):
        self.root = None
        self.count = 0
        self.repr_arr = []

    def __len__(self,current=None):
        if current is None:
            current = self.root
            self.count = 0 # initialize count to erase previous record
        
        if current is not None:
            self.count += 1 # update class variable, rather than create a variable within this recursion as it does not carry forward at the end
            if current.left is not None:
                self.__len__(current.left)
            if current.right is not None:
                self.__len__(current.right)
        return self.count

    def __repr__(self,current=None):
        if current is None:
            current = self.root
            self.repr_arr = []
        
        if current is not None:
            if current.left is not None:
                self.__repr__(current.left)
            self.repr_arr.append(current.key)
            if current.right is not None:
                self.__repr__(current.right)
        return str(self.repr_arr)

    def insert(self,key,current=None):
        if current is None and self.root is None:
            self.root = Node(key)
        else:
            if current is None: current = self.root
            
            if key <= current.key:
                if current.left is None:
                    current.left = Node(key,current)
                else:
                    self.insert(key,current.left)
            elif key > current.key:
                if current.right is None:
                    current.right = Node(key,current)
                else:
                    self.insert(key,current.right)
    
    def is_in_tree(self,key,current=None):
        if current == None:
            current = self.root

        if current is not None:
            if key < current.key and current.left is not None:
                if (self.is_in_tree(key,current.left)): # parsing the return value up the recursive tree 
                    return True
                else: return False
            elif key > current.key and current.right is not None:
                if (self.is_in_tree(key,current.right)): return True
                else: return False
            elif key == current.key:
                print ('current key is equal to key searching') 
                return True


bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(3)
bst.insert(60)
bst.insert(1)
bst.insert(5)
bst.insert(15)
bst.insert(4)
print ('Done')