from Syntactic.SyntacticAnalyzer import LL1Parser
from Lexical.LexicalAnalyzer import LexicalAnalyzer 
from Semantic.SymbolTable import symbolicTable
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
    
    print("\n")
    
    showTable = ""

    # Print the headers (keys of the symbol table)
    for key in symbolicTable.keys():
        showTable += f"{key}\t\t"
    showTable += "\n"

    # Print a separator line for better readability
    showTable += "-" * 8 * len(symbolicTable) + "\n"

    # Get the maximum number of rows from the longest list in the dictionary
    num_rows = max(len(values) for values in symbolicTable.values())

    # Print each row
    for row_index in range(num_rows):
        for key in symbolicTable.keys():
            if row_index < len(symbolicTable[key]):
                showTable += f"{symbolicTable[key][row_index]}\t\t"
            else:
                showTable += "\t\t"  # Add empty space if the list is shorter
        showTable += "\n"

    print(showTable)