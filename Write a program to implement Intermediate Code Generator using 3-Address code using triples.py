# Code
class IntermediateCodeGenerator:
    def __init__(self, code):
        self.code = code
        self.triples = []

    def generate(self):
        lines = self.code.split('\n')
        for i, line in enumerate(lines):
            if '=' in line:
                left, right = line.split('=')
                op = 'ASSIGN'
                arg1 = right.strip()
                arg2 = ''
                result = left.strip()
                self.triples.append((op, arg1, arg2, result))
            elif '+' in line:
                left, right = line.split('+')
                op = 'ADD'
                arg1 = left.strip()
                arg2 = right.strip()
                result = 't' + str(i+1)
                self.triples.append((op, arg1, arg2, result))
            elif '-' in line:
                left, right = line.split('-')
                op = 'SUBTRACT'
                arg1 = left.strip()
                arg2 = right.strip()
                result = 't' + str(i+1)
                self.triples.append((op, arg1, arg2, result))
        return self.triples

# Example usage
code = '''
x = 5;
y = 3 + x;
z = y - 2;
'''

generator = IntermediateCodeGenerator(code)
triples = generator.generate()
for triple in triples:
    print(triple)

# Output
('ASSIGN', '5;', '', 'x')
('ASSIGN', '3 + x;', '', 'y')
('ASSIGN', 'y - 2;', '', 'z')

# Note:
This program implements an intermediate code generator using 3-address code using triples. The IntermediateCodeGenerator class has a generate() method which generates the intermediate code in the form of triples.

The program takes an input code as a string and creates an instance of the IntermediateCodeGenerator class. It then calls the generate() method to generate the intermediate code using 3-address code using triples and stores the result in triples.

Finally, the program prints out the generated triples. The example code provided demonstrates how the program can be used to generate the intermediate code for a simple code snippet.
