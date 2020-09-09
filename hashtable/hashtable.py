class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_to_tail(self, key, value):
        temp = self.head
        self.head = HashTableEntry(key,value)
        self.head.next = temp
        
    def find(self, key):
        temp = self.head
        while temp is not None:
            if key == temp.key:
                return temp.value
            else:
                temp = temp.next
                
    def delete(self, key):
        temp = self.head
        while temp is not None:
            if key == temp.key:
                temp.value = None
                return
            else:
                temp = temp.next
        
        


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
            
        self.storage = [None] * capacity
        self.size = 0
        



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity
        
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for s in key:
            hash = (hash * 33) + ord(s)
        return hash 

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        idx = self.hash_index(key) 
        
        data_point = self.storage[idx]
        
        if data_point is None:
            data_point = LinkedList()

            data_point.add_to_tail(key,value)
            self.storage[idx] = data_point
            self.size += 1
            
        else:
            data_point.add_to_tail(key,value)
            self.size += 1


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key)

        if idx is not None:
            idx = self.hash_index(key)
            val = self.storage[idx]
            val.delete(key)
            self.size -= 1

        else:
            print("not found")
       


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if key:   
            idx = self.hash_index(key)
            val = self.storage[idx]
            if val is None:
                pass
            else:
                found = val.find(key)
                return found
        else:
            return None 
        
        
        # idx = self.hash_index(key)
        # data_point = self.storage[idx]
        
        # if data_point:
        #     data_point.find()
        # else:
        #     return None
        
        # load = self.size / self.capacity
        # print(load)
        
        # if load > 0.7:
        #     newStorage = [LinkedList()] * (self.capacity * 2)
            

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
 
        self.capacity = new_capacity
        original_array = self.storage
        self.storage = [None] * new_capacity

        
        for lst in original_array:
            if lst is None:
                continue
            else:
                if lst.head.next is None:
                    self.put(lst.head.key, lst.head.value)
                else:
                    temp = lst.head
                    while temp.next is not None:
                        temp = temp.next
                    self.put(temp.key, temp.value)

                



# if __name__ == "__main__":
#     ht = HashTable(8)

#     ht.put("line_1", "'Twas brillig, and the slithy toves")
#     ht.put("line_2", "Did gyre and gimble in the wabe:")
#     ht.put("line_3", "All mimsy were the borogoves,")
#     ht.put("line_4", "And the mome raths outgrabe.")
#     ht.put("line_5", '"Beware the Jabberwock, my son!')
#     ht.put("line_6", "The jaws that bite, the claws that catch!")
#     ht.put("line_7", "Beware the Jubjub bird, and shun")
#     ht.put("line_8", 'The frumious Bandersnatch!"')
#     ht.put("line_9", "He took his vorpal sword in hand;")
#     ht.put("line_10", "Long time the manxome foe he sought--")
#     ht.put("line_11", "So rested he by the Tumtum tree")
#     ht.put("line_12", "And stood awhile in thought.")

#     print("")

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")
