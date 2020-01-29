import pytest
from linked_list import LinkedList

class TestLinkedList:
    def test_instantiation(self):
        ll = LinkedList()
        assert(ll.head == None)

    def test_insert(self):
        ll = LinkedList()
        ll.insert(1, [100])
        assert(ll.head.key) == 1
        assert(ll.head.value) == [100]
        assert(ll.tail.key) == 1
        assert(ll.tail.value) == [100]
        ll.insert(2, [200])
        assert(ll.head.key) == 1
        assert(ll.head.value) == [100]
        assert(ll.tail.key) == 2
        assert(ll.tail.value) == [200]

    def test_find_by_key(self):
        ll = LinkedList()
        ll.insert(1, [100])
        ll.insert(2, [200])
        assert(ll.find_by_key(1)) == [100]
        assert(ll.find_by_key(2)) == [200]
        assert(ll.find_by_key(27)) == None

    def test_delete_head(self):
        ll = LinkedList()
        ll.insert(1, 1)
        ll.insert(2, 2)
        ll.insert(3, 3)
        ll.delete(1)
        assert(ll.head.key) == 2

    def test_delete_tail(self):
        ll = LinkedList()
        ll.insert(1, 1)
        ll.insert(2, 2)
        ll.insert(3, 3)
        ll.delete(3)
        assert(ll.tail.key) == 2

    def test_delete_middle(self):
        ll = LinkedList()
        ll.insert(1, 1)
        ll.insert(2, 2)
        ll.insert(3, 3)
        ll.delete(2)
        assert(ll.head.next.value) == 3
