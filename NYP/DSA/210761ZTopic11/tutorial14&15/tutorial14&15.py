class Node:
    def __init__(self, __v: int = None) -> None:
        self.next = None
        self.value = __v


# q1
def find_second_last_node(N: Node):
    while N.next.next != None:
        N = N.next
    return N


# q2
def concat_linked_lists(L: Node, M: Node):
    while L.next != None:
        L = L.next
    L.next = M
    return L


# q3
def count_linked_list(N: Node):
    if N.next == None:
        return 1
    return 1 + count_linked_list(N.next)


# q4
class LinkedList:
    def __init__(self, __n: Node) -> None:
        self.head = __n
        self.tail = __n

    # a)
    def append_tail(self, __n: Node) -> None:
        self.tail.next = __n
        self.tail = __n

    def append_head(self, __n: Node) -> None:
        n = self.head
        self.head = __n
        self.head.next = n

    # b)
    def pop_tail(self) -> Node:
        n = self.tail
        i = self.head
        while i.next != self.tail:
            i = i.next
        n = i.next
        self.tail = i
        return n

    def pop_head(self) -> Node:
        n = self.head
        self.head = self.head.next
        return n
