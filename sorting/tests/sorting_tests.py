from nose.tools import *
from Sorting.sorting import *

def test_insertion_sort():
    lists = [5,2,4,6,1,3]
    assert_equals(insertion_sort(lists), [1,2,3,4,5,6])
    assert_equals(insertion_sort([10,33,2,4,66]), [2,4,10,33,66])
    
def test_merge_sort():
    lists = [10, 99, 2, 5, 88, 66]
    assert_equals(merge_sort(lists), [2, 5, 10, 66, 88, 99])
    assert_equals(merge_sort([100, 23, 56, 77, 66]), [23, 56, 66, 77, 100]) 


