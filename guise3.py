#GUISE - The Symbolic Integrator in Python
#Get Used to Integrating on StEroids
#GUISE IS CURRENTLY MUCH LIKE A SAINT.
#Cleanesch Verzhion
#Eine sauberere Version, die derzeit im Bau
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
#TERNARY OP TREE
#CRUCIAL FOR SIMPLIFICATION OPS
class TernaryTree:
    def __init__(self,expr,level):
        self.val = expr #The Algebraic Expression
        self.level = level#The depth of manipulation. See depth.py for more details
        self.leftExpr = None#Left Ternary Op Tree, for further subparanthesised algebra
        self.op = None#The op binding the left and right expressions
        self.rightExpr = None#Right Ternary Op Tree, for further SPA.
    
    def insertLexp(self,newLexp):
        if self.leftExpr == None:
            self.leftExpr = TernaryTree(newLexp)
        else:
            TExp = TernaryTree(newLexp)
            TExp.leftExpr = self.leftExpr
            self.leftExpr = TExp
    
    def insertOp(self,newOp):
        if self.op == None:
            self.op = TernaryTree(newOp)
        else:
            top = TernaryTree(newOp)
            top.op = self.op
            self.op = top
    
    def insertRexp(self,newRexp):
        if self.rightExpr == None:
            self.rightExpr = TernaryTree(newRexp)
        else:
            TExp = TernaryTree(newRexp)
            TExp.rightExpr = self.rightExpr
            self.rightExpr = TExp
    def getLexp(self):
        return self.leftExpr
    def getOp(self):
        return self.op
    def getRexp(self):
        return self.rightExpr
    def getExpr(self):
        return self.val
    def getLevel(self):
        return self.level
    
    
            
        
#

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
    
main = TernaryTree(input,0)    
print main.val
inpar = []
p_count = 1
status = 0 #parantheses status
i=0
#We define an empty dictionary of expression values
dict = {}
for j in range(100):
    dict[j] = TernaryTree()
#Now every element of dict is an (independent, unconnected) ternary tree
for e in main.val:
    if e == '(':
        status = 1
        p_count = p_count + 1 #Level checking parantheses counters
    elif e == ')':
        status = 0
        p_count = p_count - 1
    if status == 1:
        #inpar.append(e)
        if e in ops:
            dict[i].op = e
            dict[i].val = e
            dict[i].level = p_count
        else:
            dict[i].op = None
            dict[i].val.append(e)
            dict[i].level = p_count
    i = i + 1

print inpar
print p_count
print dict[1].val