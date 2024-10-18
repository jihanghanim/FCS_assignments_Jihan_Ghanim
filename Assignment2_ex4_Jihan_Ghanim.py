#Assignment 2
#Exercise 4

words= 'Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality Open your eyes, look up to the skies and see I\'m just a poor boy, I need no sympathy Because I\'m easy come, easy go, little high, little low Any way the wind blows doesn\'t really matter to me, to me Mama, just killed a man Put a gun against his head, pulled my trigger, now he\'s dead Mama, life had just begun But now I\'ve gone and thrown it all away Mama, ooh, didn\'t mean to make you cry If I\'m not back again this time tomorrow Carry on, carry on as if nothing really matters Too late, my time has come Sends shivers down my spine, body\'s aching all the time Goodbye, everybody, I\'ve got to go Gotta leave you all behind and face the truth Mama, ooh (any way the wind blows) I don\'t wanna die I sometimes wish I\'d never been born at all I see a little silhouetto of a man Scaramouche, Scaramouche, will you do the Fandango? Thunderbolt and lightning, very, very frightening me (Galileo) Galileo, (Galileo) Galileo, Galileo Figaro, magnifico But I\'m just a poor boy, nobody loves me He\'s just a poor boy from a poor family Spare him his life from this monstrosity.'

int1= int(input('Please enter the first integer: '))
int2= int(input('Please enter the second integer: '))



if  int2 > len(words) or int1 > len(words) or int1 < -1 * len(words) or int1 < -1 * len(words):
    #the integers should not be greater that the length of the string
    if int2 > len(words) or int1 > len(words):
        print(f'The integer(s) cannot exceed {len(words)}.')

    #the integers should not be smaller that the negative value of string length
    if int1 < -1 * len(words) or int2 < -1 * len(words):
        print(f'The integer(s) cannot exceed -{len(words)}.')

    
#both integers have same sign and int1 is smaller than or equal to  int2
#we do not want to read words from right to left to avoid weird words
elif (int1>= 0 and int2>= 0 and  int1 <=int2) or (int1< 0 and int2< 0 and  int1 <=int2):
        #we want the index of int1 and int2 to be incusive
        if int2== -1:
            print(words[int1:])
        else:   
            print(words[int1:int2 +1])

#both integers have same sign but int1 is larger than int2
elif (int1>= 0 and int2>= 0 and  int1 >int2) or (int1< 0 and int2< 0 and  int1 >int2):
    #we do not want to read words from right to left to avoid weird words
    print('The first integer should be smaller than or equal to the second integer.')

#integers have different signs to avoid confusion
elif (int1>= 0 and int2< 0) or (int1<0 and int2>=0):
    print('The integers should have same sign.')

