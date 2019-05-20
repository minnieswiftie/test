import os
import numpy as np
from scipy.signal import find_peaks, argrelextrema
import matplotlib.pyplot as plt


# def printFiles(path):
#     if (os.path.isdir(path) == False):
#         # base case:  not a folder, but a file, so print its path
#         print(path)
#     else:
#         # recursive case: it's a folder
#         for filename in os.listdir(path):
#             printFiles(path + "/" + filename)


#printFiles("sampleFiles")

def run(path):
    #for file in folder:
    data = readSSM(path)
    #displayGraph(data)
    findMaxima(data)
    #writeToCSV(maxima)
    
    
def displayGraph(data):
    xValues = []
    yValues = []
    for i in range(len(data)):
        xValues.append(data[i][0])
        yValues.append(data[i][1])
    plt.plot(xValues,yValues)
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Photon #")
    plt.show()



def readSSM(path):
    fileString = open(path, 'r').readlines()
    print(fileString)
    result = []
    for data in fileString:
        x = getWavelength(data)
        y = getPhoton(data)
        result.append((x,y))
    return result

def getWavelength(data):
    for i in range(len(data)):
        if data[i] == '\t':
            return round(float(data[:i]),1)
            
def getPhoton(data): #assume power is 0 <= x < 100
    for i in range(len(data)):
        if data[i] == '\t':
            return round(float(data[i+1:-5])*(10**int(data[-3:-1])),1)
    
    
def findMaxima(data):
    xValues = []
    yValues = []
    for i in range(len(data)):
        xValues.append(data[i][0])
        yValues.append(data[i][1])
    xnp = np.array(xValues)
    ynp = np.array(yValues)
    
    sortId = np.argsort(xnp)
    xnp = xnp[sortId]
    ynp = ynp[sortId]

    maxm = argrelextrema(ynp, np.greater)  # (array([1, 3, 6]),)
    minm = argrelextrema(ynp, np.less)  # (array([2, 5, 7]),)

    peaks, _ = find_peaks(ynp, height = 3000, distance = 150)
    
    # this way the x-axis corresponds to the index of x
    plt.plot(xnp, ynp)
    plt.plot(peaks, ynp[peaks], "x")
    print(peaks, ynp[peaks])
    plt.show()
    
    
    # for i in range(5, len(data)-5):
    #     if data[i][1] > data[i+1][1] and data[i-5][1]:
    #         result.append(data[i])
    # return result

def writeToCSV(maxima):
    pass
    
    
run("emissionFiles/1_CN4_NN1.SSM")