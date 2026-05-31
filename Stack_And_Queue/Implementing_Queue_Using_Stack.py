class myQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
    def dequeue(self):
        if not self.s1:
            return  
        self.s1.pop()
    def front(self):
        if not self.s1:
            return -1
        return self.s1[-1]
    def size(self):
        return len(self.s1)

  class myQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    def enqueue(self, x):
        self.s1.append(x)
    def dequeue(self):
        if not self.s1 and not self.s2:
            return
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        self.s2.pop()
    def front(self):
        if self.s2:
            return self.s2[-1]
        if self.s1:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]
        return -1  
    def size(self):
        return len(self.s1) + len(self.s2)

  class myQueue:
    def __init__(self):
        self.s = []
    def enqueue(self, x):
        self.s.append(x)
    def dequeue(self):
        if not self.s:
            print("Queue Underflow")
            return
        x = self.s.pop()
        if not self.s:
            return
        self.dequeue()
        self.s.append(x)
        return
    def front(self):
        if not self.s:
            print("Queue is empty")
            return -1
        x = self.s.pop()
        if not self.s:
            self.s.append(x)
            return x
        item = self.front()
        self.s.append(x)
        return item
    def size(self):
        return len(self.s)
