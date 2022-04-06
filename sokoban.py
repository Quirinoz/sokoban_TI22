class Sokoban:
    mapa = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [3, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 3],
        [3, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 3],
        [3, 1, 1, 4, 4, 1, 1, 1, 1, 1, 1, 1, 3],
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3],
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    ]
    # mapa donde uno puede representarse y poder moverse

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

    personaje_fila = 1  # fila en la que se encuentra el personaje

    personaje_columna = 1  # columna en la que se encuentra el personaje
    # variables que ubican la posición del personaje en el mapa

    def imprimirMapa(self):  # Imprime el mapa
        for fila in self.mapa:  # Recorre la fila por el mapa
            print(fila)  # Imprime la fila

    
    def moverDerecha(self):
        # 0 (personaje, espacio)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 0 (personaje, espacio) derecha")

        # 1 (personaje, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 1 (personaje, meta) derecha")

        # 2 (personaje, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 2 (personaje, caja, espacio) derecha")

        # 3 (personaje, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 3 (personaje, caja, meta) derecha")

        # 4 (personaje, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 4 (personaje, caja_meta, espacio) derecha")

        # 5 (personaje, caja_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 5 (personaje, caja_meta, meta) derecha")

        # 6 (personaje_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 6 (personaje_meta, espacio) derecha")

        # 7 (personaje_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 7 (personaje_meta, meta) derecha")

        # 8 (personaje_meta, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 8 (personaje_meta, caja, espacio) derecha")

        # 9 (personaje_meta, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 9 (personaje_meta, caja, meta) derecha")

        # 10 (personaje_meta, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 2
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 10 (personaje_meta, caja_meta, espacio) derecha")

        # 11 (personaje_meta, caja_meta_, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna + 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna + 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna + 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna + 2] = 6
            self.personaje_columna += 1  # solo es la unidad actualizada del movimiento
            print("# 11 (personaje_meta, caja_meta_, meta) derecha")

    #############################################################################

    # 0 (personaje, espacio)
    def moverIzquierda(self):
        # 0 (personaje, espacio)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1  # solo es la unidad actualizada del movimiento
            print("# 0 (personaje, espacio) izquierda")

        # 1 (personaje, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
            print("# 1 (personaje, meta) izquierda")

        # 2 (personaje, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 1
            print("# 2 (personaje, caja, espacio) izquierda")

        # 3 (personaje, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
            print("# 3 (personaje, caja, meta) izquierda")

        # 4 (personaje, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.persoanje_columna -= 1
            print("# 4 (personaje, caja_meta, espacio) izquierda")

        # 5 (personaje, caja_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
            print("# 5 (personaje, caja_meta, meta) izquierda")

        # 6 (personaje_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.personaje_columna -= 1
            print("# 6 (personaje_meta, espacio) izquierda")

        # 7 (personaje_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.personaje_columna -= 1
            print("# 7 (personaje_meta, meta) izquierda")

        # 8 (personaje_meta, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 1
            print("# 8 (personaje_meta, caja, espacio) izquierda")

        # 9 (persoanje_meta, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 2
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 0
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
            print("# 9 (persoanje_meta, caja, meta) izquierda")

        # 10 (personaje_meta, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 2
            self.personaje_columna -= 1
            print("# 10 (personaje_meta, caja_meta, espacio) izquierda")

        # 11 (personaje_meta, caja_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila][self.personaje_columna - 1] == 6
            and self.mapa[self.personaje_fila][self.personaje_columna - 2] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila][self.personaje_columna - 1] = 5
            self.mapa[self.personaje_fila][self.personaje_columna - 2] = 6
            self.personaje_columna -= 1
            print("# 11 (personaje_meta, caja_meta, meta) izquierda")

    ##################################################################################

    
    def moverArriba(self):
        # 0 (personaje, espacio)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.personaje_fila -= 1
            print("# 0 (personaje, espacio) arriba")

        # 1 (personaje, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila -= 1
            print("# 1 (personaje, meta) arriba")

        # 2 (personaje, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2
            self.personaje_fila -= 1
            print("# 2 (personaje, caja, espacio) arriba")

        # 3 (personaje, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_columna - 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_columna - 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -= 1
            print("# 3 (personaje, caja, meta) arriba")

        # 4 (personaje, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2
            self.personaje_fila -= 1
            print("# 4 (personaje, caja_meta, espacio) arriba")

        # 5 (personaje, caja_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -= 1
            print("# 5 (personaje, caja_meta, meta) arriba")

        # 6 (personaje_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.personaje_fila -= 1
            print("# 6 (personaje_meta, espacio) arriba")

        # 7 (personaje_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.personaje_fila -= 1
            print("# 7 (personaje_meta, meta) arriba")

        # 8 (personaje_meta, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2
            self.personaje_fila -= 1
            print("# 8 (personaje_meta, caja, espacio) arriba")

        # 9 (personaje_meta, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -= 1
            print("# 9 (personaje_meta, caja, meta) arriba")

        # 10 (personaje_meta, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 2
            self.personaje_fila -= 1
            print("# 10 (personaje_meta, caja_meta, espacio) arriba")

        # 11 (personaje_meta, caja_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila - 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila - 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila - 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila - 2][self.personaje_columna] = 6
            self.personaje_fila -= 1
            print("# 11 (personaje_meta, caja_meta, meta) arriba")

    ############################################################################
    
    def moverAbajo(self):
        # 0 (personaje, espacio)
        if (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila += 1
            print("# 0 (personaje, espacio) abajo")

        # 1 (personaje, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila += 1
            print("# 1 (personaje, meta) abajo")

        # 2 (personaje, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila += 1
            print("# 2 (personaje, caja, espacio) abajo")

        # 3 (personaje, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila += 1
            print("# 3 (personaje, caja, meta) abajo")

        # 4 (personaje, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila += 1
            print("# 4 (personaje, caja_meta, espacio) abajo")

        # 5 (personaje, caja_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 0
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 1
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila += 1
            print("# 5 (personaje, caja_meta, meta) abajo")

        # 6 (personaje_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.personaje_fila += 1
            print("# 6 (personaje_meta, espacio) abajo")

        # 7 (personaje_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.personaje_fila += 1
            print("# 7 (personaje_meta, meta) abajo")

        # 8 (personaje_meta, caja, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.persoanje_fila += 1
            print("# 8 (personaje_meta, caja, espacio) abajo")

        # 9 (personaje_meta, caja, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 2
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 0
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila += 1
            print("# 9 (personaje_meta, caja, meta) abajo")

        # 10 (personaje_meta, caja_meta, espacio)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 1
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 2
            self.personaje_fila += 1
            print("# 10 (personaje_meta, caja_meta, espacio) abajo")

        # 11 (personaje_meta, caja_meta, meta)
        elif (
            self.mapa[self.personaje_fila][self.personaje_columna] == 5
            and self.mapa[self.personaje_fila + 1][self.personaje_columna] == 6
            and self.mapa[self.personaje_fila + 2][self.personaje_columna] == 4
        ):
            self.mapa[self.personaje_fila][self.personaje_columna] = 4
            self.mapa[self.personaje_fila + 1][self.personaje_columna] = 5
            self.mapa[self.personaje_fila + 2][self.personaje_columna] = 6
            self.personaje_fila += 1
            print("# 11 (personaje_meta, caja_meta, meta) abajo")

    ######################################################################################
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
