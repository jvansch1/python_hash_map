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
        assert(hash[1]) == [100]
        assert(hash["Hello"]) == "Goodbye"

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
        assert(hash[1]) == [100]
        assert(hash[2]) == [200]
        assert(hash[3]) == [300]
        # Doubling happens here
        hash[4] = [400]
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
