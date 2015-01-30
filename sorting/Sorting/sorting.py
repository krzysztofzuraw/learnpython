from heapq import merge

def merge_sort(lists):
    """
    Merge sorting algorithm
    :param lists: list to be sorted
    :return: sorted list
    :rtype: list
    """
    if len(lists) <= 1:
        return lists
        
    middle = len(lists) // 2
    left = lists[:middle]
    right = lists[middle:]
    left = merge_sort(left)
    right = merge_sort(right)
    
    return list(merge(left,right))
    
    

def insertion_sort(lists):
    """
    Insertion sorting alogrithm
    :param lists: list to be sorted
    :return: sorted list
    :rtype: list
    """
    for j in range(1,len(lists)):
        key = lists[j]
        i = j - 1
        while i >= 0 and lists[i] > key:
            lists[i + 1] = lists[i]
            i = i - 1
        lists[i+1] = key
    return lists    
