# read sensor data file and generate plots
import os
fileAndfolderPathStoreData="/home/pi/BioMaker/GitHubGardenObserver/Data/GardenObserver_SensorData.txt"

if os.path.isfile(fileAndfolderPathStoreData):  #check if file exists
    fileHandle = open(fileAndfolderPathStoreData,"r")
    for i in range(8):
        a=fileHandle.read(5)
        print(a)

    
    
else:
      print("Datafile not found")
      
    
