# volleyball.py

def main():
    print Intro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)


def Intro():
    print "This program simulates a gsme of volleyball between"
    print "two players called A and B."
    print "player A always has the first serve"


def getInputs():
    a = input("Player A wins a serve")
    b = input("Player B wins a serve")
    n = input("How many games do you want to simulate?")
    return a, b, n


def simNGames(n, probA, probB):
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winB + 1
        return winsA, winsB


def simOneGame(probA, probB):
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"

    return scoreA, scoreB


def gameOver(a, b):
    return a == 15 or b == 15


def printSummary(winsA, winsB):
    n = winsA + winsB
    print "\nGames simulated", n
    print "Wins for A: %d (%0.1f%%)" % (winsA, float(winsA) / n * 100)


if __name__ == '__main__': main()