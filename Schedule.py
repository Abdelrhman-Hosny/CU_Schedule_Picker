import Subject as sb
from math import ceil
from copy import deepcopy


class Schedule:
    
    def __init__(self):
        self.days = {}
        for day in sb.weekdays:
            self.days[day] = []
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
        i , ListLength = 0 , len(ScheduleList)
        while(i < ListLength):
            if(ScheduleList[i].Clash_Stat == True):
                ScheduleList.remove(ScheduleList[i])
                ListLength -= 1
            else:
                i += 1

    @staticmethod
    def sort_day(day_list): 
        n = len(day_list) 
        for i in range(n):        
            for j in range(0, n-i-1): 

                if (day_list[j].startTime > day_list[j+1].startTime) : 
                    day_list[j], day_list[j+1] = day_list[j+1], day_list[j] 

    @staticmethod
    def sort_schedule(scheduleList):
        for Sched   in scheduleList:
            for day in Sched.days:
                Schedule.sort_day(Sched.days[day])
        
        



            
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
