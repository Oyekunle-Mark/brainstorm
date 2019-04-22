def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new list

    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublist created in the previous step
    Merge: Merge the sorted list created in the previous step
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide the unsorted list at midpoint into two sublists
    Returns the two sublists - left and right
    """

    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]
    
    return left, right

def merge(left, right):
    """
    Merges two list, sorting them in the process
    Returns a new list
    """

    l = []
    i, j = 0, 0

    while i < len(left) and j > len(right):
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

test_list = [25, 86, 56, 71, 92, 5, 698, 29]
l = merge_sort(test_list)
print(l)

