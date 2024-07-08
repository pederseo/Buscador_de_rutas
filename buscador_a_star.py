import heapq

def heuristic( nodo_actual, nodo_final):
    '''Calcula la distancia Manhattan entre dos puntos a y b.'''
    x_ab = abs(nodo_actual[0] - nodo_final[0])
    y_ab = abs(nodo_actual[1] - nodo_final[1])
    return x_ab + y_ab


def a_star(inicio,objetivo,mapa):
    # print(mapa,inicio,objetivo)
    '''agloritmo de busqueda en grafos'''
    movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    open_set = []
    close_set = {}
    heapq.heappush(open_set, (0, inicio))

    g_score = [[float('inf')] * columnas for _ in range(filas)]
    g_score[inicio[0]][inicio[1]] = 0 #agrega un 0 a la primera posicion

    f_score = [[float('inf')] * columnas for _ in range(filas)]
    f_score[inicio[0]][inicio[1]] = heuristic(inicio, objetivo)


    #1)_______________________buscamos el coste total mas pequeno_________________________#
    while open_set:
        _, pos_actual = heapq.heappop(open_set) #extrae la posicion con menor coste


    #2)_______________________comprobamos si encontro el objetivo_________________________#
        if pos_actual == objetivo:
            camino = []
            while pos_actual in close_set:
                camino.append(pos_actual)
                pos_actual = close_set[pos_actual]
            camino.append(inicio)
            camino.reverse()
            return camino


    #3)_______________________evaluacion de movimientos posibles____________________________#
        for direction in movimientos:
            mov_eval = (pos_actual[0] + direction[0], pos_actual[1] + direction[1])
            #evaluacion si esta dentro de los limites y es un camino
            if 0 <= mov_eval[0] < filas and 0 <= mov_eval[1] < columnas and mapa[mov_eval[0]][mov_eval[1]] == ' ':
                tentative_g_score = g_score[pos_actual[0]][pos_actual[1]] + 1
                

    #4)________________________actualizacion de la cola de prioridades_______________________#
                if tentative_g_score < g_score[mov_eval[0]][mov_eval[1]]:
                    close_set[mov_eval] = pos_actual #nos indica de donde viene el movimiento evaluado

                    g_score[mov_eval[0]][mov_eval[1]] = tentative_g_score #+1
                    h_score = heuristic(mov_eval, objetivo)
                    f_score[mov_eval[0]][mov_eval[1]] = tentative_g_score + h_score #costo total

                    heapq.heappush(open_set, (f_score[mov_eval[0]][mov_eval[1]], mov_eval)) #carga los movimientos despues de la evaluacion
    # print(close_set)                

    return 'no se encontro'  # No se encontró una ruta

#_______________________________________________________________________________________________________________________________________________________________

mapa = [[' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#'],
        [' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#'],
        [' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#'],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' '],
        ['#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' '],
        ['#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' '],
        ['#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' '],
        ['#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' '],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        [' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#'],
        [' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#'],
        [' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#'],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
        ['#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#'],
        ['#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#'],
        ['#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#','#','#',' ','#'],
        [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

filas = len(mapa)
columnas = len(mapa[0])

inicio_x = int(input('ingrese x inicio '))
inicio_Y = int(input('ingrese y inicio '))
inicio = (inicio_x,inicio_Y)

objetivo_x = int(input('ingrese x objetivo '))
objetivo_Y = int(input('ingrese y objetivo '))
objetivo = (objetivo_x,objetivo_Y)

obstaculo_x = int(input('ingrese x obstaculo '))
obstaculo_Y = int(input('ingrese y obstaculo '))
obstaculo = (obstaculo_x,obstaculo_Y)

mapa[obstaculo_x][obstaculo_Y] = '#'

camino = a_star(inicio,objetivo,mapa)
print(f'camino encontrado: {camino}')
