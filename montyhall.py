import time, random, matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


plt.rcParams['toolbar'] = 'None' 

def montyHell(initialDoor, totalDoors, tries = 1):

    contest = []  # CONTEST, WHERE THE (0) REPRESENTS THE "GOATS" AND THE (1) REPRESENTS THE "CAR"
    
    # ARRAY TO MAKE THE GRAPH
    success = [0] 
    fails = [0]

    # SUCCESS/FAILS COUNTERS
    successCounter = 0
    failsCounter = 0

    for total in range(totalDoors):  # FILL THE ENTIRE CONTEST WITH 0
        contest.insert(total, 0)

    realProb = ((1 + totalDoors - 2) / totalDoors) * 100  # REAL PROBABILITY
    initialTries = tries  # INITIAL TRIES TO CALCULATE THE SUCCESS PROBABILITY

    while tries > 0:

        # LOOK IF THERE IS ANY (1) "CAR" IN THE CONTEST AND REMOVES IT
        try:
            tempC = contest.index(1)  
            contest[tempC] = 0
        except ValueError:
            pass

        carPos = random.randint(1, totalDoors)  # GENERATE RANDOM POS FOR THE CAR BETWEEN 1 AND TOTAL DOORS
        contest[carPos - 1] = 1

        # IF THE CAR IS IN THE SAME DOOR YOU PICKED FIRST
        if contest[initialDoor - 1] == 1:  
            failsCounter += 1
            fails.append(failsCounter)
            success.append(successCounter)

        # IF THE CAR ISN'T IN THE SAME DOOR THAT YOU ARE
        elif contest[initialDoor - 1] != 1:
            successCounter += 1
            fails.append(failsCounter)
            success.append(successCounter)

        tries -= 1

    #  LOOK FOR THE LAST NUMBER OF THE ARRAYS TO CHECK WHAT IS THE TOTAL SUCCESS/FAILS
    totalSuccess = success[len(success) - 1]
    totalFails = fails[len(fails) - 1]

    obtainedProb = totalSuccess / (totalSuccess + totalFails)  # OBTAINED PROBABILITY

    xtries = [0]  # ARRAY WHICH STORES THE TRIES TO USE IT IN THE GRAPH
    for i in range(1, initialTries + 1):
        xtries.append(i)

    successPlot, = plt.plot(xtries, success, label='Door Changed')  # SUCCESS GRAPHIC PLOT
    successPlot, = plt.plot(xtries, fails, label='Initial Door')  # FAIL GRAPHIC PLOT

    plt.legend([successPlot, successPlot], ['Door Changed: {}'.format(totalSuccess), 'Initial Door: {}'.format(totalFails)], loc='upper left')  # LEGEND WHICH SAYS HOW MANY FAILS/SUCCESS

    # LABELS
    plt.xlabel("Nº Tries")
    plt.ylabel("Nº Success")

    plt.xlim(right = initialTries, left = 0) 
    plt.ylim(bottom = 0)

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    fig.suptitle('Monty Hall Paradox', fontsize=14, fontweight='bold')
    ax.set_title('Expected: {}%    -    Obtained: {}%'.format(round(realProb, 2), round(100 * obtainedProb, 2)))
    fig.canvas.set_window_title('Monty Hall Paradox')

    plt.show()


while 1 > 0:
    opcion = input('''Want to start? if is Yes, write "s": ''')
    if opcion.lower() == 's':

        print('''\nYou need to choose:
        1) Tries
        2) Total Doors
        3) Initil Door
        - ALWAYS NUMBER > 0 -''')
        tries = int(input("\nHow many tries do you want?: "))
        totalDoors = int(input("How many doors do you want?: "))
        initialDoor = int(input("\nChoose your starting door [1 - {}]: ".format(totalDoors)))
        montyHell(initialDoor, totalDoors, tries)
    else:
        exit()


