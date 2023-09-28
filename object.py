from datetime import datetime
import numpy as np

class kinematicObject():
    def __init__(self, oMass, oSize, oLocation):
        self.objectMass = oMass
        self.objectSize = oSize
        self.objectLocation = oLocation
        self.objectAcceleration = np.array([0.0, 0.0])
        self.lastUpdate = datetime.now()
        
    def updateAcceleration(self, newAccel):
        '''Adjust object's acceleration'''
        self.objectAcceleration += np.array(newAccel)
        
    def applyAcceleration(self):
        '''Apply the acceleration based on the given time'''
        t = datetime.now()
        self.objectLocation += np.array(self.objectAcceleration) * (t - self.lastUpdate).total_seconds() **2
        self.lastUpdate = datetime.now()
    def getGravityByDistance(self, distance, oMass):
        g = [0,0]
        d = ((distance[0] -self.objectLocation[0])**2 + (distance[1] - self.objectLocation[1])**2)**0.5
        G = (self.objectMass * oMass)/(d**2)
        
        if G < self.objectMass:
            g[0] = (-distance[0] + self.objectLocation[0]) * G
            g[1] = (-distance[1] + self.objectLocation[1]) * G
        
            #print(d)
            #print(G)
        return g
        


class stationaryObject():
    def __init__(self, pMass, pLocation, pRadius):
        self.planetMass = pMass
        self.planetLocation = pLocation
        self.planetRadius = pRadius
        
    def getGravityByDistance(self, distance, oMass):
        g = [0,0]
        d = ((distance[0] -self.planetLocation[0])**2 + (distance[1] - self.planetLocation[1])**2)**0.5
        G = (self.planetMass * oMass)/(d**2)
        
        if G < self.planetMass:
            g[0] = (-distance[0] + self.planetLocation[0]) * G
            g[1] = (-distance[1] + self.planetLocation[1]) * G
        
            #print(d)
            #print(G)
        return g
    
    def collisionCheck(self, oLoc):
        d = ((oLoc[0] -self.planetLocation[0])**2 + (oLoc[1] - self.planetLocation[1])**2)**0.5
        if d <= self.planetRadius:
            return True
        else:
            return False
    