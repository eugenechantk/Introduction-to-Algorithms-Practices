class HashTable:
    def __init__(self,size):
        self.hashtable = [[] for _ in range(size)]
        self.size = size

    def hash(self, key):
        return hash(key) % self.size

    def add(self,key,value):
        hash_value = self.hash(key)
        bucket = self.hashtable[hash_value]
        if len(bucket) == 0:
            bucket.append([key, value])
        else:
            for i in bucket:
                if i[0] == key:
                    i[1] = value
                    break
            else: bucket.append([key,value])

    def exists(self,key):
        hash_value = self.hash(key)
        bucket = self.hashtable[hash_value]
        if len(bucket) == 0:
            return False
        else:
            for i in bucket:
                if i[0] == key:
                    return True
            else: return False

    def get(self,key):
        hash_value = self.hash(key)
        bucket = self.hashtable[hash_value]
        if len(bucket) == 0:
            return -1
        else:
            for i in bucket:
                if i[0] == key:
                    return i[1]
            else: return -1

    def remove(self,key):
        hash_value = self.hash(key)
        bucket = self.hashtable[hash_value]
        if len(bucket) == 0:
            raise Exception('Key not in hash table')
        else:
            for i in bucket:
                if i[0] == key:
                    bucket.remove(i)
            else: raise Exception('Key not in hash table')
    
hash_table = HashTable(10)
hash_table.add(10,'abc')
hash_table.add(10,'def')
hash_table.add(20,'ghi')
print (hash_table.exists(20))
hash_table.remove(20)
print (hash_table.get(20))
print (hash_table)


