import re
import count_value


def command(c):
    if c == "/exit":
        print("Bye")
        exit()
    elif c == "/help":
        print("The program calculates the sum of numbers")
    else:
        print("Unknown command")


def test_identifier(identifier):
    return identifier.isalpha()


def get_number(num):
    num = num.strip(" ")
    if test_identifier(num):
        if num in count_value.MathematicsOperation.variable.keys():
            print(count_value.MathematicsOperation.variable[num])
        else:
            print("Unknown variable")
            return
    else:
        print(int(num))


def test(identifier, variable):
    if test_identifier(identifier):
        if variable.isdigit():
            count_value.MathematicsOperation.variable[identifier] = int(variable)
            return True
        elif variable in count_value.MathematicsOperation.variable.keys():
            count_value.MathematicsOperation.variable[identifier] = count_value.MathematicsOperation.variable[variable]
            return True
        else:
            print("Invalid assignment")
    else:
        print("Invalid identifier")
        return False


def new_argument(argument):
    argument = argument.split('=')
    argument[0] = argument[0].replace(" ", "")
    argument[1] = argument[1].replace(" ", "")
    if len(argument) == 2:
        test(argument[0], argument[1])
    else:
        print("Invalid assignment")


while True:
    text = input()
    try:
        if text.find('/') == 0:
            command(text)
        elif text.find('=') != -1:
            new_argument(text)
        elif re.search("[+-/*/()]", text):
            mathematics_operation = count_value.MathematicsOperation(text)
            if mathematics_operation.deal_with_many_operators():
                mathematics_operation.test_operation()
        elif len(text) > 0:
            get_number(text)

    except IndexError:
        pass
