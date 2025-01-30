class Heap:
    def __init__(self):
        self.heap=[0]
        self.size=0
        
    def float(self,k):
        while (k//2>0):
            if(self.heap[k] <self.heap[k//2]):
                self.heap[k],self.heap[k//2]=self.heap[k//2],self.heap[k]
            k//=2

    def insert(self,item):
        self.heap.append(item)
        self.size+=1
        self.float(self.size)
    
    def minindex(self,k):# chooses the appropriate child to compare with the parent
        if (k*2+1>self.size):
            return k*2
        elif(self.heap[k*2]<self.heap[k*2+1]):
            return k*2
        else:
            return k*2+1
