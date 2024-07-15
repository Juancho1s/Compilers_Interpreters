from PredictiveMatrix import predictiveMatrix
from Grammar import grammar


class LL1Parser:
    def __init__(self, parsing_table, grammar, start_symbol):
        self.parsing_table = parsing_table
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, tokens):
        stack = ['$', self.start_symbol]
        tokens.append("$")
        index = 0

        while len(stack) > 0:
            top = stack.pop()
            current_token = tokens[index]

            print(f"Stack: {stack}")
            print(f"Current Token: {current_token}")
            print(f"Remaining Tokens: {tokens[index:]}")

            if top == current_token:
                index += 1
            elif top in self.grammar and current_token in self.parsing_table[top]:
                rule = self.parsing_table[top][current_token]
                print(f"Applying Rule: {top} -> {rule}")
                if rule != ["epsilon"]:
                    stack.extend(rule[::-1])
            else:
                print("Error: Invalid token or missing rule")
                return False

        return index == len(tokens)


def tokenize(program):
    keywords = {
        "!init",
        "¡end",
        "var",
        "integer",
        "decimal",
        "string",
        "bool",
        "for",
        "while",
        "read",
        "write",
        "if",
        "then",
        "endif",
        "else",
        "do",
    }
    symbols = {
        ";",
        ":",
        "{",
        "}",
        "=",
        "+",
        "-",
        "*",
        "/",
        "&&",
        "||",
        "<",
        "<=",
        "=",
        ">",
        ">=",
        "!=",
        "(",
        ")",
        ":=",
        ",",
    }
    tokens = []
    token = ""
    for char in program:
        if char.isspace():
            if token:
                tokens.append(token)
                token = ""
        elif char in symbols:
            if token:
                tokens.append(token)
                token = ""
            tokens.append(char)
        else:
            if char != "Â":  # This handles the special character issue
                token += char
    if token:
        tokens.append(token)

    return tokens


parser = LL1Parser(predictiveMatrix, grammar, "PROGRAM")

print("Valid Example:")

content = ""

with open("Program1.txt", "r", encoding="utf-8") as file:  # Ensure proper encoding
    content = file.read()

print("Program Content:\n", content)
tokens = tokenize(content)
print("Tokens:\n", tokens)
result = parser.parse(tokens)
print(f"Example: {content} - {'Valid' if result else 'Invalid'}")
