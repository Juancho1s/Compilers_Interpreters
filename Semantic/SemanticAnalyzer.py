from .SymbolTable import symbolicTable

class SemanticAnalysis:
    
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        
        # semantic data types
        self.dataTypes = ["integer", "decimal", "string", "bool"]
        # will work with the previous declaration in order to know the type of comparisons
        self.conditionalType = None
        
        # index of current instance of assignation
        self.symbolIndex = None
        
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
            "CONDITIONAL": False,
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
            
            # Checking the declaration process
            if current_token == "identifier":
                
                # If the current instance is already declared
                if current_instance in self.names: 
                    print("Error: semantic error while declaring")
                    return False
                
                # Other wises it is written on the "symboltable"
                self.names.append(self.tokens["tokens"][index])
                
            # Now, to check corresponding type
            elif current_token in self.dataTypes:
                self.types.append(current_token)
                symbolicTable["value"].append(self.tokens["tokens"][index])
                
            # By the end seting the flag to flase when the statement is aready completed
            elif current_token in [";", "{"]:
                self.semanticFlags["DECLARE"] = False
        

        elif self.semanticFlags["ASIGN"] == True:
            operation = self.semanticFlags["OPERATION"]
            
            if (current_token == "identifier"):
                
                if not (current_instance in self.names): 
                    
                    print("Error: Variable not declared")
                    return False
                
                indexToID = self.names.index(current_instance)
                
                if operation[0] == True:
                    if self.types[indexToID] == "integer" and not self.operation(float(self.values[indexToID]), float(self.holder), operation[1]):
                        return False

                    elif not self.operation(self.values[indexToID], self.holder, operation[1]):
                        return False


                else:
                    self.holder = self.values[indexToID]
            
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
                self.symbolIndex = None
                self.semanticFlags["OPERATION"] = [False, ""]
                
        elif self.semanticFlags["CONDITIONAL"] == True:
            if current_token == "identifier":
                # Check if variable is declared
                if not (self.checkIdentifierExistence(current_instance)):
                    print("Error: Variable not declared")
                    return False
                
                elif not (self.types[self.names.index(current_instance)] == self.dataTypes[self.conditionalType]):
                    print("Error: Type mismatch")
                    return False
                
            elif current_token in self.dataTypes:
                if not(self.dataTypes[self.conditionalType] == current_token):
                    print("Error: Type mismatch")
                    return False

            elif current_token in ["do", "then"]:
                self.semanticFlags["CONDITIONAL"] = False
                self.conditionalType = None
                
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
                
            if self.types[self.symbolIndex] == "integet":
                self.holder = int(self.holder)
                
            else:
                self.holder = float(self.holder)
                
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
            if self.checkIdentifierExistence(current_instance): 
                print("Error: already existing declaration")
                return False
            
            self.semanticFlags["DECLARE"] = True
            
        elif currentProduction  == "ASIGN":
            if not (self.checkIdentifierExistence(current_instance)):
                print("Error: undeclared identifier")
                return False

            self.semanticFlags["ASIGN"] = True
            self.symbolIndex = self.names.index(current_instance)
                
        elif currentProduction in ["IF STAT", "WHILE STAT", "FOR STAT"]:
            if not (self.determineConditioal(index)):
                return False

            self.semanticFlags["CONDITIONAL"] = True
    
        return True

    def checkIdentifierExistence(self, id):
        if id in self.names:
            return True
        else:
            return False

    def determineConditioal(self, index):
        token = self.tokens["tokensAnalysis"][index + 1]
        tokenIdentity = self.tokens["tokens"][index + 1]

        if (token == "identifier"):
            if not (self.checkIdentifierExistence(tokenIdentity)):
                print("Error: undeclared identifier")
                return False

            self.conditionalType = self.dataTypes.index(self.types[self.names.index(tokenIdentity)])

        else:
            self.conditionalType = self.dataTypes.index(tokenIdentity)

        return True