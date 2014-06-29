#GUISE - The Symbolic Integrator in Python
#Get Used to Integrating on StEroids
#GUISE IS CURRENTLY MUCH LIKE A SAINT.

#We need to create a function representation technique
#so that we can show the computer what a polynomial is.
#Also, we need a factorization routine.

#terminal to list reader: Needed for processing symbolic math
def terminal():
    tlist = []
    tlist = raw_input('*')
    print tlist
    return tlist
#
#Tree Data Structure
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

input = terminal()
