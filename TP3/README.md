# TPC 3
## Construir um analisador léxico 
### Enunciado 
Contruir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

```sparql
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
  ?s a dbo:MusicalArtist.
  ?s foaf:name "Chuck Berry"@en .
  ?w dbo:artist ?s.
  ?w foaf:name ?nome.
  ?w dbo:abstract ?desc
} LIMIT 1000
```
### Resolução
Desenvolvi o programa [tokenizer.py](tokenizer.py) que contém a função tokenize() percorre o texto de entrada linha a linha e, usando expressões regulares, reconhece e classifica diferentes elementos da linguagem — como palavras-chave, variáveis, números, operadores e símbolos — transformando o texto numa sequência estruturada de tokens que representam os componentes léxicos necessários para etapas posteriores de análise sintática.

Corri o programa [tokenizer.py](tokenizer.py) com o teste acima [sqarl_test.txt](sqarl_test.txt) e obtive o seguinte resultado:

```
('KEYWORD', 'select', 1, (0, 6))
('VAR', '?nome', 1, (7, 12))
('VAR', '?desc', 1, (13, 18))
('KEYWORD', 'where', 1, (19, 24))
('CA', '{', 1, (25, 26))
('NEWLINE', '\n', 1, (26, 27))
('VAR', '?s', 2, (4, 6))
('KEYWORD', 'a', 2, (7, 8))
('PREFIX', 'dbo:MusicalArtist', 2, (9, 26))
('ENDLINE', '.', 2, (26, 27))
('NEWLINE', '\n', 2, (27, 28))
('VAR', '?s', 3, (4, 6))
('PREFIX', 'foaf:name', 3, (7, 16))
('STRING', '"Chuck Berry"@en', 3, (17, 33))
('ENDLINE', '.', 3, (34, 35))
('NEWLINE', '\n', 3, (35, 36))
('VAR', '?w', 4, (4, 6))
('PREFIX', 'dbo:artist', 4, (7, 17))
('VAR', '?s', 4, (18, 20))
('ENDLINE', '.', 4, (20, 21))
('NEWLINE', '\n', 4, (21, 22))
('VAR', '?w', 5, (4, 6))
('PREFIX', 'foaf:name', 5, (7, 16))
('VAR', '?nome', 5, (17, 22))
('ENDLINE', '.', 5, (22, 23))
('NEWLINE', '\n', 5, (23, 24))
('VAR', '?w', 6, (4, 6))
('PREFIX', 'dbo:abstract', 6, (7, 19))
('VAR', '?desc', 6, (20, 25))
('NEWLINE', '\n', 6, (25, 26))
('CF', '}', 7, (0, 1))
('KEYWORD', 'LIMIT', 7, (2, 7))
('INT', '1000', 7, (8, 12))
```








