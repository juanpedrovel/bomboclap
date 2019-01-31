# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    k = None
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i+1))

        if next == ')' or next == ']' or next == '}':
            if opening_brackets_stack:
                top = opening_brackets_stack.pop()
                a = top.Match(next)
                if a == False:
                    print(i+1)
                    k = 1
                    break
            else:
                print(i+1)
                k = 1
                break
    if not k:
        if not opening_brackets_stack:
            print("Success")
        else:
            print(opening_brackets_stack[0].position)
            

    # Printing answer, write your code here\