import os
import shutil
import time

days = 30

path = input("Enter path: ")
isExist = os.path.exists(path)
print(isExist)

def getTime():
    if isExist==True:
        print("Working")
        os.walk(path)
        os.path.join(path)
        ctime = os.stat(path).st_ctime
        return ctime
        if (ctime>=days):
            print("Time Exceeded")
            shutil.rmtree(path)

    else:
        print("File not recognised")

getTime()







    
