primer_nombre = 'rigoberta'
segundo_nombre = 'menchú'
nota = 'Ganadora Premio Nobel de la Paz'

primer_nombre_cap = primer_nombre.capitalize()
segundo_nombre_cap = segundo_nombre.capitalize()
premio_ubicacion = nota.find("Premio")
premio_texto = nota[9:]

print(primer_nombre_cap)
print(segundo_nombre_cap)
print(f'Posição da palavra: {premio_ubicacion}')
print(f'Extração do texto: {premio_texto}')