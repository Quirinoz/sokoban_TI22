class Sokoban:
  mapa = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,4,1,1,2,1,1,4,1,0,1,4,1,1,2,1,1,4,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
  ]
  #mapa donde uno puede representarse y poder moverse

  # W - Arriba
  # A - Izquierda
  # S - Abajo
  # D - Derecha

  # 0 = personaje
  # 1 = espacio
  # 2 = caja
  # 3 = pared
  # 4 = meta
  # 5 = personaje_meta
  # 6 = caja_meta

  personaje_fila = 2 #fila en la que se encuentra el personaje
  personaje_columna = 9 #columna en la que se encuentra el personaje 
#variables que ubican la posición del personaje en el mapa
  def imprimirMapa(self):# Imprime el mapa
    for fila in self.mapa:# Recorre la fila por el mapa
      print(fila)# Imprime la fila

  # 0 (personaje, espacio)
  def moverDerecha(self):
    if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 1 (personaje, meta)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 2 (personaje, caja, espacio)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 3 (personaje, caja, meta)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 4 (personaje, caja_meta, espacio)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 5 (personaje, caja_meta, meta)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 6 (personaje_meta, espacio)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 7 (personaje_meta, meta)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 8 (personaje_meta, caja, espacio)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 9 (personaje_meta, caja, meta)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 10 (personaje_meta, caja_meta, espacio)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

  # 11 (personaje_meta, caja_meta_, meta)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6 and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

#############################################################################

  # 0 (personaje, espacio)
  def moverIzquierda(self):
    if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1:
        self.mapa[self.personaje_fila][self.personaje_columna] = 1
        self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
        self.personaje_columna -= 1 #solo es la unidad actualizada del movimiento

  # 1 (personaje, meta)
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
      self.personaje_columna -= 1

##################################################################################

  def jugar(self):
    while True:
      self.imprimirMapa()
      movimiento = input("Moverse")
      if movimiento == "d":
        self.moverDerecha()
      elif movimiento == "a":
        self.moverIzquierda()
      elif movimiento == "w":
        self.moverArriba()
      elif movimiento == "s":
        self.moverAbajo()
        
juego = Sokoban()
juego.jugar()

