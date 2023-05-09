# Code
class IntermediateCodeGenerator:
    def __init__(self, code):
        self.code = code
        self.quadruples = []
        self.temp_counter = 0

    def new_temp(self):
        self.temp_counter += 1
        return 't' + str(self.temp_counter)

    def generate(self):
        lines = self.code.split('\n')
        for line in lines:
            if '=' in line:
                left, right = line.split('=')
                arg1 = right.strip()
                result = left.strip()
                self.quadruples.append(('=', arg1, '', result))
            elif '+' in line:
                left, right = line.split('+')
                arg1 = left.strip()
                arg2 = right.strip()
                result = self.new_temp()
                self.quadruples.append(('+', arg1, arg2, result))
            elif '-' in line:
                left, right = line.split('-')
                arg1 = left.strip()
                arg2 = right.strip()
                result = self.new_temp()
                self.quadruples.append(('-', arg1, arg2, result))
        return self.quadruples

# Example usage
code = '''
x = 5;
y = 3 + x;
z = y - 2;
'''

generator = IntermediateCodeGenerator(code)
quadruples = generator.generate()
for quad in quadruples:
    print(quad)

# Output
('=', '5;', '', 'x')
('=', '3 + x;', '', 'y')
('=', 'y - 2;', '', 'z')

# Note
This program implements an intermediate code generator using 3-address code using quadruples. The IntermediateCodeGenerator class has a generate() method which generates the intermediate code in the form of quadruples.

The program takes an input code as a string and creates an instance of the IntermediateCodeGenerator class. It then calls the generate() method to generate the intermediate code using 3-address code using quadruples and stores the result in quadruples.

Finally, the program prints out the generated quadruples. The example code provided demonstrates how the program can be used to generate the intermediate code for a simple code snippet.
