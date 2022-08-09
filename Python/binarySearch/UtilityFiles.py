def searchItem(items, target):
    for item in range(len(items)):
        if items[item] == target:
            return item
    return -1


#implicitely add optional low and high with values 
# none as initializers
def binarySearch(items, target, low = None, high = None):
    #get a mid, left and right pointer
    
    #At the beginning, set the low and high
    if low is None:
        low = 0
    if high is None:
        high = len(items)-1
    
    #if they ever cross, nothing was found
    if high < low:
        return -1
    
    #set the mid point
    mid = (high+low) // 2
    
    #if the left or right pointer is the target, return it
    #if the same, return the mid point
    if items[mid] == target:
        return mid
    #if  the target is less than the mid point, 
    # run it again with high as the mid-1
    elif items[mid] > target:
        return binarySearch(items, target, low, mid-1)
    else:
    #if target is more than the mid point, 
    # run it again with low as mid+1
        return binarySearch(items, target,mid+1, high)
