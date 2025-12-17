import re
patron = re.compile('a[3-5]+') # coincide con una letra, seguida de al menos 1 dígito entre 3 y 5
cadena = 'a44453'
print(patron.match(cadena)) # <re.Match object; span=(0, 6), match='a44453'>
print(patron.search(cadena)) # <re.Match object; span=(0, 6), match='a44453'>
cadena = 'ba3455' # la coincidencia no está al principio!
print(patron.search(cadena)) # <re.Match object; span=(1, 6), match='a3455'>
print(patron.match(cadena)) # None

print(isinstance())