#GUISE - The Symbolic Integrator in Python
#Get Used to Integrating on StEroids
#Lynch Envy Thru AI Labs(L.E.TH.A.L)
#GUISE IS CURRENTLY MUCH LIKE A SAINT.
#Cleanesch Verzhion
#Eine sauberere Version, die derzeit im Bau
#We need to create a function representation technique
#so that we can show the computer what a polynomial is.
#Also, we need a factorization routine.
import os
import numpy as np
np.set_printoptions(threshold=np.nan)
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
class ExpressionBlock:
    def __init__(self):
        self.val = []#The Algebraic Expression
        self.level = None#The depth of manipulation. See depth.py for more details
        self.opstat = None #Is it an op?
        self.op = None #If yes, then what?
    def isop(self):
        return self.opstat
    
    
    
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
    
main = ExpressionBlock()    
main.val = input
print main.val
inpar = []
p_count = 1
status = 0 #parantheses status
i=0
counter=0
#We define an empty dictionary of expression values
dict = {}
for j in range(100):
    dict[j] = ExpressionBlock()
#Now every element of dict is an (independent, unconnected) ternary tree
for e in main.val:
    if e == '(':
        status = 1
        p_count = p_count + 1 #Level checking parantheses counters
    elif e == ')':
        status = 0
        p_count = p_count - 1
    if status == 1 and e != '(':
        #inpar.append(e)
        if e in ops:
            dict[i].op = e
            dict[i].val = e
            dict[i].level = p_count
            dict[i].opstat = 1
            counter = counter + 1
        else:
            dict[i].op = None
            dict[i].val = e
            dict[i].level = p_count
            dict[i].opstat = 0
            counter = counter + 1
        i = i + 1
    elif status == 0 and e != ')':
            dict[i].op = e
            dict[i].val = e
            dict[i].level = p_count
            dict[i].opstat = 1
            counter = counter + 1
            i = i + 1

print inpar
print p_count
print 'Counter Value Breakpoint Here!'
print counter
for i in range(counter):
    print i
    print 'Value:'
    print dict[i].val
    print 'Opstat'
    print dict[i].opstat
    print 'Level'
    print dict[i].level
output = []
aux = []#should be set to empty after every parse pass
EL = []
#Main evaluation logic. Its simpliefied because of the ExpressionBlock Structure.
for i in range(counter):
    if dict[i].level == 2 and dict[i].opstat==0:
       EL.extend(dict[i].val)
    if dict[i].level == 1 and dict[i].opstat==1:
        EL.extend(dict[i].val)
        aux = EL
    if dict[i].level == 2 and dict[i].opstat==1:
        EL.extend(dict[i].val)
        aux.extend(dict[i+1].val)
        EL.extend(aux)

print EL


    