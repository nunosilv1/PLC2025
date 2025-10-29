import sys
import re

def tokenize(input_string):
    reconhecidos = []
    mo = re.finditer(r'(?P<INT>\d+)|(?P<KEYWORD>SELECT|WHERE|LIMIT|AS|INSERT|DELETE|PREFIX|FILTER|OPTIONAL|ASK|CONSTRUCT|DESCRIBE|ORDER|BY|ASC|DESC|OFFSET|DISTINCT|REDUCED|UNION|GRAPH|BIND|A)|(?P<CA>\{)|(?P<CF>\})|(?P<PA>\()|(?P<PF>\))|(?P<PREFIX>[a-z][a-zA-Z0-9_]*:[a-zA-Z0-9_]+)|(?P<DECPRFX>[a-z][a-zA-Z0-9_]*:)|(?P<STRING>"[^"]*"(?:@[a-zA-Z]+)?)|(?P<LINK><.*>)|(?P<VAR>\?[a-z][a-zA-Z0-9_]*)|(?P<COMP>>=|<=|<|>|==)|(?P<OPERATOR>\*|\+)|(?P<ENDLINE>\.$)|(?P<NEWLINE>\n)|(?P<SKIP>[ \t])|(?P<ERRO>.)', input_string, re.IGNORECASE)

    for m in mo:
        dic = m.groupdict()
        if dic['INT']:
            t = ("INT", dic['INT'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())

        elif dic['KEYWORD']:
            t = ("KEYWORD", dic['KEYWORD'], linha, m.span())

        elif dic['CA']:
            t = ("CA", dic['CA'], linha, m.span())

        elif dic['CF']:
            t = ("CF", dic['CF'], linha, m.span())

        elif dic['PA']:
            t = ("PA", dic['PA'], linha, m.span())

        elif dic['PF']:
            t = ("PF", dic['PF'], linha, m.span())

        elif dic['PREFIX']:
            t = ("PREFIX", dic['PREFIX'], linha, m.span())

        elif dic['DECPRFX']:
            t = ("DECPRFX", dic['DECPRFX'], linha, m.span())

        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())

        elif dic['LINK']:
            t = ("LINK", dic['LINK'], linha, m.span())

        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
        
        elif dic['COMP']:
            t = ("COMP", dic['COMP'], linha, m.span())

        elif dic['OPERATOR']:
            t = ("OPERATOR", dic['OPERATOR'], linha, m.span())

        elif dic['ENDLINE']:
            t = ("ENDLINE", dic['ENDLINE'], linha, m.span())

        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

linha = 1 
for line in sys.stdin:
    for tok in tokenize(line):
        print(tok)    
    linha += 1