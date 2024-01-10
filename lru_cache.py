from collections import deque

class LRUCache:

    class Node:
        def __init__(self, key: int, nxt=None, prev=None):
            self.key = key
            # self.val = val
            self.next = nxt
            self.prev = prev
        
        def __repr__(self):
            return f"Node({self.key}, next={self.next})"


    def __init__(self, capacity: int):
        self.map = {}
        self.max_cap = capacity
        self.cap = 0
        self.head = None
        self.tail = None

    def _evict(self) -> None:
        if self.cap <= self.max_cap:
            return
        
        # In the case we're over capacity, we need to remove the key
        # corresponding to the tail from the data structure.
        # Start with the map.
        del self.map[self.tail.key]
        # Then remove it from the LL.
        if self.max_cap < 1:
            # We will never have any values in the list.
            self.head = self.tail = None
        elif self.cap == 2:
            # We need to retain the head and not the tail.
            self.head.next = None
            self.tail = self.head
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.cap -= 1
    
    # 'Use' the key of the node passed in.
    def _use(self, node) -> int:
        # True if key already existed in LL.

        found = self.map.get(node.key, -1) 
       
        # In this case we know we must update our LL.
        if found != -1:
            # We are guaranteed that both self.head and self.tail exist in
            # this case, since they can only equal none if there are no 
            # nodes in the LRU.
            # We are also guaranteed node.key exists in the
            # LRU. We thus must look for the node's position 
            # within the LRU.
            if self.cap == 1:
                # In this case it's easy.
                self.head = node
                self.tail = node
            elif self.cap == 2:
                if self.head.key == node.key:
                    node.next = self.head.next
                    node.next.prev = node
                    self.head = node
                else:
                    # it's the tail in this case
                    self.head.next = None
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
            else:
                curr = self.head
                # This should never hit 'None'.
                while curr.key != node.key:
                    curr = curr.next

                # Curr will now be the node whose key is identical to
                # that of the passed in node.
                # We must remove it altogether from the list, then make the
                # newnode the head of the list.
                # There are two special cases: if curr is the head, or
                # if curr is the tail. (We do not have both since we 
                # are guaranteed that self.cap > 1).
                if curr == self.head:
                    # In this case, simply update it and unlink the
                    # old head.
                    node.next = self.head.next
                    self.head = node
                elif curr == self.tail:
                    # Make the new tail be old tail's prev.
                    self.tail = self.tail.prev
                    self.tail.next = None
                    self.head.prev = node
                    node.next = self.head
                    self.head = node 
                else:
                    # Otherwise, curr is somewhere in the middle of the
                    # list. We must delete and relink the other nodes.
                    print(curr)
                    print(curr.prev)
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    # SHOULD relink properly...check to make sure
                    print(curr.prev)
                    print(curr.next.prev)
                    node.next = self.head
                    self.head = node

        # If found is false, we don't know whether we're putting or
        # getting and so leave updating the list up to put if it needs
        # to.
        
        return found

    # Inserts a brand new key into the LRU's linked list.
    def _insert_new(self, node) -> None:
        # If the LRU doesn't exist, instantiate it to this node.
        if self.head == None:
            # We can set both because we will only have 
            # self.head == None when self.tail == None.
            self.head = node
            self.tail = node
        else:
            # Otherwise we're guaranteed that self.head exists.
            self.head.prev = node
            node.next = self.head
            self.head = node
        


    def get(self, key: int) -> int:
        val = self._use(self.Node(key, None))
        return val
        
        

    def put(self, key: int, value: int) -> None:
        newnode = self.Node(key, None)
        found = self._use(newnode)
        if found == -1:
            # Then we need to insert it as a new node in the LRU.
            self._insert_new(newnode)
            self.cap += 1
        # If we found it, _use already updated the LL for us.
        # In either case, add it to the map and then evict if necessary
        
        self.map[newnode.key] = value
        self._evict()

if __name__ == "__main__":
    s = LRUCache(2)
    # s.put(1, 1)
    # s.put(2, 2)
    # print(s.get(1))
    # s.put(3, 3)
    # print(s.get(2))
    # s.put(4, 4)
    # print(s.get(1))
    # print(s.get(3))
    # print(s.get(4))

    s.put(2,1)
    s.put(3,2)
    print(s.get(3))
    print(s.get(2))
    s.put(4,3)
    print(s.get(2))
    print(s.get(3))
    print(s.get(4))