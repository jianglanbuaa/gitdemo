# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:44:59 2020

@author: jiang
"""

class Stack:
    def __init__(self):
       self.items = []
       
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)


def infixToPostfix(tokenList):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    
    for token in tokenList:
        if token in "+-*/":
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            postfixList.append(token)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return postfixList

def change(string):
    l = []
    num_string = ""
    for i in range(len(string)):
        if string[i] in "0123456789":
            num_string = num_string + string[i]
        else:
            if num_string != "":
                l.append(num_string)
                num_string = ""
            l.append(string[i])
        if i == len(string)-1:
            if num_string != "":
                l.append(num_string)
    return l


a = change(input())
list_post = infixToPostfix(a)
list_num = []
for i in list_post:
    if i in "+-*/":
        m2 = list_num.pop()
        m1 = list_num.pop()
        if i == "+":
            list_num.append(m1+m2)
        if i == "-":
            list_num.append(m1-m2)
        if i == "*":
            list_num.append(m1*m2)
        if i == "/":
            list_num.append(m1//m2)
    else:
        list_num.append(eval(i))

print(list_num[0])
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    