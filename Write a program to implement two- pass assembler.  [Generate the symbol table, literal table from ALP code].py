# Code
SYMBOL_TABLE = {}
LITERAL_TABLE = {}

# First pass: generate symbol table and literal table
def first_pass(code):
    location_counter = 0
    tokens = code.split()
    for token in tokens:
        if token.endswith(':'):
            symbol = token[:-1]
            SYMBOL_TABLE[symbol] = location_counter
        elif token.startswith('='):
            literal = token
            if literal not in LITERAL_TABLE:
                LITERAL_TABLE[literal] = location_counter
            location_counter += 1
        else:
            location_counter += 1

# Second pass: generate object code
def second_pass(code):
    object_code = []
    tokens = code.split()
    for token in tokens:
        if token.endswith(':'):
            continue
        elif token.startswith('='):
            literal = token
            address = LITERAL_TABLE[literal]
            object_code.append(address)
        elif token in SYMBOL_TABLE:
            address = SYMBOL_TABLE[token]
            object_code.append(address)
        else:
            object_code.append(token)
    return ' '.join(str(code) for code in object_code)

# Example usage
code = '''
START 1000
LOOP LDA =FOO
    ADD BAR
    STA RESULT
    JNZ LOOP
    HLT
FOO DB 10
BAR DB 20
RESULT DS 1
END
'''
first_pass(code)
object_code = second_pass(code)
print(object_code)


# Output:
START 1000 LOOP LDA 4 ADD BAR STA RESULT JNZ LOOP HLT FOO DB 10 BAR DB 20 RESULT DS 1 END

# Note :
  This program implements a two-pass assembler for a simple assembly language. The first pass generates the symbol table and literal table by iterating over the code and keeping track of the current location counter. The symbol table is a dictionary that maps symbols to memory addresses, and the literal table is a dictionary that maps literals to memory addresses. The second pass generates the object code by iterating over the code again and replacing symbols and literals with their corresponding memory addresses. The object code is returned as a string.

To use the program, simply call first_pass() with the code to generate the symbol table and literal table, and then call second_pass() with the code to generate the object code. The example code provided demonstrates how the program can be used to assemble a simple program, where each instruction consists of an opcode followed by one or more operands, and where symbols are used to represent memory addresses.
