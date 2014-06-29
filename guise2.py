#GUISE - The Symbolic Integrator in Python
#Get Used to Integrating on StEroids
#GUISE IS CURRENTLY MUCH LIKE A SAINT.
#Cleanesch Verzhion
#We need to create a function representation technique
#so that we can show the computer what a polynomial is.
#Also, we need a factorization routine.
import os
import numpy as np
#terminal to list reader: Needed for processing symbolic math
def terminal():
    tlist = []
    tlist = raw_input('*')
    print tlist
    return tlist
#
#Tree Data Structure: The AST Tree
class exprnode(object):
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    
    def evaluate(self):
        if self.value == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.value == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.value == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.value == '/':
            return self.left.evaluate() / self.right.evaluate()
        else:
            return self.value
            
my_expr = exprnode('*',
    exprnode('+',
        exprnode(2),
        exprnode(3)),
    exprnode(4))
#
#Generic Tree

class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
#
while(1):
    ops = ['+','-','*','/']
    parantheses=['(',')']
    input = terminal()
    j=0
    k=0
    l=0
    processed = np.chararray((len(input),1))
    oplist = []
    parlist = []
    for e in input:
        if e in ops:
            oplist.append(e)
            processed[j,0]=k
            k = k + 1
        else:
            if e in parantheses:
                oplist.append(0)
                parlist.append(e)
                processed[j,0]=l
                l = l + 1
            else:
                processed[j,0]=e
        
        j=j+1
                
    print processed
    print oplist
    print parlist
    