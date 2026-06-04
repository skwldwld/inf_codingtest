class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def count(self):
        count = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            count += 1
        return count

def get_linked_list_sum(linked_list_1, linked_list_2):
    count1 = LinkedList.count(linked_list_1)
    total1 = 0
    cur = linked_list_1.head
    for i in range(count1):
        total1 += cur.data * (10 ** (count1 - i - 1))
        cur = cur.next

    count2 = LinkedList.count(linked_list_2)
    total2 = 0
    cur = linked_list_2.head
    for i in range(count2):
        total2 += cur.data * (10 ** (count2 - i - 1))
        cur = cur.next

    return total1 + total2
    # return 1032


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))