from object import kinematicObject, stationaryObject
import matplotlib.pyplot as plt
import numpy as np
import time




if __name__ == "__main__":
    kinObj = []
    statObj = []
    '''Setup Plot'''
    plt.ion()
    fig=plt.figure()
    x=list()
    y=list()
    axSize = 100
    
    '''Setup objects'''
    #Create moving object.
    kinObj.append(kinematicObject(1, {"x": 2, "y": 2}, [8.5, 30]))
    kinObj.append(kinematicObject(0.5, {"x": 2, "y": 2}, [10, -30]))
    print(kinObj[0].objectSize)
    #Set object acceleration
    kinObj[0].updateAcceleration([500, 0])
    kinObj[1].updateAcceleration([-500, 0])
    #Create stationary gravitational object 
    statObj.append(stationaryObject(1000, [8.5, -7.2], 2))
    statObj.append(stationaryObject(2000, [-30, 0], 2))
    
    #Start event loop
    while True:
        #Apply and update acceleration to object.
        for i in range(len(kinObj)):
            kinObj[i].applyAcceleration()
            for k in range(len(statObj)):
                kinObj[i].updateAcceleration(statObj[k].getGravityByDistance(kinObj[i].objectLocation, kinObj[i].objectMass))
            for j in range(len(kinObj)):
                if j != i:
                    kinObj[i].updateAcceleration(kinObj[j].getGravityByDistance(kinObj[i].objectLocation, kinObj[i].objectMass))
        
        #Collision Checking
        toDelete = []
        for i in range(len(kinObj)):
            for j in range(len(statObj)):
                if statObj[j].collisionCheck(kinObj[i].objectLocation):
                    toDelete.append(i)
        toDelete.reverse()
        if len(toDelete) > 0:
            for i in range(len(toDelete)):
                del kinObj[toDelete[i]]
                print("Collision Occured")
        
                    
                
        
        #Plot functions
        plt.clf() #Comment out to see path
        for i in range(len(statObj)):
            plt.scatter(statObj[i].planetLocation[0], statObj[i].planetLocation[1])
        for i in range(len(kinObj)):
            plt.scatter(kinObj[i].objectLocation[0], kinObj[i].objectLocation[1])
        #print(square.objectLocation[1])
        for i in range(len(kinObj)):
            if abs(kinObj[i].objectLocation[0]) > axSize or abs(kinObj[i].objectLocation[1]) > axSize:
                axSize = max(abs(kinObj[i].objectLocation[0]), abs(kinObj[i].objectLocation[1])) + 100
        plt.axis((-axSize, axSize, -axSize, axSize))
        plt.show()
        plt.pause(0.0001)
        
        