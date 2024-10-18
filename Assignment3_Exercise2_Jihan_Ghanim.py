#Exercise 2
#method1
def comb_string(list1, i):
    if i== len(list1):
            return   
    for j in range(len(list1)):
        str1 =str(list1[i]) + str(list1[j])
        print(str1)
    comb_string(list1, i+1)    
    

comb_string(["a","b","c"], 0)

print("***")

#method2
def comb_string2(list1, n, str1):
     
    if n==0:
        print(str1)
        return
    for i in list1:
        comb_string2(list1, n-1, str1 + i)

comb_string2(["a","b","c"], 2, "")    