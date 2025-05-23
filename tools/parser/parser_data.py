# I'm thinking about choosing only the necessary tokens for the test cases because the table will be too big and complicated.
valid_tokens = ["leftBrace", "rightBrace", "plus", "minus", "assignment", "multiply", "divide", "semicolon", "leftParen", "rightParen", "identifier", "integer", "dot", "true", "false", "printf", "int", "float", "bool", "main", "return"]

# Fix table_column according to the table
table_column = ["leftBrace", "rightBrace", "plus", "minus", "assignment", "multiply", "divide", "semicolon", "leftParen", "rightParen", "identifier", "integer", "dot", "true", "false", "printf", "int", "float", "bool", "main", "return", "$", "E'", "P", "B", "E", "T", "F", "A", "M", "R"]

# Fix table according to our valid tokens
table = [
#       {       }       +       -       =       *       /       ;       (       )      identifier  integer   dot     true    false   printf  int     float   bool    main   return    $       E'      P       B       E       T       F       A       M       R
        ["S4",  "R5",   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",      "S14",  None,   "S15",  "S16",  "S17",   "S9",  "S10",  "S11",   None,  "S18",  "R5",   None,   "1",     "2",   "3",    "8",   "6",     "5",   None,   "7"],  # 0
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "Acc",  None,   None,   None,   None,   None,  None,   None,  None,  None],  # 1
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "R1",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 2
        ["S4",  "R5",   "S20",  "S21",  None,   None,   None,   None,   "S12",  None,   "S13",     "S14",   None,   "S15",  "S16",  "S17",  "S9",   "S10",  "S11",   None,  "S18",   "R5",  None,   None,   "19",   "3",   "8",    "6",      "5",  None,  "7"],  # 3
        ["S4",  "R5",   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",     "S14",   None,   "S15",  "S16",  "S17",  "S9",   "S10",  "S11",   None,  "S18",   "R5",  None,   None,   "22",   "3",   "8",    "6",      "5",  None,  "7"],  # 4
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14", None,   "S15",  "S16",  "S17",   None,   None,   None,  "S26",   None,   None,   None,   None,   None,   None,   "25",   "24",   None,   "23",  None],  # 5
        ["R16", "R16",   "R16", "R16",  "S27",  "R16",  "R16",  "S28",  "R16",  "R16",  "R16",     "R16",   None,   "R16",  "R16",  "R16", "R16",  "R16",   "R16",  None,   "R16",   "R16", None,   None,   None,   None,   None,   None,   None,  None,  None],  # 6
        ["R11",  "R11", "R11", "R11",   None,   None,   None,   None,   "R11",   "R11", "R11",     "R11",   None,   "R11",   "R11",  "R11",  "R11", "R11",  "R11",  None,   "R11",   "R11", None,   None,   None,   None,   None,   None,   None,  None,  None],  # 7
        ["R12", "R12",  "R12", "R12",   None,   "S29",  "S30",  None,   "R12",  "R12",  "R12",     "R12",   None,   "R12", "R12",  "R12",   "R12",  "R12",  "R12",  None,   "R12",  "R12",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 8
        [None,  None,   None,   None,   None,   None,   None,   None,   "R24",  None,  "R24",      "R24",   None,   "R24",  "R24", "R24",   None,   None,   None,  "R24",   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 9
        [None,  None,   None,   None,   None,   None,   None,   None,   "R25",  None,  "R25",      "R25",   None,   "R25", "R25",  "R25",   None,   None,   None,  "R25",   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 10
        [None,  None,   None,   None,   None,   None,   None,   None,   "R26",   None,   "R26",    "R26",   None,   "R26", "R26",  "R26",   None,   None,   None,  "R26",   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 11
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,   "S13",    "S14",   None,   "S15", "S16",  "S17",   "S9",   "S10",  "S11",  None,   "S18",   None,   None,   None,   None,   "31",   "8",   "6",   "32",  None,  "7"],  # 12
        ["R18", "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  "R18",   "R18",    "R18",   None,   "R18",  "R18",  "R18",  "R18",  "R18",  "R18",  None,   "R18",  "R18",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 13
        ["R19", "R19",  "R19",  "R19",  "R19",  "R19",  "R19",  "R19",  "R19",  "R19",   "R19",    "R19",   "S33",  "R19",  "R19",  "R19",  "R19",  "R19",   "R19",  None, "R19",   "R19",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 14
        ["R21", "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  "R21",   "R21",    "R21",   None,   "R21",  "R21",  "R21",  "R21",  "R21",  "R21",  None,  "R21",   "R21",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 15
        ["R22", "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  "R22",   "R22",    "R22",   None,   "R22",  "R22",  "R22",  "R22",  "R22",  "R22",  None,  "R22",   "R22",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 16
        [None,  None,   None,   None,   None,   None,   None,   None,   "S34",   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 17
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",     "S14",   None,   "S15", "S16",   "S17",   "S9",   "S10",  "S11",  None,  "S18",   None,   None,   None,   None,   "35",   "8",   "6",     "32",  None,  "7"],  # 18
        [None,  "R2",   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "R2",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 19
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14",  None,   "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "36",   "37",   None,  None, None],  # 20
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14",  None,   "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "38",   "37",   None,  None, None],  # 21
        [None,  "S39",   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 22
        ["S4",  "R5",   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",      "S14",   None,   "S15", "S16",  "S17",   "S9",   "S10",  "S11",   None, "S18",  "R5",   None,   None,   "40",   "3",     "8",    "6",     "5",  None,  "7"],  # 23
        ["R16", "R16",  "R16", "R16",   "S41",  "R16",  "R16",  "S28",  "R16",  "R16",  "R16",      "R16",   None,   "R16",  "R16",  "R16",  "R16",  "R16",  "R16",  None,  "R16"   "R16",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 24
        ["R9",   "R9",  "R9",   "R9",   None,   "S29",  "S30",  None,    "R9",  "R9",  "R9",         "R9",   "R9",    "R9",   "R9",   "R9",   "R9",  "R9",   "R9",   None,  "R9",    "R9",  None,   None,   None,   None,   None,   None,   None,  None,  None],  # 25
        [None,  None,   None,   None,   None,   None,   None,   None,   "S42",   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 26
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,  "S13",     "S14",   None,   "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "43",   "37",   None,  None,  None],  # 27
        ["R15", "R15",  "R15",  "R15",  None,   "R15",  "R15",  None,   "R15",  "R15",  "R15",      "R15",   None,  "R15",  "R15",  "R15",   "R15",  "R15", "R15",   None,  "R15",  "R15",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 28
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",      "S14",   None,  "S15",  "S16",  "S17",  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "44",   None,  None,  None],  # 29
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",  None,   "S13",      "S14",   None,  "S15",  "S16",  "S17",  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "45",   None,  None,  None],  # 30
        [None,  None,   "S20",  "S21",   None,   None,   None,   None,   None,   "S46",   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 31
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,   "S13",     "S14",   None,  "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "25",   "24",   None,  None,  None],  # 32
        [None,  None,   None,   None,   None,   None,   None,   None,   None,   None,   None,       "S47",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 33
        [None,  None,   None,   None,   None,   None,   None,   None,   "S12",   None,   "S13",     "S14",   None,  "S15",  "S16",  "S17",   "S9",  "S10",  "S11",   None,  "S18",   None,   None,   None,   None,   "48",   "8",   "6",   "32",  None,  "7"],  # 34
        ["R28", "R28",  None,   None,   None,   None,   None,   None,   "R28",   "R28",   "R28",    "R28",   None,  "R28",  "R28",  "R28",  "R28",  "R28",  "R28",   None,  "R28",  "R28",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 35
        ["R6",  "R6",   "R6",   "R6",   None,  "S29",  "S30",   None,   "R6",   "R6",   "R6",       "R6",   None,   "R6",   "R6",   "R6",   "R6",   "R6",   "R6",   None,   "R6",   "R6",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 36
        ["R16", "R16",  "R16",  "R16",   None,  "R16",  "R16",  "S28",  "R16",  "R16",  "R16",      "R16",   None,  "R16",  "R16",  "R16",  "R16",  "R16",  "R16",   None,  "R16",  "R16",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 37
        ["R7",  "R7",   "R7",   "R7",   None,  "S29",  "S30",   None,   "R7",   "R7",   "R7",       "R7",   None,   "R7",   "R7",   "R7",   "R7",   "R7",   "R7",   None,   "R7",   "R7",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 38
        [None,  "R3",   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "R3",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 39
        [None,  "R4",   None,   None,   None,   None,   None,   None,   None,   None,   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "R4",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 40
        [None,  None,   None,   None,   None,   None,   None,   None,  "S12",   None,  "S13",      "S14",   None,  "S15",  "S16",  "S17",   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   "49",   "37",   None,  None,  None],  # 41
        [None,  None,   None,   None,   None,   None,   None,   None,   None,  "S50",   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 42
        ["R10", "R10", "R10",  "R10",   None,  "S29",  "S30",   None,  "R10",  "R10",  "R10",      "R10",   None,  "R10",  "R10",  "R10",  "R10",  "R10",  "R10",   None,  "R10",  "R10",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 43
        ["R13", "R13", "R13",  "R13",   None,  "R13",  "R13",   None,  "R13",  "R13",  "R13",      "R13",   None,  "R13",  "R13",  "R13",  "R13",  "R13",  "R13",   None,  "R13",  "R13",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 44
        ["R14", "R14", "R14",  "R14",   None,  "R14",  "R14",   None,  "R14",  "R14",  "R14",      "R14",   None,  "R14",  "R14",  "R14",  "R14",  "R14",  "R14",   None,  "R14",  "R14",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 45
        ["R17", "R17", "R17",  "R17",  "R17",  "R17",  "R17",  "R17",  "R17",  "R17",  "R17",      "R17",   None,  "R17",  "R17",  "R17",  "R17",  "R17",  "R17",   None,  "R17",  "R17",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 46
        ["R20", "R20", "R20",  "R20",  "R20",  "R20",  "R20",  "R20",  "R20",  "R20",  "R20",      "R20",   None,  "R20",  "R20",  "R20",  "R20",  "R20",  "R20",   None,  "R20",  "R20",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 47
        [None,  None,  "S20",  "S21",   None,   None,   None,   None,   None,  "S51",   None,       None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 48
        ["R8",  "R8",   "R8",   "R8",   None,  "S29",  "S30",   None,   "R8",   "R8",   "R8",       "R8",   None,   "R8",   "R8",   "R8",   "R8",   "R8",   "R8",   None,   "R8",   "R8",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 49
        ["R27", "R27",   None,   None,   None,   None,   None,   None,  "R27",   None,  "R27",      "R27",   None, "R27",  "R27",  "R27",  "R27",  "R27",  "R27",   None,  "R27",  "R27",   None,   None,   None,   None,   None,   None,   None,  None,  None],  # 50
        ["R23", "R23",  "R23",  "R23",  "R23",  "R23",  "R23",  "R23",  "R23",  "R23",  "R23",      "R23",   None,  "R23",  "R23",  "R23",  "R23",  "R23",  "R23",   None,  "R23",  "R23",   None,   None,   None,   None,   None,   None,   None,  None,  None]   # 51
]

# Production Rules Done. Passing tokens for both test cases
# E' -> P
# P -> B
# B -> E B
# B -> { B }
# B -> A M B
# B -> ''
# E -> E + T
# E -> E - T
# E -> A F = T
# E -> A T
# E -> F = T
# E -> R
# E -> T
# T -> T * F
# T -> T / F
# T -> F ;
# T -> F
# F -> ( E )
# F -> id
# F -> num
# F -> num . num
# F -> true
# F -> false
# F -> printf ( E )
# A -> int
# A -> float
# A -> bool
# M -> main ( )
# R -> return E

# Use this website
#   https://jsmachines.sourceforge.net/machines/slr.html 

# Both tests cases parsing correctly
# Tokens from test case 1:
# int main ( ) { int id = num ; float id = num . num ; bool id = true ; id = id + num ; id = id + id ; return num ; }

# Tokens from test case 2:
# int main ( ) { int id ; float id = num ; id = num + id ; func ( id ) ; return num . num ; }

productions = {
    0: ("E'", ["P"]),
    1: ("P", ["B"]),
    2: ("B", ["E", "B"]),
    3: ("B", ["leftBrace", "B", "rightBrace"]),
    4: ("B", ["A", "M", "B"]),
    5: ("B", [""]),
    6: ("E", ["E", "plus", "T"]),
    7: ("E", ["E", "minus", "T"]),
    8: ("E", ["A", "F", "assignment", "T"]),
    9: ("E", ["A", "T"]),
    10: ("E", ["F", "assignment", "T"]),
    11: ("E", ["R"]),
    12: ("E", ["T"]),
    13: ("T", ["T", "multiply", "F"]),
    14: ("T", ["T", "divide", "F"]),
    15: ("T", ["F", "semicolon"]),
    16: ("T", ["F"]),
    17: ("F", ["leftParen", "E", "rightParen"]),
    18: ("F", ["identifier"]),
    19: ("F", ["integer"]),
    20: ("F", ["integer", ".", "integer"]),
    21: ("F", ["true"]),
    22: ("F", ["false"]),
    23: ("F", ["printf", "leftParen", "E", "rightParen"]),
    24: ("A", ["int"]),
    25: ("A", ["float"]),
    26: ("A", ["bool"]),
    27: ("M", ["main", "leftParen", "rightParen"]),
    28: ("R", ["return", "E"])
}
