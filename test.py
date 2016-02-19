import Graph as g 
import matplotlib.pyplot as plt
import time
import numpy as np

graph = g.graphAlea(5, 5, 0.5)



def testalgoWelshPowel() :
    graph.algoWelshPowel()
    print(graph)

def testalgoDSATUR() :
    graph.algoDSATUR()
    print(graph)

def testalgoNaif() :
    graph.algoNaif()
    print(graph)

def moyenne50(n,p,algo) :
    if algo == 0:
        print("algoNaif")
    elif algo == 1 :
        print("algoDSATUR")
    elif algo == 2 :
        print("algoWelshPowel")
    temps = []
    couleurs = []
    for i in range(50) :
        graph = g.graphAlea(n,5,p)
        if algo == 0 :
            start_time = time.time()
            graph.algoNaif()
        elif algo == 1 :
            start_time = time.time()
            graph.algoDSATUR()
        elif algo == 2 :
            start_time = time.time()
            graph.algoWelshPowel()
        graph.algoNaif()
        interval = time.time() - start_time
        temps.append(interval)
        couleurs.append(graph.totalColor())
    sommeT = sum(temps)
    sommeC = sum(couleurs)
    return (float(sommeT)/50.,float(sommeC)/50)

def plotColor() :
    plt.xlabel('probabilité')
    x = np.linspace(0.1,0.9,num=9)
    plt.ylabel('colorations')
    y = np.zeros((3,9))
    for i in range(3) :
        for j in range(9) :
            y[i,j] = moyenne50(100,x[j],i)[1]
    labels=["algoNaif","algoDSATUR","algoWelshPowel"]
    for y_arr, label in zip(y,labels) :
        plt.plot(x,y_arr,label=label)
    plt.legend()
    plt.show()

def plotTemps() :
    plt.xlabel('probabilité')
    x = np.linspace(0.1,0.9,num=9)
    plt.ylabel('temps')
    y = np.zeros((3,9))
    for i in range(3) :
        for j in range(9) :
            y[i,j] = moyenne50(100,x[j],i)[0]
    labels=["algoNaif","algoDSATUR","algoWelshPowel"]
    for y_arr, label in zip(y,labels) :
        plt.plot(x,y_arr,label=label)
    plt.legend()
    plt.show()

plotTemps()
# print(moyenne50(50,0.5,0))
# print(moyenne50(50,0.5,1))
# print(moyenne50(50,0.5,2))



