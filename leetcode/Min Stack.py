class MinStack:
    
    def __init__(self):
        self.dl = []
        self.sl = []
        
    def push(self,x):
        self.dl.append(x)
        if not self.sl:
            self.sl.append(x)
        else:
            if x <= self.sl[-1]:
                self.sl.append(x)
    
    def top(self):
        return self.dl[-1]
    
    def getMin(self):
        return self.sl[-1]
    
    def pop(self):
        x = self.dl.pop(-1)
        if x <= self.sl[-1]:
            self.sl.pop(-1)
        return x
