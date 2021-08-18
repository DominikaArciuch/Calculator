from collections import deque
import re


class MathematicsOperation:
    variable = dict()

    def __init__(self, operation):
        self.output_queue = deque()
        self.operators_stack = deque()
        self.final_result_stack = deque()
        operation = re.split(r"(\W)", operation)
        self.operation = [x.strip() for x in operation if x.strip()]

    def test_operation(self):
        if self.operation.count("(") != self.operation.count(")"):
            print("Invalid expression")
            return False

        MathematicsOperation.create_stacks(self)
        # print(self.operators_stack)
        # print(self.output_queue)
        MathematicsOperation.count(self)
        return True

    def deal_with_many_operators(self):
        i = 1
        bad = ['/', '*']
        first = self.operation[0]
        while i < len(self.operation) - 1:
            second = self.operation[i]
            if first in bad and second in bad:
                print("Invalid expression")
                return False
            if first == second and first not in ['(', ')']:
                self.operation.pop(i)
            else:
                first = second
            i += 1
        return True

    def create_stacks(self):
        for el in self.operation:
            if re.search("[+-/*/()]", el):
                MathematicsOperation.deal_with_operands(self, el)
            elif el.isalpha():
                try:
                    self.output_queue.append(self.variable[el])
                except KeyError:
                    print(f"Unknown variable {el}")
                    return False
            elif el.isdigit():
                self.output_queue.append(int(el))
            else:
                print("Invalid expression")
                return False
        while len(self.operators_stack) > 0:
            self.output_queue.append(self.operators_stack.pop())
        return True

    def deal_with_operands(self, operator):
        if len(self.operators_stack) == 0:
            self.operators_stack.append(operator)
        elif re.search("[+-/*]", operator):
            first = self.operators_stack.pop()
            higher_precedence = ["*", "/"]
            lower_precedence = ["-", "+"]
            if operator in higher_precedence:
                equal_higher = higher_precedence
            else:
                equal_higher = lower_precedence + higher_precedence
            while first in equal_higher:
                self.output_queue.append(first)
                if len(self.operators_stack) == 0:
                    self.operators_stack.append(operator)
                    return True
                first = self.operators_stack.pop()
            self.operators_stack.append(first)
            self.operators_stack.append(operator)

        elif operator == "(":
            self.operators_stack.append(operator)
        elif operator == ")":
            first = self.operators_stack.pop()
            while first != "(":
                self.output_queue.append(first)
                first = self.operators_stack.pop()
        else:
            print("Error, you use bad operand")
            return False
        return True

    def count(self):
        size = len(self.output_queue)
        self.output_queue.reverse()
        for i in range(size):
            el = str(self.output_queue.pop())
            if el.isdigit():
                self.final_result_stack.append(int(el))
            else:
                b = self.final_result_stack.pop()
                a = self.final_result_stack.pop()
                w = 0
                if el == "+":
                    w = a + b
                elif el == "-":
                    w = a - b
                elif el == "/":
                    try:
                        w = a / b
                    except ZeroDivisionError:
                        print(f"Error, division by 0: {b} / {a}")
                        return False
                elif el == "*":
                    w = a * b
                self.final_result_stack.append(w)
        a = self.final_result_stack.pop()
        print(int(a))
        return True
