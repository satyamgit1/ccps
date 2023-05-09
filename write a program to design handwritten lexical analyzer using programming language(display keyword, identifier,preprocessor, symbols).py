code
import re

# Define regular expressions for keywords, identifiers, preprocessor directives, and symbols
keywords = ['if', 'else', 'while', 'for', 'int', 'float', 'char']
identifiers = r'[a-zA-Z_]\w*'
preprocessor = r'#\w+'
symbols = r'[+\-*/=(),{};]'

# Combine the regular expressions into a single pattern
pattern = '|'.join([re.escape(keyword) for keyword in keywords] + [identifiers, preprocessor, symbols])

# Define a function to tokenize a string of code
def tokenize(code):
    tokens = []
    for match in re.finditer(pattern, code):
        token = match.group(0)
        if re.match(identifiers, token):
            tokens.append(('IDENTIFIER', token))
        elif re.match(preprocessor, token):
            tokens.append(('PREPROCESSOR', token))
        elif token in keywords:
            tokens.append(('KEYWORD', token))
        else:
            tokens.append(('SYMBOL', token))
    return tokens

# Example usage
code = 'int main() {\n  printf("Hello, world!\\n");\n  return 0;\n}'
tokens = tokenize(code)
for token in tokens:
    print(token)

    Output:
        ('IDENTIFIER', 'int')
('IDENTIFIER', 'main')
('SYMBOL', '(')
('SYMBOL', ')')
('SYMBOL', '{')
('IDENTIFIER', 'printf')
('SYMBOL', '(')
('IDENTIFIER', 'Hello')
('SYMBOL', ',')
('IDENTIFIER', 'world')
('IDENTIFIER', 'n')
('SYMBOL', ')')
('SYMBOL', ';')
('IDENTIFIER', 'return')
('SYMBOL', ';')
('SYMBOL', '}')

Note : 
    
    This program defines regular expressions for keywords, identifiers, preprocessor directives, and symbols, and combines them into a single pattern using the | operator. The tokenize() function takes a string of code, searches for matches of the pattern using re.finditer(), and categorizes each match as an identifier, preprocessor directive, keyword, or symbol based on its regular expression. The function returns a list of tuples, each containing a token type and the corresponding token value.

To use the program, simply call tokenize() with a string of code and iterate over the resulting list of tokens to display the token type and value.
