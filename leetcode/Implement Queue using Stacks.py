class MyQueue:
    
    def __init__(self):
        self.l = []
        
    def push(self,x):
        self.l.append(x)
    
    def pop(self):
        x = self.l[0]
        self.l = self.l[1:]
        return x
        
    def peek(self):
        return self.l[0]
    
    def empty(self):
        return not self.l
