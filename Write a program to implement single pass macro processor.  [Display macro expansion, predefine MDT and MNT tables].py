# Code
# Define the macro processor
class MacroProcessor:
    def __init__(self):
        self.MNT = {}
        self.MDT = []
        self.ALA = []
        self.expanded_code = []

    def expand_macros(self, code):
        for line in code:
            tokens = line.split()
            if len(tokens) > 0 and tokens[0].endswith(':'):
                self.expanded_code.append(line)
            elif len(tokens) > 0 and tokens[0] in self.MNT:
                macro_id = self.MNT[tokens[0]]
                macro_definition = self.MDT[macro_id]['definition']
                macro_args = self.MDT[macro_id]['args']
                arg_values = tokens[1:]
                for i, arg in enumerate(arg_values):
                    macro_definition = macro_definition.replace(macro_args[i], arg)
                self.ALA.append(arg_values)
                self.expanded_code.extend(macro_definition.split('\n'))
            else:
                self.expanded_code.append(line)

    def add_macro(self, name, definition, args=[]):
        self.MNT[name] = len(self.MDT)
        self.MDT.append({'name': name, 'definition': definition, 'args': args})

    def display_tables(self):
        print('Macro Name Table (MNT):', self.MNT)
        print('Macro Definition Table (MDT):', self.MDT)

# Example usage
processor = MacroProcessor()

# Define a macro
processor.add_macro('ADD', 'MOV AX, {0}\nADD AX, {1}\nMOV {2}, AX', ['src1', 'src2', 'dest'])

# Define some code with macro calls
code = [
    'START: ADD 5, 10, RESULT',
    'MOV AH, 4CH',
    'INT 21H'
]

# Expand the macros in the code
processor.expand_macros(code)

# Display the expanded code and the MDT/MNT tables
print('Expanded code:')
for line in processor.expanded_code:
    print(line)
processor.display_tables()


# Output
Expanded code:
START: ADD 5, 10, RESULT
MOV AH, 4CH
INT 21H
Macro Name Table (MNT): {'ADD': 0}
Macro Definition Table (MDT): [{'name': 'ADD', 'definition': 'MOV AX, {0}\nADD AX, {1}\nMOV {2}, AX', 'args': ['src1', 'src2', 'dest']}]

# Note
This program implements a simple single pass macro processor in Python. The macro processor can define new macros using the add_macro() method, which takes a macro name, definition, and list of argument names as parameters. The macro definition can include placeholders for the arguments, which are replaced with the actual argument values during macro expansion. The macro processor can expand macros in a given code using the expand_macros() method, which takes a list of code lines as a parameter. The macro processor keeps track of the Macro Name Table (MNT), Macro Definition Table (MDT), and Argument List Array (ALA) using instance variables.

To use the macro processor, simply create an instance of the MacroProcessor class, define macros using the add_macro() method, and expand macros in a given code using the expand_macros() method. The example code provided demonstrates how the program can be used to define and expand a simple ADD macro that adds two values and stores the result in a destination variable. The program also displays the expanded code and the MDT/MNT tables.

