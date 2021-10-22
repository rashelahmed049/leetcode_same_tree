class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = node(data)
        else:
            self.data = data
            
    def display(self):
        if self.left:
            self.left.display()
        print(self.data)
        if self.right:
            self.right.display()
def compare(p,q):
    if p is None and q is None:
        return True
    if (p and q is None) or (q and p is None):
        return False
    if p.data == q.data and compare(p.left,q.left) and  compare(p.right,q.right):
        return True
    return False
            
r = node(3)
r.insert(5)
r.insert(2)

q = node(3)
q.insert(5)
q.insert(2)

print(compare(r,q))
        
                