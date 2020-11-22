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
        self.height = 0       
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
        if current is None:
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

    def get_height(self,current=None,count=0):
        if current is None:
            current = self.root
            self.height = 0

        count += 1
        if current.left is not None:
            self.get_height(current.left,count)
        if current.right is not None:
            self.get_height(current.right,count)
        if count >= self.height:
            self.height = count

        return self.height

    def get_min(self,current=None):
        if current is None:
            current = self.root
        
        if current.left is not None:
            return (self.get_min(current.left)) # parse the return value when traversed to the left-most node up the recursive tree
        else:
            return current.key

    def get_max(self,current=None):
        if current is None:
            current = self.root
        
        if current.right is not None:
            return (self.get_max(current.right))
        else:
            return current.key

    def delete_value(self,key):
        current = self.root
        delete = None
        while not delete:
            if key < current.key and current.left is not None:
                current = current.left
            elif key > current.key and current.right is not None:
                current = current.right
            elif key == current.key:
                delete = current
            else:
                break
        
        if delete:
            # case 1: this node has no children node
            if delete.left is None and delete.right is None:
                if  delete.key <= delete.parent.key:
                    delete.parent.left = None
                else:
                    delete.parent.right = None
                return True
            
            # case 2a: this node has left child node
            elif delete.left is not None and delete.right is None:
                if delete.key <= delete.parent.key:
                    delete.parent.left = delete.left
                    delete.parent.left.parent = delete.parent
                else:
                    delete.parent.right = delete.left
                    delete.parent.right.parent = delete.parent
                return True
            
            # case 2b: this node has right child node
            elif delete.right is not None and delete.left is None: 
                if delete.key <= delete.parent.key:
                    delete.parent.left = delete.right
                    delete.parent.left.parent = delete.parent
                else:
                    delete.parent.right = delete.right
                    delete.parent.right.parent = delete.parent
                return True
            
            # case 3: this node has two children node
            else:
                next_biggest = delete.right
                while next_biggest.left is not None:
                    next_biggest = next_biggest.left
                next_biggest.parent.left = None
                next_biggest.parent = delete.parent
                next_biggest.left = delete.left
                next_biggest.right = delete.right
                delete.left.parent = next_biggest
                delete.right.parent = next_biggest
                if delete == self.root: # set the root node if we are deleting the root
                    self.root = next_biggest
                return True
            
            # remove the node we are deleting
            del delete
        else: return -1

    def get_successor(self,key):
        if key == self.get_max(): # escape case if key is the maximum key in the BST
            return -1
        else:
            node = self.root
            while key != node.key: # find the node with the key by traversing the BST
                if key < node.key:
                    node = node.left
                elif key > node.key:
                    node = node.right
            
            # if the node has right subtree, just need to find the smallest key in the right subtree, because all keys in right subtree are bigger than the node
            if node.right is not None:
                return self.get_min(node.right)
            
            # if the node has no right subtree...
            next_biggest = node.parent
            # see if the node is the biggest member of k-i level subtree
            # if yes, need to traverse up a level to find the smallest node that is bigger than the node
            # if no, that means the parent of k-i level subtree is bigger than the node
            while next_biggest is not None and node == next_biggest.right: 
                node = next_biggest
                next_biggest = node.parent
            return next_biggest.key

bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(3)
bst.insert(60)
bst.insert(1)
bst.insert(5)
bst.insert(15)
bst.insert(4)
bst.insert(9)
bst.insert(7)
bst.insert(12)
bst.insert(12)
bst.insert(17)
bst.insert(40)
print (bst.get_height())
print (bst.get_min())
print (bst.get_max())
# bst.delete_value(10)
print (bst.get_successor(9))
print ('Done')