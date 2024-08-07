from Semantic.SymbolTable import symbolicTable
from Semantic.SemanticAnalyzer import SemanticAnalysis


class LL1Parser:
    def __init__(self, parsing_table, grammar, start_symbol):
        self.parsing_table = parsing_table
        self.grammar = grammar
        self.start_symbol = start_symbol

    def parse(self, tokens):
        semantics = SemanticAnalysis(tokens)
        stack = ['$', self.start_symbol]
        tokens["tokensAnalysis"].append("$")
        index = 0
        
        # Map of variables
        symbolIndex = 0

        # analysis semantic and syntactic
        while len(stack) > 0:
            top = stack.pop()
            
            # set for each semantic flag is any conincidence
            if not semantics.semanticFlagsSet(index, top): return False
            
            # token of syntactic analysis
            current_token = tokens["tokensAnalysis"][index]
                
            # analysis of tokens grammar
            if top == current_token:
                # Analysis of each corresponding structure or operation in semantics processes
                if not semantics.semanticAnalysis(index):
                    # print an error
                    print("Error in semantic analysis")
                    return False
                
                # consecuence
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