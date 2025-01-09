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


queue=Queue()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)
print(queue.inbound_stack)
print("outbound stack:",queue.outbound_stack)
queue.dequeue()
print("inbound stack after dequeue:",queue.inbound_stack)
print("outbound_stack after dequeue",queue.outbound_stack)
queue.dequeue()
print("outbound_stack after dequeue",queue.outbound_stack)
