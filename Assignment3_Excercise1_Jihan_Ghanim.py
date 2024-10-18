#Exercise 1
#Binary seach (recursive version)

def binarySearch(list1, key, start, end):

    mid= (start+ end)//2

    if  start>end:
        print('False')
        return
    
    if list1[mid]>key:
        #recursive call
        #end=mid-1
        binarySearch(list1, key, start, mid -1)
    
    elif list1[mid]==key:
        print('True')
        return 
    else:
        #recursive call
        #start=mid+1        
        binarySearch(list1, key, mid +1 , end)
    
list1=[12, 14,15,44,54,64,78]
start= 0
end= len(list1) -1
key=44
binarySearch(list1,key, start,end)

