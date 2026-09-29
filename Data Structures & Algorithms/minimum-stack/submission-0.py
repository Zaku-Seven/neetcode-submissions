class MinStack:

    def __init__(self):

        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:

        self.stack.pop(-1)
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:

        return min(self.stack)
        

    # essentially building out the stack class with init self and its functions being pop, push, top, and getMin

    #push --> putting a new element onto the stack, the val will be on top so if we pop it we will see that value once again, stack height increases by 1

    #pop --> remove function of the stack, height moves by one and the top of the stack is gone and the value below takes the top of the stack

    #top allows you to see the top of the stack, most recent value

    #getmin gets you the lowest value in the stack


    #constraints:
    #functions are called always on non-empty stacks, therefore if top() is empty, immedietly break/return thus we don't need a checker!!



    #thinking about solutions:

    #init stack = to an empty array


