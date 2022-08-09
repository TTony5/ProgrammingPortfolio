
#Run a Binary Search for a point
#if it finds it, return the number, else return -1
#Assume Sorted Tree

from UtilityFiles import binarySearch, searchItem

if __name__=='__main__':
    l = [1,3,4,5,6,8,9]
    target = 6
    
    print(searchItem(l, target))
    print(binarySearch(l, target))