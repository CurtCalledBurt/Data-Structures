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
            # get the node from the dictionary
            node = self.dict[key]
            # move the node to the back of the cache
            self.cache.move_to_end(node)
            # the node's value is a list of shape [key, value], 
            # so node.value[1] returns the value of the node
            return node.value[1]
        # if the key isn't in the dictionary, return None
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
            self.cache.add_to_tail((key, value))
            # add the Node to the dictionary
            self.dict[key] = self.cache.tail

        # check if key is already in use
        else:
            # get the node in question
            node = self.dict[key]   
            # update the node's value
            node.value = (key, value)
            # move node to back of the DLL
            self.cache.move_to_end(node)
            # if key is in use, the size of the cache stays the same, 
            # so the node max hasn't been reached. So we can return here 
            # to make this just a bit faster
            return

        # if the node limit is reached delete the LRUsed
        if self.max_nodes < len(self.cache):
            # get key of node to be removed
            key_of_oldest = self.cache.head.value[0]
            # remove the node from dictionary
            del self.dict[key_of_oldest]
            # remove the node from the list
            self.cache.remove_from_head()
