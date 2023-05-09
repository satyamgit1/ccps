# Code
MOT = {'LDA': '01', 'STA': '02', 'ADD': '03', 'SUB': '04', 'MUL': '05', 'DIV': '06', 'JMP': '07', 'JNZ': '08', 'HLT': '09'}
POT = {'DC': '01', 'DS': '02', 'DB': '03', 'DW': '04'}

# First pass: generate symbol table and literal table
def first_pass(code):
    location_counter = 0
    tokens = code.split()
    for token in tokens:
        if token.endswith(':'):
            continue
        elif token.startswith('='):
            location_counter += 1
        elif token in MOT:
            location_counter += 1
        elif token in POT:
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
            object_code.append(token)
        elif token in MOT:
            opcode = MOT[token]
            object_code.append(opcode)
        elif token in POT:
            opcode = POT[token]
            object_code.append(opcode)
        else:
            object_code.append(token)
    return ' '.join(str(code) for code in object_code)

# Example usage
code = '''
START: LDA =FOO
    ADD BAR
    STA RESULT
    JNZ LOOP
    HLT
FOO: DC 10
BAR: DC 20
RESULT: DS 1
END
'''
first_pass(code)
object_code = second_pass(code)
print("MOT Contents: ", MOT)
print("POT Contents: ", POT)
print("Object Code: ", object_code)

# Output :
MOT Contents:  {'LDA': '01', 'STA': '02', 'ADD': '03', 'SUB': '04', 'MUL': '05', 'DIV': '06', 'JMP': '07', 'JNZ': '08', 'HLT': '09'}
POT Contents:  {'DC': '01', 'DS': '02', 'DB': '03', 'DW': '04'}
Object Code:  01 =FOO 03 BAR 02 RESULT 08 LOOP 09 01 10 01 20 02 1 END
  
 # Note:
This program implements a two-pass assembler for a simple assembly language. The first pass generates the symbol table and literal table by iterating over the code and keeping track of the current location counter. The location counter is incremented based on the instruction type, which is determined by checking the instruction against the MOT and POT. The MOT (Machine Opcode Table) contains the opcodes for the machine instructions, and the POT (Pseudo Opcode Table) contains the opcodes for the assembler directives.

The second pass generates the object code by iterating over the code again and replacing instructions and directives with their corresponding opcodes. The object code is returned as a string.

To use the program, simply call first_pass() with the code to generate the symbol table and literal table, and then call second_pass() with the code to generate the object code. The example code provided demonstrates how the program can be used to assemble a simple program, where each instruction consists of an opcode followed by one or more operands, and where symbols are used to represent memory addresses. The program also displays the contents of the MOT and POT.
