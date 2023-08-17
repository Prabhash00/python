'''
Prabhash Singh
202010101150020
'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2     
        if arr[mid] < x:
            low = mid + 1        
        elif arr[mid] > x:
            high = mid - 1      
        else:
            return mid
    
    return -1
 
arr = [ 7,8,12,23,64,89,248,993]
x = int(input("Enter number to be searched: "))

result = binary_search(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")