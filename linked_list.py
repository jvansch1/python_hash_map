class ListNode(object):
    def __init__(self, key, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
        self.tail = head

    def insert(self, key, value):
        if self.head == None:
            self.head = ListNode(key, value)
            self.tail = self.head
            return

        self.tail.next = ListNode(key, value)
        self.tail = self.tail.next

    def find_by_key(self, key):
        current_node = self.head

        while current_node:
            if current_node.key == key:
                return current_node.value

            current_node = current_node.next

        return None

    def delete(self, key):
        current_node = self.head
        prev_node = None

        while current_node:
            # The key we are deleting is the head
            if current_node.key == key and prev_node == None:
                self.head = current_node.next
                return True
            # Node we are deleting is tail
            elif current_node.key == key and current_node.next == None:
                prev_node.next = None
                self.tail = prev_node
                return True
            elif current_node.key == key:
                prev_node.next = current_node.next
                return True

            prev_node = current_node
            current_node = current_node.next

        # If we do not find the key return false
        return False


    def keys(self):
        keys = []

        current_node = self.head

        while current_node:
            keys.append(current_node.key)
            current_node = current_node.next

        return keys

    def values(self):
        values = []

        current_node = self.head

        while current_node:
            values.append(current_node.value)
            current_node = current_node.next

        return values

    def key_value_pairs(self):
        key_value_pairs = []
        current_node = self.head

        while current_node:
            key_value_pairs.append((current_node.key, current_node.value))
            current_node = current_node.next

        return key_value_pairs
