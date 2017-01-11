class Stack():
    """A FIFO stack of objects"""

    def __init__(self):
        """ (Stack) -> NoneType
        Creates an empty stack
        """
        self._contents = []

    def push(self, new_object):
        """

        :param new_object: generic obj
        :return: Nothing
        """
        # self._contents = [new_obj] + self._contents
        self._contents.append(new_object)

    def pop(self):
        """
        Stack
        :return: Object
        """
        # return_value = self._contents[0]
        # self._contents =self._contents[1:]
        return_value = self._contents[-1]
        self._contents = self._contents[:-1]
        return return_value

    def is_empty(self):
        """

        :return: returns true iff stack conatains data, BOOL
        """
        return len(self._contents) == 0


my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.pop())
my_stack.push("D")
while(not my_stack.is_empty()):
    print(my_stack.pop())
