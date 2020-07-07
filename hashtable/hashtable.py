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


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_table = [None]*capacity
        self.num_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_items/self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        hval = 0x811c9dc5
        fnvprime = 0x01000193
        fnvsize = 2**32
        if not isinstance(key, bytes):
            key = key.encode("UTF-8", "ignore")
        for byte in key:
            hval = (hval * fnvprime) % fnvsize
            hval = hval ^ byte
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        i = self.hash_index(key)

        # If bucket is empty, insert at index
        if self.hash_table[i] is None:
            self.hash_table[i] = HashTableEntry(key, value)
            self.num_items += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.capacity*2)
            return

        # If not empty, check if key already exists and overwrite
        cur = self.hash_table[i]
        while cur is not None:
            if cur.key == key:
                cur.value = value
                return
            cur = cur.next

        # If key doesn't already exist, insert at beginning of bucket
        head = self.hash_table[i]
        self.hash_table[i] = HashTableEntry(key, value)
        self.hash_table[i].next = head
        self.num_items += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)  


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Check if key is head of bucket. Delete if so
        i = self.hash_index(key)
        cur = self.hash_table[i]
        if cur.key == key:
            self.hash_table[i] = self.hash_table[i].next
            self.num_items -= 1
            return cur.value

        # If not head, check rest of bucket
        prev = cur
        cur = cur.next
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.num_items -= 1
                return cur
            prev = cur
            cur = cur.next

        print('key not found!')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Check each item for key
        i = self.hash_index(key)
        cur = self.hash_table[i]
        while cur is not None:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        self.capacity = new_capacity
        old_table = self.hash_table
        self.hash_table = [None]*new_capacity

        for bucket in old_table:
            cur = bucket
            while cur is not None:
                self.put(cur.key, cur.value)
                cur = cur.next



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
