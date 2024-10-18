# Exercise 4 Adding a number to a sorted list
def add_num(list1, num):
    #number is less than or equal than the first element 
    if list1[0]>= num:
        list1= [num] + list1
    #number is greater than or equal than the last element    
    elif list1[-1]<= num:
        list1.append(num)   
    #number is greater than the first element and smaller than the last element
    else:
        start= 0
        end = len(list1) -1
        mid= (start +end)//2 
       
        while start<=end:
            if  num> list1[mid]:
                start= mid +1
                mid= (start +end)//2     
       
            else:
                end= mid -1
                mid= (start +end)//2

        list_mid= list1[:start] + [num] + list1[start:]
        list1= list_mid
    
    return list1

list1= [1,34,56,78,89]
num=77
print(add_num(list1, num))
list1= [1,3,56,234,789]
num=-99
list1= add_num(list1, num)
print(list1)
num= 789
print(add_num(list1, num))

