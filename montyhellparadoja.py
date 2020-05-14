import time, random
import matplotlib.pyplot as plt


def montyHell(puertainicial = 0, totalpuertas = 0, intentos = 1):

    if totalpuertas == 0:
        totalpuertas = random.randint(3, 100)

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

        if puertainicial == 0:
            puertainicial = random.randint(1, totalpuertas)
        
        try:
            tempC = coche.index(1)  # BUSCA SI HAY UN 1
            coche[tempC] = 0
        except ValueError:
            pass

        posicioncoche = random.randint(0, totalpuertas - 1)  # INDICA LA POSICION O INDEX DEL COCHE
        coche[posicioncoche] = 1

        print ("TU PUERTA ES LA NUMERO ({}) Y EL COCHE ESTA EN LA PUERTA NUMERO ({})".format(puertainicial, coche.index(1) + 1))

        if coche[puertainicial - 1] == 1:
            print ("No has conseguido el coche :(\n")
            contadorFracasos += 1
            fracasos.append(contadorFracasos)
            aciertos.append(contadorAciertos)
        else:
            print("Has conseguido el coche!\n")
            contadorAciertos += 1
            fracasos.append(contadorFracasos)
            aciertos.append(contadorAciertos)

        intentos -= 1

    aciertosTotales = sum(aciertos)
    fracasosTotales = sum(fracasos)

    print("HAS ACERTADO: {} VECES".format(aciertosTotales))
    print("HAS FALLADO: {} VECES".format(fracasosTotales))

    probabilidadObtenida = aciertosTotales / (aciertosTotales + fracasosTotales) 

    print("\n EL NUMERO TOTAL DE PUERTAS HA SIDO: {}".format(totalpuertas))
    print("\n- EL PORCENTAJE QUE DEBERIA SALIR AL CAMBIAR DE PUERTA ES: {}%".format(probabilidadreal))
    print("\n- MIENTRAS QUE EL PORCENTAJE REAL HA SIDO: {}%".format(100 * probabilidadObtenida))

    xIntentos = [0]  # VARIABLE QUE GUARDA VALORES X
    for i in range(1, intentosiniciales + 1):
        xIntentos.append(i)

    plt.plot(xIntentos, aciertos)  # GRAFICA DE ACIERTOS AL CAMBIAR PUERTA
    plt.plot(xIntentos, fracasos)  # GRAFICA DE ERRORES AL CAMBIAR PUERTA

    #plt.show()



opcion = int(input("Quieres elegir tu en que puerta empezar y cuantas puertas deben haber (1) o que sea aleatorio? (2): "))
intentos = int(input("Cuantas veces quieres repetir el experimento?: "))

if opcion == 1:
    totalpuertas = int(input("Cuantas puertas quieres que hayan?: "))
    puertainicial = int(input("Que puerta quieres elegir? [1 - {}]: ".format(totalpuertas)))

    montyHell(puertainicial, totalpuertas, intentos)
else:
    montyHell(intentos = intentos)

