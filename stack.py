"""
github:https://github.com/sodiqoydinov
"""
class Stack:
    def __init__(self):
        self.stack=[]
        
    def isEmpty(self):
        """Bo'sh ekanligini tekshirish"""
        return len(self.stack)==0
    
    def push(self,data):
        """Element qo'shish"""
        self.stack.append(data)
        return True
    
    def pop(self):
        """Element sug'urib olish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack.pop()
        
    def peek(self):
        """Eng ustki elementni ko'rish"""
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.stack[-1]