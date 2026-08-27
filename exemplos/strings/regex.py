#/hello/:
#\d: qualquer número de 0 a 9
#\w: letra, número ou _
#.: qualquer caractere
#+: uma ou mais ocorrência do padrão anterior
#*: zero ou mais ocorrências
#?: entre 0 e 1 ocorrência

import re

codigo_cinco_digitos = '12345'
codigo_nueve_digitos = '12345-6789'
numero_telefono = '123-456-7890'

regex_cinco_digitos = r'\d{5}'

print(re.search(regex_cinco_digitos, codigo_cinco_digitos))
print(re.search(regex_cinco_digitos, codigo_nueve_digitos))
print(re.search(regex_cinco_digitos, numero_telefono))