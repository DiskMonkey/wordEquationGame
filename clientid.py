from datetime import datetime
from datetime import timedelta


numIdentitiesInUse = 0
identitiesInUse = dict() #eventually, this should become a username/password combo, with the addition of guest passes

# hardcoding how long each task should be open for here:
taskTimings = {
    'get3': timedelta(seconds=10)
}

def getNewID(): #just generates a unique value. TODO: update to a hash
    global numIdentitiesInUse

    numIdentitiesInUse += 1
    identitiesInUse[numIdentitiesInUse] = None
    return numIdentitiesInUse

def isIDInUse(id: int):
    return (id in identitiesInUse)

def setIDtask(id: int, task: str):
    identitiesInUse[id] = (task, datetime.now())

def getIDtask(id: int):
    return identitiesInUse[id][0]

def getIDstart(id: int):
    return identitiesInUse[id][1]

def isIDInTask(id: int, task: str) -> bool:
    '''Given an int `id`, and a str `task`, checks whether the given task is still being completed.'''
    time = taskTimings[task]

    if (isIDInUse(id) and (identitiesInUse[id] != None) and (getIDtask(id) == task)):
        oldtime = getIDstart(id)
        curtime = datetime.now()
        timePassed = curtime - oldtime

        return (time > timePassed)

    return False





