import time, random, matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


plt.rcParams['toolbar'] = 'None' 

def montyHell(puertainicial, totalpuertas, intentos = 1):

    coche = []  # EL COCHE SERA UN 1 Y LAS CABRAS 0
    aciertos = [0]
    fracasos = [0]
    contadorAciertos = 0
    contadorFracasos = 0

    for total in range(totalpuertas):  # LLENA EL ARRAY DE CEROS (CABRAS)
        coche.insert(total, 0)

    probabilidadreal = ((1 + totalpuertas - 2) / totalpuertas) * 100
    intentosiniciales = intentos  # INTENTOS INICIALES PARA CALCULAR EL PORCENTAJE DE ACIERTO

    while intentos > 0:

        try:
            tempC = coche.index(1)  # BUSCA SI HAY UN 1
            coche[tempC] = 0
        except ValueError:
            pass

        posicioncoche = random.randint(0, totalpuertas - 1)  # INDICA LA POSICION O INDEX DEL COCHE
        coche[posicioncoche] = 1

        if coche[puertainicial - 1] == 1:  # IF THE CAR IS IN THE SAME DOOR YOU PICKED FIRST
            contadorFracasos += 1
            fracasos.append(contadorFracasos)
            aciertos.append(contadorAciertos)
        elif coche[puertainicial - 1] != 1:
            contadorAciertos += 1
            fracasos.append(contadorFracasos)  # IF THE CAR ISN'T IN THE SAME DOOR THAT YOU ARE
            aciertos.append(contadorAciertos)

        intentos -= 1

    aciertosTotales = aciertos[len(aciertos) - 1]
    fracasosTotales = fracasos[len(fracasos) - 1]

    print("HAS ACERTADO: {} VECES".format(aciertosTotales))
    print("HAS FALLADO: {} VECES".format(fracasosTotales))

    probabilidadObtenida = aciertosTotales / (aciertosTotales + fracasosTotales) 

    print("\n EL NUMERO TOTAL DE PUERTAS HA SIDO: {}".format(totalpuertas))
    print("\n- EL PORCENTAJE QUE DEBERIA SALIR AL CAMBIAR DE PUERTA ES: {}%".format(probabilidadreal))
    print("\n- MIENTRAS QUE EL PORCENTAJE REAL HA SIDO: {}%".format(100 * probabilidadObtenida))

    xIntentos = [0]  # VARIABLE QUE GUARDA VALORES X
    for i in range(1, intentosiniciales + 1):
        xIntentos.append(i)

    lineaAciertos, = plt.plot(xIntentos, aciertos, label='Puerta Cambiada')  # GRAFICA DE ACIERTOS AL CAMBIAR PUERTA
    lineaFracasos, = plt.plot(xIntentos, fracasos, label='Puerta Inicial')  # GRAFICA DE ERRORES AL CAMBIAR PUERTA

    plt.legend([lineaAciertos, lineaFracasos], ['Puerta Cambiada: {}'.format(aciertosTotales), 'Puerta Inicial: {}'.format(fracasosTotales)], loc='upper left')

    plt.xlabel("Nº intentos")
    plt.ylabel("Nº aciertos")

    plt.xlim(right = intentosiniciales, left = 0)
    plt.ylim(bottom = 0)

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    fig.suptitle('Monty Hall Problem', fontsize=14, fontweight='bold')
    ax.set_title('RESULTADO ESPERADO: {}%    -    RESULTADO OBTENIDO: {}%'.format(round(probabilidadreal, 2), round(100 * probabilidadObtenida, 2)))
    fig.canvas.set_window_title('La Paradoja de Monty Hall')

    plt.show()


while 1 > 0:
    opcion = input("\n\n\n############################## Quieres empezar con el PROBLEMA DE MONTY HALL? SI (s) NO (n): ")
    if opcion.lower() == 's':

        intentos = int(input("\n\n\n- Cuantas veces quieres que se haga el concurso (intentos): "))
        totalpuertas = int(input("\n- Cuantas puertas quieres que hayan?: "))
        puertainicial = int(input("\n- Que puerta quieres elegir? [1 - {}]: ".format(totalpuertas)))
        montyHell(puertainicial, totalpuertas, intentos)
    else:
        exit()


