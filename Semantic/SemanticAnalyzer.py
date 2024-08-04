from .SymbolTable import symbolicTable
from decimal import Decimal

class SemanticAnalysis:
    
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        
        # semantic data types
        self.dataTypes = ["integer", "decimal", "string", "bool"]
        
        # index of current instance of assignation
        self.symbolIndex = 0
        
        # symbol table values
        for key in symbolicTable:
            print(key)
        
        self.types = symbolicTable["type"]
        self.names = symbolicTable["name"]
        self.values = symbolicTable["value"]
        
        # possible operators in semantic analysis
        self.operations = ["+", "-", "*", "/"]
        
        self.holder = None
        
        # Flags for grammar analysis
        self.semanticFlags = {
            "DECLARE": False,
            "ASIGN": False,
            "IF STAT": False,
            "WHILE STAT": False,
            "FOR STAT": False,
            "OPERATION": [False, ""]
        }
        

    def semanticAnalysis(self, index):
        if index >= len(self.tokens["tokens"]): return True  
        # token of syntactic analysis
        current_token = self.tokens["tokensAnalysis"][index]
        # token of semantic analysis
        current_instance = self.tokens["tokens"][index]
            
        # review of semantic flags
        if self.semanticFlags["DECLARE"] == True:
            
            if current_token == "identifier":
                
                if current_token in self.names: 
                    print("Error: semantic error while declaring")
                    return False
                
                self.names.append(self.tokens["tokens"][index])
                
            elif current_token in self.dataTypes:
                self.types.append(current_token)
                symbolicTable["value"].append(self.tokens["tokens"][index])
                
            elif current_token in [";", "{"]:
                self.semanticFlags["DECLARE"] = False
        
        elif self.semanticFlags["ASIGN"] == True:
            operation = self.semanticFlags["OPERATION"]
            
            if ((current_token == "identifier" and 
                current_instance in self.names and
                self.types[self.symbolIndex] == self.types[self.names.index(current_instance)])):
                
                indesToID = self.names.index(current_instance)
                
                if operation[0] == True:
                    if not self.operation(float(self.values[indesToID]), float(self.holder), operation[1]):
                        return False
                    
                else:
                    self.holder = self.values[indesToID]
            
            elif (current_token in self.dataTypes and self.types[self.symbolIndex] == current_token):
                if operation[0] == True:
                    if not self.operation(float(current_instance), float(self.holder), operation[1]):
                        return False
                    
                else:
                    self.holder = current_instance
                
            elif (current_token in self.operations):
                self.semanticFlags["OPERATION"] = [True, current_token]
            
            elif current_token == ";":
                self.semanticFlags["ASIGN"] = False
                symbolicTable["value"][self.symbolIndex] = self.holder
                
                self.holder = None
                self.semanticFlags["OPERATION"] = [False, ""]
                
        elif any(self.semanticFlags[flag] for flag in ["IF STAT", "WHILE STAT"]):
            
                
        return True
            
            
    def operation(self, current_instance, current_holder, operation):
        if self.types[self.symbolIndex] in ["integer", "decimal"]:
            if operation == "-":
                self.holder = current_instance - current_holder
            
            elif operation == "+":
                self.holder = current_instance + current_holder
                
            elif operation == "*":
                self.holder = current_instance * current_holder
                
            else:
                if self.holder == 0:
                    print("Error: division by zero")
                    return False
                self.holder = current_instance / current_holder
                
        elif self.types[self.symbolIndex] == "string":
            if operation == "+":
                self.holder = self.holder + current_instance
            
            else:
                print("Error: invalid operation for string")
                return False
            
        else: 
            print("Error: invalid operation for type")
            return False
        
        self.semanticFlags["OPERATION"] = [False, ""]
        return True
    
    
    def semanticFlagsSet(self, index, currentProduction):
        if index >= len(self.tokens["tokens"]): return True
        
        # token of syntactic analysis
        current_token = self.tokens["tokensAnalysis"][index]
        
        # token of semantic analysis
        current_instance = self.tokens["tokens"][index]
        
        # switch of corresponding procedure
        if "DECLARE" in currentProduction:
            if current_instance in self.names: 
                print("Error: already existing declaration")
                return False
            
            self.semanticFlags["DECLARE"] = True
            
        elif currentProduction  == "ASIGN":
            if current_instance in self.names:
                self.semanticFlags["ASIGN"] = True
                self.symbolIndex = self.names.index(self.tokens["tokens"][index])
            else:
                print("Error: Variable not declared")
                return False
                
        elif currentProduction == "IF STAT":
            self.semanticFlags["IF STAT"] = True
            
        elif currentProduction == "WHILE STAT":
            self.semanticFlags["WHILE STAT"] = True

        elif currentProduction == "FOR STAT":
            self.semanticFlags["FOR STAT"] = True
    
        return True