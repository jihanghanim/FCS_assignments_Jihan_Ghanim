class Stack:
    def __init__(self):
        self.elements=[]
    def push(self,val): 
        self.elements.append(val)
    def pop(self): 
        if len(self.elements)==0:
            return None
        
        return self.elements.pop()
    
msg= input('Enter message: ')
output= ''
s=Stack()
for m in msg:
#once you reach an Asterix, pop one character out of your stack
    if m=='*':
        output += s.pop()
#push each alphabetical character your stack    
    else:
        s.push(m)
#pop remaining characters
l= len(s.elements)
for i in range(l):
    output += s.pop()
print(output)
