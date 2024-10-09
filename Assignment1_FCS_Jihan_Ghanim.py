# Exercise 1
print('Exercise 1')

# age criterion
age_criterion=18
# valid residency
valid_residency= 'Lebanon'
# valid hacker rank score
valid_score =110

# not required but added to handle non-integers
try:
    # input age
    student_age= int(input('Please input your age in digits: '))

    
    # check if age above age criterion (18)
    if student_age> age_criterion:

        # input residency
        student_residency= input('Please input your country of residency: ').capitalize()

        # check the validity of the residency
        if student_residency == valid_residency:

            # input hacker rank score
            student_score= int(input('Please input your hacker rank score: '))

            # check the validity of the hacker rank score
            if student_score> valid_score:
                print('welcome to FCS!')

            # hacker rank score not valid
            else:
                print('insufficient hacker rank score')

        # residency not valid
        else:
            print('foreign country')

    # insufficient age
    else: 
        print('insufficient age')

# Age is not an integer
except ValueError:
    print('Age is not an integer')




# Exercise 2

print('Exercise 2')

# not required but added to handle non-integers
try:
    # input an integer
    num= int(input('Please input an integer number: '))

    #check if number is even
    if num % 2==0:
        # even number
        print('This number is even.')
    else:
        # odd number
        print('This number is odd.')

# Age is not an integer
except ValueError:
    print('Number is not an integer')