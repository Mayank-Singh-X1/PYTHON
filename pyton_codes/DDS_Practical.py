class Stack:
    def __init__(self):
        self.stack=[]

    def isempty(self):
        return len(self.stack)==0
    
    def push(self,value):
        self.stack.append(value)
        print(f"Pushed {value}")

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        value=self.stack.pop()
        print(f"value popped {value}")
    
    def peek(self):
        if self.isempty():
            print("Stack is empty")
            return None
        print(f"top element is {self.stack[-1]}")

    def traverse(self):
        if self.isempty():
           print("Stack is empty")
           return None
        for i in reversed(self.stack):
            print(i)

    def search(self,target):
        if self.isempty():
           print("Stack is empty")
           return None
        for i in range(len(self.stack)):
            if self.stack[i]==target:
                pos=len(self.stack)-i
                print(f"Match found at {pos}") 
                return         
        print("no match found")

s=Stack()
s.push(130)
s.push(20)
s.push(50)
s.pop()
s.search(130)
s.traverse()
        
         


        


