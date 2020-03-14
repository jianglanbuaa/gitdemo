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
    
"""
Update 1 

@author: jiang
""" 

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first<last:
        splitpoint = partition(alist, first, last)
        
        quickSortHelper(alist, first, splitpoint -1)
        quickSortHelper(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivotvalue = alist[first]
    
    leftmark = first + 1
    rightmark = last
    
    done = False
    while not done:
        
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    
    return rightmark

"""
Update 2 

@author: jiang
""" 
    
def merge_sort(lst):
if len(lst) <= 1:
    return lst

middle = len(lst)//2
left = merge_sort(lst[:middle])
right = merge_sort(lst[middle:])

merged = []
while left and right:
    if left[0] <= right[0]:
        merged.append(left.pop(0))
    else:
        merged.append(right.pop(0))
    
merged.extend(right if right else left)

return merged

    
    
    
    
    
    