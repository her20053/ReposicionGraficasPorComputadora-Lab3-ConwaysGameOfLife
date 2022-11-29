import pygame
import sys
import math
from   copy    import deepcopy
from   random  import randint

def Lab3ConwaysGameOfLife():
    resolucionPantalla = int(sys.argv[1]), int(sys.argv[2])
    numero = randint(int(sys.argv[3]), int(sys.argv[3]) + 5)
    def vcell(ea, x, y):
        c = 0
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if ea[j][i]:
                    c += 1
        if ea[y][x]:
            c -= 1
            if c == 2 or c == 3:
                return 1
            return 0
        else:
            if c == 3:
                return 1
            return 0
    w, h = math.floor(int(sys.argv[1])/10), math.floor(int(sys.argv[2])/10)
    pygame.init()
    canvas = pygame.display.set_mode(resolucionPantalla)
    pygame.display.set_caption('Lab 3: Conway’s Game Of Life')
    siguienteEstado = [[0 for i in range(w)]for j in range(h)]
    estadoActual = [[1 if not (i*j) % 25 else 0 for i in range(w)]
                    for j in range(h)]
    continuidad = True
    while continuidad:
        canvas.fill(pygame.Color('darkorchid4'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        [pygame.draw.line(canvas, pygame.Color('black'), (x, 0), (x, int(sys.argv[2])))
        for x in range(0, int(sys.argv[1]), 10)]
        [pygame.draw.line(canvas, pygame.Color('black'), (0, y), (int(sys.argv[1]), y))
        for y in range(0, int(sys.argv[2]), 10)]
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                if estadoActual[y][x]: 
                    pygame.draw.rect(canvas, pygame.Color('darkgoldenrod1'), (x * numero + 2, y * numero + 2, numero - 2, numero - 2))
                siguienteEstado[y][x] = vcell(estadoActual, x, y)
        estadoActual = deepcopy(siguienteEstado)
        pygame.display.flip()
if __name__ == "__main__":
    Lab3ConwaysGameOfLife()