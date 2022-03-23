class Sokoban:
  mapa = [
    [3,3,3,3,3,3,3],
    [3,1,1,1,1,1,3],
    [3,1,1,1,1,1,3],
    [3,1,1,0,1,1,3],
    [3,1,1,1,1,1,3],
    [3,1,1,1,1,1,3],
    [3,3,3,3,3,3,3]
  ]
  #mapa donde uno puede representarse y poder moverse
  personaje_fila = 3 #fila en la que se encuentra el personaje
  personaje_columna = 3 #columna en la que se encuentra el personaje 
#variables que ubican la posición del personaje en el mapa
  def imprimirMapa(self):
    for fila in self.mapa:
      print(fila)
      
  def jugar(self):
    while True:
      self.imprimirMapa()
      movimiento = input("Moverse")

juego = Sokoban()
juego.jugar()

