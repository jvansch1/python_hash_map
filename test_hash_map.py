import pytest
from hash_map import HashMap
from linked_list import LinkedList

class TestHashMap:
    def test_instantiation(self):
        hash = HashMap()
        assert(isinstance(hash.store[0], LinkedList))
        assert(hash.store[0].head) == None

    def test_put_and_get(self):
        hash = HashMap()
        hash[1] = [100]
        hash["Hello"] = "Goodbye"
        hash[1.7] = 45
        assert(hash[1]) == [100]
        assert(hash["Hello"]) == "Goodbye"
        assert(hash[1.7]) == 45

    def test_delete(self):
        hash = HashMap()
        hash[1] = 100
        hash[2] = 200
        hash[3.1] = 64
        assert(hash[1]) == 100
        assert(hash[2]) == 200
        assert(hash[3.1]) == 64
        assert(hash.data_count) == 3
        hash.delete(2)
        hash.delete(3.1)
        assert(hash[2]) == None
        assert(hash[3.1]) == None
        assert(hash.data_count) == 1

        # Deleting key not in hash should not decrement data count
        hash.delete(555)
        assert(hash.data_count) == 1

    def test_keys(self):
        hash = HashMap()
        hash[1] = [100]
        hash[2] = [200]
        hash[3] = [300]
        hash["Hello"] = "Goodbye"
        keys = hash.keys()
        assert("Hello" in keys)
        assert(1 in keys)
        assert(2 in keys)
        assert(3 in keys)

    def test_values(self):
        hash = HashMap()
        hash[1] = [100]
        hash[2] = [200]
        hash[3] = [300]
        hash["Hello"] = "Goodbye"
        values = hash.values()
        assert([100] in values)
        assert([200] in values)
        assert([300] in values)
        assert("Goodbye" in values)

    def test_increase_store_size(self):
        hash = HashMap()
        hash[1] = [100]
        hash[2] = [200]
        hash[3] = [300]
        assert(hash.size) == 5
        assert(hash[1]) == [100]
        assert(hash[2]) == [200]
        assert(hash[3]) == [300]
        # Doubling happens here
        hash[4] = [400]
        assert(hash.size) == 10
        hash[5] = [500]
        hash[6] = [600]
        hash[7] = [700]
        hash[8] = [800]
        assert(hash[1]) == [100]
        assert(hash[2]) == [200]
        assert(hash[3]) == [300]
        assert(hash[4]) == [400]
        assert(hash[5]) == [500]
        assert(hash[6]) == [600]
        assert(hash[7]) == [700]
        assert(hash[8]) == [800]

    def final_test(self):
        map = HashMap()
        map[1] = 100
        map[5] = 500
        map[20] = 5
        map["Hello"] = "Goodbye"
        assert(map.exists("Hello"))
        assert(map["Hello"]) == "Goodbye"
        map.delete("Hello")
        assert(map["Hello"]) == None
