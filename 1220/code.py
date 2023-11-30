import re

class Node:
    def __init__(self, id, value, prev=None, next=None):
        self.id = id
        self.prev = prev
        self.value = value
        self.next = next

    def decrypt(self):
        self.value *= 811589153

class LinkedList:
    def __init__(self, head=None, last=None, length=None):
        self.head = head
        self.last = last
        self.length = length

    def get_prev(self, node, step=0):
        prev = node.prev
        for i in range(0, step):
            prev = prev.prev
        return prev
    
    def get_next(self, node, step=0):
        next = node.next
        for i in range(0, step):
            next = next.next
        return next

    # Debugging
    def print_list_once(self):
        tmp = self.head
        len = self.length
        for i in range(0, len):
            print(tmp.value, end = " ")
            tmp = tmp.next
        print('\n')
    
    def find_by_id(self, id):
        tmp = self.head
        while tmp.id != id:
            tmp = tmp.next
        return tmp

    def get_zero_value(self):
        tmp = self.head
        for i in range(0, self.length):
            while tmp.value != 0:
                tmp = tmp.next
        return tmp
    
    def decrypt(self):
        tmp = self.head
        for i in range(0, self.length):
            tmp.decrypt()
            tmp = tmp.next

def parse(file):
    linked_list = LinkedList()
    with open(file) as f:
        lines = f.readlines()
        arr = []
        for i, line in enumerate(lines):
            num = int(line.strip('\n'))
            if i == 0:
                linked_list.head = Node(i, num)
                arr.append(linked_list.head)
            elif i == len(lines) - 1:
                node = Node(i, num, arr[-1], linked_list.head)
                arr[-1].next = node
                linked_list.head.prev = node
                linked_list.last = node
                arr.append(node)
            else:
                node = Node(i, num, arr[-1])
                arr[-1].next = node
                arr.append(node)
        linked_list.length = len(arr)
    return linked_list

def shift(linked_list):
    for i in range(0, linked_list.length):
        node_to_move = linked_list.find_by_id(i) # 1
        
        prev_node = node_to_move.prev # 4
        next_node = node_to_move.next # 2

        moving_steps = node_to_move.value

        moving_steps %= linked_list.length - 1
        if moving_steps < 0:
            while moving_steps < 0:
                moving_steps += linked_list.length - 1
        if moving_steps == 0: continue

        # Get the new next and previous nodes
        new_next_node = linked_list.get_next(node_to_move, moving_steps)
        new_prev_node = linked_list.get_prev(new_next_node)

        # Detach the node that needs to be moved
        prev_node.next = next_node 
        next_node.prev = prev_node

        # Insert the node between new next and prev nodes
        node_to_move.prev = new_prev_node
        new_prev_node.next = node_to_move
        node_to_move.next = new_next_node
        new_next_node.prev = node_to_move

        # Move head and last when necessary
        if linked_list.head.id == i:
            linked_list.head = next_node
        
        if linked_list.last.id == i:
            linked_list.last = prev_node

    return linked_list
    
def calculate_from(node, step):
    tmp = node
    for _ in range(step):
        node = node.next
    return node.value

# Part 1
linked_list = parse("input.txt")
linked_list = shift(linked_list)
zero_value_node = linked_list.get_zero_value()

arr = []
for i in range(0, 4000, 1000):
    arr.append(calculate_from(zero_value_node, i))

print(sum(arr))

# Part 2
linked_list = parse("input.txt")
linked_list.decrypt()

for i in range(0, 10):
    linked_list = shift(linked_list)

zero_value_node = linked_list.get_zero_value()
arr = []
for i in range(0, 4000, 1000):
    arr.append(calculate_from(zero_value_node, i))

print(sum(arr))
