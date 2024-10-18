#Assignment 2

#Exercise 2

names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]

# function to get all names that contain the inputted letter
def name_letter(names):
    #lowercase the inputted letter
    letter= input('Please input a letter: ').lower()
    #condition of a single letter
    if len(letter)>1:
        print('Please input a single letter.')
    #loop over names in the list
    for name in names:
        # lowercase the name
        #if letter in name print the name
        if letter in name.lower():
            print(name)
    #repeatedly call function       
    name_letter(names)

#call the function
name_letter(names)
