from Syntactic.SyntacticAnalyzer import LL1Parser
from Lexical.LexicalAnalyzer import LexicalAnalyzer 
from LL1Structure.Grammar import grammar
from LL1Structure.PredictiveMatrix import predictiveMatrix


if __name__ == "__main__":
    myInstance = LexicalAnalyzer(
        "C:\\Users\\POERT\\Desktop\\Universidad\\8th cuater\\compilers and interpreters\\TestFiles\\Tokens.txt",
        "C:\\Users\\POERT\\Desktop\\Universidad\\8th cuater\\compilers and interpreters\\TestFiles\\Errors.txt"
    )
    
    content = myInstance.getFileContent("C:\\Users\\POERT\\Desktop\\Universidad\\8th cuater\\compilers and interpreters\\TestFiles\\Program2.txt")
    
    parser = LL1Parser(predictiveMatrix, grammar, "PROGRAM")

    myTokens = myInstance.generateToken(content)
    
    print(myTokens)
    
    result = parser.parse(myTokens)
    
    print(f"Example: {content} - {'Valid' if result else 'Invalid'}")