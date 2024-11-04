#Exercise1


class Stack:
    def __init__(self):
        self.elements=[]
    def push(self,val): #O(1)
        self.elements.append(val)
    def pop(self): #O(1)
        if len(self.elements)==0:
            return None
        return self.elements.pop()
class Palindrome:
    def __init__(self,string1):
        self.string1= string1.lower()
    def check(self):
        s=Stack()
        string2= ''
        for i in self.string1:
            s.push(i)
        for i in range(len(self.string1)):
            string2 +=s.pop()
        if string2== self.string1:
            print(self.string1,'is a palindrome.')
        else:
            print(self.string1,'is a not a palindrome.')
        
p=Palindrome('mom')
p1= Palindrome('Neveroddoreven')
p.check()
p1.check()


