grammar = {
  "PROGRAM": [["!init", "identifier", ";", "BODY", "¡end"]],
  "BODY": [["DECLARE", "MAIN"], ["MAIN"]],
  "DECLARE": [["var", "IDENTIFIERS", ":", "TYPES"]],
  "IDENTIFIERS": [["identifier", ";", "IDENTIFIERS'"]],
  "IDENTIFIERS'": [["identifier", ";", "IDENTIFIERS'"], [""]],
  "TYPES": [["DEFAULT"]],
  "DEFAULT": [["integer"], ["decimal"], ["string"], ["bool"]],
  "MAIN": [["{", "STATEMENTS", "}"]],
  "STATEMENT": [["ASIGN"], ["FOR STAT"], ["WHILE STAT"], ["INPUT"], ["OUTPUT"], ["IF STAT"]],
  "EXPRESION": [["EXP", "EXPRESION'"]],
  "EXPRESION'": [["REL", "EXP"], [""]],
  "REL": [["<"], ["<="], ["="], [">"], [">="], ["!="], ["||"]],
  "EXP": [["TERM", "EXP'"]],
  "EXP'": [["+", "TERM", "EXP'"], ["-", "TERM", "EXP'"], [""]],
  "ASIGN": [["identifier", "=", "EXPRESION"]],
  "TERM": [["FACTOR", "TERM'"]],
  "TERM'": [["*", "FACTOR", "TERM'"], ["/", "FACTOR", "TERM'"], ["&&", "FACTOR", "TERM'"], [""]],
  "FACTOR": [["{", "EXPRESION", "}"], ["identifier"], ["true"], ["string"], ["number"]],
  "STATEMENTS": [["STATEMENT", ";", "STATEMENTS'"]],
  "STATEMENTS'": [["STATEMENT", ";", "STATEMENTS'"], [""]],
  "FOR STAT": [["for", "CONTER", "do", "{", "STATEMENTS", "}"]],
  "CONTER": [["identifier", ":=", "EXPRESION", "for", "ROT"]],
  "WHILE STAT": [["while", "EXPRESION", "do", "{", "STATEMENTS", "}"]],
  "INPUT": [["read", "{", "ROS", "}"]],
  "ROS": [["identifier", ",", "ROS"], ["identifier"]],
  "OUTPUT": [["write", "(", "ROS", ")"]],
  "IF STAT": [["if", "EXPRESION", "then", "{", "STATEMENTS", "}", "ELSE", "endif"]],
  "ELSE": [["else", "{", "STATEMENTS", "}"], [""]],
  "ROT": [["EXPRESION"]]
}
