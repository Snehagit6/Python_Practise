from Python.data_structures.stacks.stack import Stack


def balanced_parentheses(parentheses: str) -> bool:
    """Use a stack to check if a string of parentheses is balanced.
    >>> balanced_parentheses("([]{})")
    True
    >>> balanced_parentheses("[()]{}{[()()]()}")
    True
    >>> balanced_parentheses("[(])")
    False
    >>> balanced_parentheses("1+2*3-4")
    True
    >>> balanced_parentheses("")
    True
    """
    stack = Stack()
    print(f"Stack : {stack}")
    bracket_pairs = {"(": ")", "[": "]", "{": "}"}
    for bracket in parentheses:
        print(f"bracket : {bracket}")
        if bracket in bracket_pairs:
            stack.push(bracket)
            print(f"Updated Stack : {stack}")
        elif bracket in (")", "]", "}"):
            print(bracket_pairs[stack.pop()])
            if stack.is_empty() or bracket_pairs[stack.pop()] != bracket:
                return False
    return stack.is_empty()


if __name__ == "__main__":
    # from doctest import testmod
    #
    # testmod()

    examples = ["((()))", "((())", "(()))"]
    print("Balanced parentheses demonstration:\n")
    for example in examples:
        not_str = "" if balanced_parentheses(example) else "not "
        print(f"{example} is {not_str}balanced")
