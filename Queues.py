class Queue:
   def __init__(self):
      self.inbound_stack=[]
      self.outbound_stack=[]
     
    
  #adding an element in front of the queue
   def enqueue(self,data):
      self.inbound_stack.append(data)
      
 
   #removing an last element from the queue using the inbound and outbound stack
   def dequeue(self):
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        return self.outbound_stack.pop()



