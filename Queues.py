class Queue:
   def __init__(self):
      self.items=[]
      self.size=0
    
  #adding an element in front of the queue
   def enqueue(self,data):
      self.items.insert(0,data)
      self.size+=1
 

