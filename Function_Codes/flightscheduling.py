def greedyFlightScheduling(tripLists):
    def generateTasks(tripLists):
        tasksDict={}
        num=len(tripLists)
        for i in range(num):
            tasksDict['task'+str(i+1)]=tripLists[i]
        return tasksDict
    def getTasks(dict):
        keys=list(dict.keys())
        ddlen=len(dict)
        dd = {}
        for j in range(ddlen):
            dd['SPDXAIF_' + str(j + 1)] = []
            currList=dict[keys[j]]
            for i in range(len(currList) - 1):
                fromPlace = currList[i]
                toPlace = currList[i + 1]
                dd['SPDXAIF_' + str(j + 1)].append([fromPlace, toPlace])
        return dd
    def minimumFlightSchedule(tasks_dict):
        placesTask=tasks_dict
        tasks=[ele for ele in placesTask.keys()]
        #print(tasks)
        flightPosition={}
        flightNum=1
        for key in placesTask:
            flightPosition['f'+str(flightNum)] = [placesTask[key][0],placesTask[key][1]]
            flightNum+=1
        # print()
        # print('Initial Tasks\n',flightPosition)
        # print()
        newSeqOfTasks={}
        newSeqOfTasks['newf'+str(1)]=flightPosition['f'+str(1)]
        for k in range(2, len(placesTask)+1):
            for i in range(2, len(placesTask)+1):
                for j in range (i,len(placesTask)+1):
                    if  newSeqOfTasks['newf' + str(i-1)][-1]==flightPosition['f'+str(j)][0]:
                        place=flightPosition['f'+str(j)][1]
                        if place not in newSeqOfTasks['newf' + str(i-1)]:
                            newSeqOfTasks['newf' + str(i-1)].append(flightPosition['f'+str(j)][1])
                   #else:
                    newSeqOfTasks['newf'+str(i)]=(flightPosition['f'+str(i)])
            #print('Kth iteration k=',k,': ',newSeqOfTasks)
        #print('Actual Tasks \n',newSeqOfTasks)
        #print('Maximum flights required : ',len(newSeqOfTasks))
        #print()
        listOfLists=[]
        for key, value in newSeqOfTasks.items():
            listOfLists.append(newSeqOfTasks[key])
        #print('Unsorted ',listOfLists)
        listOfLists.sort(key=len)
        #print('Sorted   ',listOfLists)
        delList=[]
        for i in range(len(listOfLists)-1):
            currListI = listOfLists[i]
            for j in range(1, len(listOfLists)):
                currListJ = listOfLists[j]
                for k in range(0,len(currListI)):
                    if currListI[k] in currListJ:
                        if k == 0:
                            presenceInd = currListJ.index(currListI[k])
                        else:
                            nowInd=currListJ.index(currListI[k])
                            if (nowInd==presenceInd+1):
                                if currListI not in delList:
                                    if len(currListI)<len(currListJ):
                                        delList.append(currListI)
                                        #print('I',currListI)
                                        #print('J', currListJ)
        def get_key(dict,val):
            for key, value in dict.items():
                if val == value:
                    return key
            return "NOT AVAILABLE"
        for ele in delList:
            newSeqOfTasks.pop(get_key(newSeqOfTasks,ele))
        #print('Final Tasks\n',newSeqOfTasks)
        numFlights = len(newSeqOfTasks)
        #print('Minimum flights required : ',numFlights)
        #print()
        finalTrips=getTasks(newSeqOfTasks)
        #print('Scheduled Flights\n',finalTrips)
        numFlights=len(finalTrips)
        #print('No of Scheduled Flights : ',numFlights)
        return finalTrips
    trip_dict=generateTasks(tripLists)
    finalTrips=minimumFlightSchedule(trip_dict)
    return finalTrips