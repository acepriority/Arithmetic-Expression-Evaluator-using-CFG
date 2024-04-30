import re


def evaluate_expression(expression):
    #Context Free Grammar definition
    def parse_expression(tokens):
        term_value = parse_term(tokens)
        while tokens and tokens[0] in {'+', '-'}:
            operator = tokens.pop(0)
            term_value = eval(f"{term_value} {operator} {parse_term(tokens)}")
        return term_value

    
    def parse_term(tokens):
        factor_value = parse_factor(tokens)
        while tokens and tokens[0] in {'*', '/'}:
            operator = tokens.pop(0)
            factor_value = eval(f"{factor_value} {operator} {parse_factor(tokens)}")
        return factor_value

    
    def parse_factor(tokens):
        token = tokens.pop(0)
        if token.isdigit():
            return int(token)
        elif token == '(':
            result = parse_expression(tokens)
            tokens.pop(0)  # Consume ')'
            return result
        else:
            raise ValueError("Invalid token")

    
    # Tokenize the expression
    tokens = re.findall(r'\d+|\S', expression)
    
    # Evaluate the expression
    return parse_expression(tokens)


expression = '2+2+2+2'
result = evaluate_expression(expression)
print(result)
