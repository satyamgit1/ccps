# Code
BASE_TABLE = {}
SYMBOL_TABLE = {}

# First pass: generate base table and symbol table
def first_pass(code):
    location_counter = 0
    tokens = code.split()
    for token in tokens:
        if token.startswith('B='):
            base = token.split('=')[1]
            BASE_TABLE[base] = location_counter
        elif token.endswith(':'):
            symbol = token[:-1]
            SYMBOL_TABLE[symbol] = location_counter
        else:
            location_counter += 1

# Second pass: generate object code and update location counter
def second_pass(code):
    object_code = []
    location_counter = 0
    tokens = code.split()
    for token in tokens:
        if token.startswith('B=') or token.endswith(':'):
            continue
        elif token.startswith('='):
            object_code.append(token)
            location_counter += 1
        elif token in SYMBOL_TABLE:
            address = SYMBOL_TABLE[token]
            object_code.append(str(address))
            location_counter += 1
        elif token.startswith('#'):
            object_code.append(token)
        elif token in BASE_TABLE:
            address = BASE_TABLE[token]
            object_code.append(str(address))
        else:
            object_code.append(token)
            location_counter += 1
    return ' '.join(object_code)

# Example usage
code = '''
B=1000
START LDA #FOO
      ADD #BAR
      STA =RESULT
      JNZ LOOP
      HLT
LOOP  LDA =FOO
      ADD #ONE
      STA =FOO
      JNZ LOOP
      HLT
FOO   DC 10
BAR   DC 20
ONE   DC 1
RESULT DS 1
END
'''
first_pass(code)
object_code = second_pass(code)
print(object_code)


# Output
START LDA #FOO ADD #BAR STA =RESULT JNZ LOOP HLT LOOP LDA =FOO ADD #ONE STA =FOO JNZ LOOP HLT FOO DC 10 BAR DC 20 ONE DC 1 RESULT DS 1 END

# Note : 
This program implements a two-pass assembler for a simple assembly language. The first pass generates the base table and symbol table by iterating over the code and keeping track of the current location counter. The base table is a dictionary that maps base names to base addresses, and the symbol table is a dictionary that maps symbols to memory addresses. The second pass generates the object code by iterating over the code again and replacing symbols and bases with their corresponding memory addresses. The location counter is also updated as the object code is generated. The object code is returned as a string.

To use the program, simply call first_pass() with the code to generate the base table and symbol table, and then call second_pass() with the code to generate the object code and update the location counter. The example code provided demonstrates how the program can be used to assemble a simple program, where each instruction consists of an opcode followed by one or more operands, and where bases and symbols are used to represent memory addresses.
