class LL1Parser:
    def __init__(self, parsing_table, grammar, start_symbol):
        self.parsing_table = parsing_table
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, tokens):
        stack = ['$', self.start_symbol]
        tokens["tokensAnalysis"].append("$")
        index = 0

        while len(stack) > 0:
            top = stack.pop()
            current_token = tokens["tokensAnalysis"][index]

            if top == current_token:
                index += 1
            elif top in self.grammar and current_token in self.parsing_table[top]:
                rule = self.parsing_table[top][current_token]
                print(f"Applying Rule: {top} ->\t\t{rule}")
                if rule != ["epsilon"]:
                    stack.extend(rule[::-1])
            else:
                print("Error: Invalid token or missing rule")
                return False

        return index == len(tokens["tokensAnalysis"])