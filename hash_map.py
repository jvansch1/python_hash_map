from linked_list import LinkedList
from hash_function import hash_function

class HashMap(object):
    def __init__(self):
        self.store = []

        for i in range(5):
            self.store.append(LinkedList())

        self.size = 5
        self.data_count = 0

    def put(self, key, value):
        index = hash_function(key, self.size)
        list = self.store[index]
        list.insert(key, value)
        self.data_count += 1

        if self.load_factor() > 0.7:
            self.increase_store_size()

    def get(self, key):
        index = hash_function(key, self.size)
        list = self.store[index]
        return list.find_by_key(key)

    def delete(self, key):
        index = hash_function(key, self.size)
        list = self.store[index]
        deleted = list.delete(key)
        if deleted:
            self.data_count -= 1

    def keys(self):
        keys = []

        for el in self.store:
            if el:
                keys += el.keys()

        return keys

    def exists(self, key):
        index = hash_function(key, self.size)
        list = self.store[index]
        return bool(list.find_by_key(key))

    def values(self):
        values = []

        for el in self.store:
            if el:
                values += el.values()

        return values

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def load_factor(self):
        return self.data_count / self.size

    def increase_store_size(self):
        new_store = []

        # The basic methodolgy here is:
        #   1. Double the size of store with each being a unique copy of linked list
        #   2. Get all existing key value pairs
        #   3. Since the store is a different size, buckets may be placed
        #      in different positions than they were previously. Re-bucket all
        #      key value pairs
        #   4. set the store of our instance to the new store

        for i in range(self.size * 2):
            new_store.append(LinkedList())

        for list in self.store:
            pairs = list.key_value_pairs()

            for pair in pairs:

                new_index = hash_function(pair[0], self.size * 2)
                new_store[new_index].insert(pair[0], pair[1])

        self.size = self.size * 2
        self.store = new_store
