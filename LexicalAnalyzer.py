from TransitionTable import transitionTable, finalStages, codes


class LexicalAnalyzer:
    def __init__(self, tokensTxtPath, errorsTxtPath):
        self.currentState = 1
        self.currentLine = 1
        self.tokensTxtPaht = tokensTxtPath
        self.errorsTxtPath = errorsTxtPath
        self.tokensHolder = []
        self.reservedWords = ["¡init", "end!", "array", "then", "var", "endif", "integer", "repeat", "else", "until", "string", "for", "write", "do", "if", "char", "while", "bool", "read", "true", "false", "of", "decimal", "program"]
    
        
    def getFileContent(self, path):
        try:
            with open(path, 'r', encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print(f"The file at {path} was not found.")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""
        
    def interpret_escape_sequences(self, s):
        """Interpret common escape sequences in a string."""
        escape_sequences = {
            '\\n': '\n',
            ' ': ' '
        }
        return escape_sequences.get(s, s)
        
    def get_transition(self, char, state):
        for key, value in transitionTable[state].items():
            
            if len(key) == 1 and char == key:

                return value
            
            elif '-' in key:
                start, end = key.split('-')
                if start <= char <= end:
                    return value
                continue
                
            interpreted_key = self.interpret_escape_sequences(key)
            
            if char in interpreted_key:

                if char == "\n":
                    self.currentLine += 1
                    
                return value
        return None

    def write(self, currentToken, path, message):
        try:
            with open(path, "a", encoding="utf-8") as file:
                if "ignore" not in message: 
                    if any(i in message for i in ["reserved word", "arithmetic", "relational", "logical", "assignment"]):
                        self.tokensHolder.append(currentToken["token"])
                        
                    else: 
                        self.tokensHolder.append(message)
                        # file.write(message)
                
            return (True, {
                "type": "",
                "token": ""
            })
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return (False, None)
        
    def generateToken(self, content):
        if content == "": return []
        
        currentToken = {
            "type": "",
            "token": ""
        }
        
        i = 0
        
        while i < (len(content)):
            if content[i] == "Â": 
                i += 1
                continue

            transition = self.get_transition(content[i], self.currentState)

            if transition is None:
                print(f"Lexical error at line {self.currentLine}: invalid character '{content[i]}'")
                return []

            if transition[0] == -1:
                
                if self.currentState in finalStages:
                    self.currentState = 1
                    writing = self.write(currentToken, self.tokensTxtPaht, f"{currentToken['type']}")
                    
                    if writing[0] == False: return []
                    
                    currentToken = writing[1]
                    continue
                    
                else:
                    print(f"Lexical error at line {self.currentLine}: invalid token")
                    return []

            self.currentState = transition[0]
            currentToken["type"] = codes[transition[1]]
            currentToken["token"] += content[i]
                
            if transition[1] == 600 and not self.coincidence(currentToken["token"]):
                print(f"Lexical error at line {self.currentLine}: invalid reserved word")
                return []
            
            i += 1
            
            if i == len(content):
                if self.currentState in finalStages:
                    writing = self.write(currentToken, self.tokensTxtPaht, f"{currentToken['type']}")
                
                else:
                    print(f"Lexical error at line {self.currentLine}: invalid token")
                    return []
                
                return self.tokensHolder
   
                
    def coincidence(self, word):
        for i in range(len(self.reservedWords)):
            if len(word) > len(self.reservedWords[i]):
                pass
            if self.reservedWords[i] == word:
                return True
            
            for j in range(len(word)):
                if word[j] != self.reservedWords[i][j]:
                    break
                
                if j == len(word) - 1:
                    return True
                
        return False



