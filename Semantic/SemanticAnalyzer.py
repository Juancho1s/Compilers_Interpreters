from SymbolTable import symbolicTable

class SemanticAnalysis:
    
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        # semantic data types
        self.dataTypes = ["integer", "decimal", "string", "bool"]
        # symbol table values
        self.types = symbolicTable["type"]
        self.names = symbolicTable["name"]
        # possible operators in semantic analysis
        self.operations = ["+", "-", "*", "/", "//", "%"]
        

    def semanticAnalysis(self, tokens, index):
    
        # Flags for grammar analysis
        semanticFlags = {
            "DECLARE": False,
            "ASIGN": False,
            "IF STAT": False,
            "WHILE STAT": False,
            "FOR STAT": False
        }
            
        # token of syntactic analysis
        current_token = tokens["tokensAnalysis"][index]
        # token of semantic analysis
        current_instance = tokens["tokens"][index]
        
        # switch of corresponding procedure
        if current_token == "DECLARE":
            if current_instance in self.names: 
                print("Error: already existing declaration")
                return False
            
            semanticFlags["DECLARE"] = True
            
        elif current_token  == "ASIGN":
            if current_instance in self.names:
                semanticFlags["ASIGN"] = True
                symbolIndex = self.names.index(tokens["tokens"])
            else:
                print("Error: Variable not declared")
                return False
                
        elif current_token == "IF STAT":
            semanticFlags["IF STAT"] = True
            
        elif current_token == "WHILE STAT":
            semanticFlags["WHILE STAT"] = True

        elif current_token == "FOR STAT":
            semanticFlags["FOR STAT"] = True
            
        # review of semantic flags
        if semanticFlags["DECLARE"] == True:
            
            if current_token == "identifier":
                
                if current_token in self.names: 
                    print("Error: semantic error while declaring")
                    return False
                
                self.names.append(tokens["tokens"])
                
            elif current_token in self.dataTypes:
                self.types.append(current_token)
                symbolicTable["value"].append(tokens[tokens])
                
            elif current_token == ";":
                semanticFlags["DECLARE"] = False
        
        elif semanticFlags["ASIGN"] == True:
            if ((current_token == "identifier" and 
                current_instance in self.names and
                self.types[symbolIndex] == self.types[self.names.index(current_instance)]) or 
                (current_token in self.dataTypes and self.types[symbolIndex] == current_token) or
                current_token in self.operations):
                pass
            
            elif current_token == ";":
                semanticFlags["ASIGN"] = False
                
            else:
                print("Error: semantic error while assigning")
                return False