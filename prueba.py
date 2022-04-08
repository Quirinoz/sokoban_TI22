# TODO LEER ARCHIVO DE TEXTO
# TODO IMPRIMIR ARCHIVO DE TEXTO
# TODO ALMACENAR ARCHIVO DE TEXTO EN UNA MATRIZ

class Archivos:

  def __init__ (self):
    pass

  def leer (self,archivo):
    file = open(archivo, 'r')
    for line in file:
      print(line)
    file.close()

objeto = Archivos()
objeto.leer("nivel.txt")