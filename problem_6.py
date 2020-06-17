class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    l_set = set()
    cur_node = llist_1.head
    while cur_node:
        l_set.add(cur_node.value)
        cur_node = cur_node.next
    cur_node = llist_2.head
    while cur_node:
        l_set.add(cur_node.value)
        cur_node = cur_node.next
    llist = LinkedList()
    for node in l_set:
        llist.append(node)
    return llist

def intersection(llist_1, llist_2):
    # Your Solution Here
    l_set1 = set()
    cur_node = llist_1.head
    while cur_node:
        l_set1.add(cur_node.value)
        cur_node = cur_node.next
    l_set2 = set()
    cur_node = llist_2.head
    while cur_node:
        l_set2.add(cur_node.value)
        cur_node = cur_node.next
    llist = LinkedList()
    for node in l_set1.intersection(l_set2):
        llist.append(node)
    return llist

def test(list1,list2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    for i in list1:
        linked_list_1.append(i)

    for i in list2:
        linked_list_2.append(i)
    print (union(linked_list_1,linked_list_2))
    print (intersection(linked_list_1,linked_list_2))

    
# Test case 1

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
print("NEW TEST :")
test(element_1,element_2)

# Test case 2
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
print("NEW TEST :")
test(element_1,element_2)

# Test case 3
element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [4,7,9,3,0,5]
print("NEW TEST :")
test(element_1,element_2)

# Test case 3
element_1 = [4,5,98,1,34,6,8]
element_2 = [4,7,9,3,0,5]
print("NEW TEST :")
test(element_1,element_2)


