from doubly_linked_list import DoublyLinkedList, ListNode

# current architecture
"""
self.cache = [node(key, value), node(key, value), node(key, value), node(key, value), . . . ]
self.dict = {key: node(key, value), key: node(key, value), key: node(key, value), . . . }
"""

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.max_nodes = limit
        self.num_current_nodes = 0
        self.cache = DoublyLinkedList()
        self.dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # check if key is in the dictionary
        if key in self.dict:
            node = self.dict[key]
            self.cache.move_to_end(node)
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if key is not in use, create a new node
        if key not in self.dict:
            # create a Node with key and value in DLList
            self.cache.add_to_tail([key, value])
            # add the node we just added to the cache tail to the dict
            self.dict[key] = self.cache.tail
            # increment current node count
            self.num_current_nodes += 1

        # check if key is already in use
        else:
            # get the node in question
            node = self.dict[key]   
            # update the node's value
            node.value = [key, value]
            # move node to back of the DLL
            self.cache.move_to_end(node)

        # if the node limit is reached delete the LRUsed
        if self.max_nodes < self.num_current_nodes:
            # get node to be removed
            node = self.cache.head
            # remove the key from dict
            self.dict.pop(node.value[0], None)
            # remove the node from the list
            self.cache.remove_from_head()
            # decrement the size counter
            self.num_current_nodes -= 1
