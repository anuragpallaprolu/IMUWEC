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
            
print 'Reached breakpoint, to read exprnode'
raw_input('Continue?')
my_expr = exprnode('*',
    exprnode('+',
        exprnode(2),
        exprnode(3)),
    exprnode(4))
    
my_expr.evaluate()