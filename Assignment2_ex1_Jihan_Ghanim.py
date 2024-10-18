# Assignment 2

# Exercise 1

#input integers
int1= int(input('Please enter the first integer: '))
int2= int(input('Please enter the second integer: '))
# given list1
list1= [54,76,2,4,98,100]

#function that produces the range of values in the list
def range_num(list1, int1, int2):
    #get the larger inputted integer
    num1= min(int1, int2)
    #get the smaller inputted integer
    num2= max(int1, int2)
    
    #obtain the range of values (considering that the inputted integers are inclusive)
    for i in range(len(list1)):
        if list1[i] >= num1 and list1[i] <= num2:
            print(list1[i])

#call the function
range_num(list1, int1, int2)