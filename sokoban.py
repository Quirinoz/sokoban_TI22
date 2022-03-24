class Sokoban:
  mapa = [
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,1,1,0,4,4,1,2,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,1,1,1,1,1,1,1,1,1,1,1,1,1,3],
    [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
  ]
  #mapa donde uno puede representarse y poder moverse
  personaje_fila = 3 #fila en la que se encuentra el personaje
  personaje_columna = 3 #columna en la que se encuentra el personaje 
#variables que ubican la posición del personaje en el mapa
  def imprimirMapa(self):# Imprime el mapa
    for fila in self.mapa:# Recorre la fila por el mapa
      print(fila)# Imprime la fila

  def moverDerecha(self):
    if self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento
      
    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

    elif self.mapa[self.personaje_fila][self.personaje_columna] == 5 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 4
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

    elif self.mapa[self.personaje_fila][self.personaje_columna] == 0 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2 and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1:
      self.mapa[self.personaje_fila][self.personaje_columna] = 1
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
      self.mapa[self.personaje_fila][self.personaje_columna + 1] = 2
      self.personaje_columna += 1 #solo es la unidad actualizada del movimiento

    
  def jugar(self):# Controla el flujo del juego
    while True:# Si es verdadera
      self.imprimirMapa()
      movimiento = input("Moverse")
      if movimiento == "d":
        self.moverDerecha()

juego = Sokoban()
juego.jugar()

