def merge_sort(list):
    # sorts a list in ascending order
    # returns a new sorted list
    # divide: find the midpoint of the list and divide into sublists
    # conquer: recursively sort the sublists created in previous step
    # combine: merge the sorted sublists created in previous step

    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    # divide the unsorted list at midpoint into sublists
    # returns 2 sublists - left and right
    mid = len(list) // 2  # floor division
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    # merges 2 lists and sorting them
    # returns a new list

    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i += 1
    
    while j < len(right):
        l.append(right[j])
        j += 1
    return l

def verify_sorted(list):
    n = len(list)

    if n==0 or n==1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [12,56,13,65,4,7]

l = merge_sort(alist)

print(l)
print(verify_sorted(alist))
print(verify_sorted(l))