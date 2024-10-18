# Assignment 2
# Exercise 3

#list of numbers
num_list= [-12, 4, 12, 25, 67]

# sort the list after a number is added
def sort_num(num_list):

    #input number
    num= float(input('Please input a number: '))
    # number is actually an integer, change it to integer
    if num.is_integer():
        num=int(num)
    #append number to the list
    num_list.append(num)
    #sort the list and print it
    print(sorted(num_list))
    #base case (-99 will also be added to the list and then the program stops)
    if num == -99:
        return
    # recursive call
    sort_num(num_list)
#call the function
sort_num(num_list)


