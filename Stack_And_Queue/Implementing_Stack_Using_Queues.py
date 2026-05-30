#Approach-1
from collections import deque
class myStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        self.q2.append(x)
        while len(self.q1) != 0:
            self.q2.append(self.q1[0])
            self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        
    def pop(self):
        if len(self.q1) == 0:
            return
        self.q1.popleft()
        
    def top(self):
        if len(self.q1) == 0:
            return -1
        return self.q1[0]
        
    def size(self):
        return len(self.q1)

#Approach-2
from collections import deque
class myStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            return
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1

    def top(self):
        if not self.q1:
            return -1
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        temp = self.q1.popleft()
        self.q2.append(temp)
        self.q1, self.q2 = self.q2, self.q1
        return temp

    def size(self):
        return len(self.q1)

#Approach-3
from collections import deque
class myStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        sz = len(self.q)
        for i in range(sz - 1):
            self.q.append(self.q[0])
            self.q.popleft()

    def pop(self):
        if self.q:
            self.q.popleft()

    def top(self):
        if not self.q:
            return -1
        return self.q[0]
      
    def size(self):
        return len(self.q)
