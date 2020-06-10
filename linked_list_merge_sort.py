from linked_list import LinkedList

def merge_sort(linked_list):
    # sort a linkedlist in ascending order

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size // 2
        
        mid_node = linked_list.node_at_index(mid - 1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half

def merge(left, right):
    # merges 2 linked lists, sorting data in nodes
    # returns a new, merged list
    
    merged = LinkedList()
    merged.add(0)  # adds a temporary head
    current = merged.head

    left_head = left.head
    right_head = right.head
    while left_head or right_head:
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            # no at either tail node
            # obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node
    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()

l.add(11)
l.add(3)
l.add(43)
l.add(67)
l.add(54)
l.add(89)
l.add(9)

print(l)
sorted_l = merge_sort(l)
print(sorted_l)