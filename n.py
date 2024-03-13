# def search(arr,target):
#     for i in range(len(arr)):
#         assert isinstance(i,int),"array elements must be integers"
#         if arr[i] == target:
#             return i
#     raise ValueError("Value not found in the list")

def if_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True


def array_addition(arr1,arr2):
    assert len(arr1)==len(arr2),"Arrays should be of same length"
    return [arr1[i]+arr2[i] for i in range(len(arr1))]

def get_first_two_elements(arr):
    assert len(arr)>=2,"Array should have atleast 2 elements"
    return arr[:2]

def modify_data(sample_data):
    sample_data[0]=lambda x:x**2,sample_data[0]

def running_sum_pair_wise3tuple(tuple_lst):
    total1 = 0
    total2 = 0
    total3 = 0
    for a,b,c in tuple_lst:
        total1 += a
        total2 += b
        total3 += c
    return total1,total2,total3

print(running_sum_pair_wise3tuple([(1,2,3),(4,5,6),(7,8,9)])==(12,15,18))




