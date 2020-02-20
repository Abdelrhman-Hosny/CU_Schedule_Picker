import Subject as sb
from math import ceil
from copy import deepcopy


class Schedule:
    
    def __init__(self):
        self.days = {}
        for day in sb.weekdays:
            self.days[day.lower()] = []
            self.Clash_Stat = False
    
    def addSubj(self , Subj):
        for items in self.days[Subj.day]:
            if(Subj.isClash(items)): 
                self.Clash_Stat = True
                return
        self.days[Subj.day].append(Subj)
        if Subj.link != None:
            self.addSubj(Subj.link)
       

    @staticmethod
    def removeClash(ScheduleList : list):
        for Sched in ScheduleList:
            if Sched.Clash_Stat == True:
                ScheduleList.remove(Sched)


    @staticmethod
    def generateSchedule(SubjDict : dict) -> list :
        ScheduleList  = [Schedule()]
        for SubjArray in SubjDict.values():
            SubjArrLength = len(SubjArray)
            if (SubjArrLength == 0) : continue #if array empty skip to next loop other wise it would * by zero and delete all previous loops' work
            len_schedule = len(ScheduleList)
            newScheduleList = []
            for _ in range(SubjArrLength):
                newScheduleList += deepcopy(ScheduleList)
            ScheduleList = deepcopy(newScheduleList)
            len_schedule *= SubjArrLength
            subjIndex = 0
            for SchedNum , Sched in enumerate(ScheduleList,1):
                if((SchedNum % (len_schedule / SubjArrLength)) == 0 ):
                    subjIndex += 1
                Sched.addSubj((SubjArray[subjIndex - 1]))

            Schedule.removeClash(ScheduleList)
                    
        return ScheduleList


    def __str__(self):

        return str(self.days)

    def __repr__(self):

        return str(self)
