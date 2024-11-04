class Node:
    def __init__(self,info,n):
        self.info=info
        self.next=n
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def addToTail(self,val): 
        if self.size==0: 
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,None)
            self.tail.next=n
            self.tail=n
            
            self.size+=1

    def deleteHead(self): 
        if self.size==0:
            return 
        if self.size==1:
            val=self.head.info
            self.head=None
            self.tail=None
            self.size=0
            return val
        
        else:
            val=self.head.info
            self.head=self.head.next
            self.size-=1
            return val

class Queue:
    def __init__(self):
        self.elements=LinkedList()
    
    def enqueue(self,val): #O(1)
        self.elements.addToTail(val)
    
    def dequeue(self): #O(1)
        return self.elements.deleteHead()
    


#check balance for a certain symbol in a giver expression: (), {}, []
def checkExpression(char1, char2, fullchar, expression):

    string_par=''
    q=Queue()
    #if char1 or char2 in expression, store it in queue
    for s in expression:
        if s==char1 or s==char2:
            q.enqueue(s)
    #dequeue the strored char1 and char2 and write them in string_par
    for i in range(q.elements.size):        
        string_par += q.dequeue()
    #check if string_par is a balanced symbol(s)
    if string_par !=None and string_par!= fullchar * (len(string_par)//2):
        print('False')
        return False
    return True


def checkBalance(expression):
    char1='('
    char2=')'
    fullchar= '()'
    #if expression contains '(' or ')', check if it has balanced symbol(s) of '()'
    balance= checkExpression(char1, char2, fullchar,expression)
    if balance== False:
        return
    
    char1='['
    char2=']'
    fullchar= '[]'
    #if expression contains '[' or ']', check if it has balanced symbol(s) of '[]'
    balance= checkExpression(char1, char2, fullchar,expression)
    if balance== False:
        return
    
    char1='{'
    char2='}'
    fullchar= '{}'
    #if expression contains '{' or '}', check if it has balanced symbol(s) of '{}'
    balance= checkExpression(char1, char2, fullchar, expression)
    if balance== False:
        return
    print('True')

expression =input('Enter expression: ')
checkBalance(expression)

