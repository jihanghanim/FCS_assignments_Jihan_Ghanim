class Node:
    def __init__(self,info,n):
        self.info=info
        self.next=n
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0 
        
    def addToHead(self,val): 
        if self.size==0: 
            n=Node(val,None)
            self.head=n
            self.tail=n
            self.size+=1
        else:
            n=Node(val,self.head)
            self.head=n
            self.size+=1
            
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
    
    def deleteTail(self): 
        if self.size<=1:
            return self.deleteHead()
        else:
            val=self.tail.info
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            self.tail=temp
            self.tail.next=None
            
            self.size-=1
            return val
    def printLL(self): 
        temp=self.head
        
        while temp!=None:
            print(temp.info," -> ",end=" ")
            temp=temp.next
        print()
        
    #delete at certain index
    def deleteAtLocation(self, indx):
        #delete head
        if indx==0:
            return self.deleteHead()
        #delete tail
        elif indx== self.size -1:
            return self.deleteTail()
        #delete in between node
        else:
            #if index> length of linkedlist
            if indx> self.size -1:
                s='location is out of range'
                return s
            #else start from index zero until reaching desired location 
            i=0
            temp=self.head
            while i != indx and temp!=None:
                i +=1
                #store current node
                temp_prev= temp
                #current node is next node
                temp=temp.next
            if i== indx:
                #delete node at this index
                temp_prev.next= temp.next
                temp.next= None
                self.size -=1
                return temp.info

#build linkedlist
l=LinkedList()
l.addToHead(0)
l.addToHead(11)
l.addToHead(76)
l.addToHead(56)
l.addToHead(12)
l.printLL()
#delete node
x=l.deleteAtLocation(3)
#print deleted node
print(x)
#print new linkedlist
l.printLL()