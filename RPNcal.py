class Algorithms(object):

    def calculator(input, output):
        stack = StackAsLinkedList()
        for line in input.readlines():
            for word in line.split():
                if word == "+":
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    stack.push(arg1 + arg2)
                elif word == "*":
                    arg2 = stack.pop()
                    arg1 = stack.pop()
                    stack.push(arg1*arg2)
                elif word == "=":
                    arg = stack.pop()
                    output.write(str(agr)+ "\n")
                else:
                    stack.push(int(word))
    calculator = staticmethod(calculator)
