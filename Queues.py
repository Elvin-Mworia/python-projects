class Queue:
   def __init__(self):
      self.inbound_stack=[]
      self.outbound_stack=[]
     
    
  #adding an element in front of the queue
   def enqueue(self,data):
      self.inbound_stack.append(data)
      
 
   #removing an last element from the queue
   def dequeue(self):
     data=self.items.pop()
     self.size-=1
     return data
      