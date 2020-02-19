import Subject as sb



class Schedule:
    
    def __init__(self):
        self.days = {}
        for day in sb.weekdays:
            self.days[day] = []
            self.Clash_Stat = False
    
    def addSubj(self , Subj):
        for items in self.days[Subj.day]:
            if(Subj.isClash(Subj,items)): 
                self.Clash_Stat = False
                return
        self.days[Subj.day].append(Subj)
        x =  self.addSubj(Subj.link) if (Subj.link != None) else True
        self.Clash_Stat = not (True and x)

    @staticmethod
    def removeClash(ScheduleList):
        for Sched in ScheduleList:
            if Sched.Clash_Stat == True:
                ScheduleList.remove(Sched)


    @classmethod
    def generateSchedule(cls,SubjDict):
        ScheduleList = [Schedule()]
        for SubjArray in SubjDict.values():
            SubjArrLength = len(SubjArray)
            if (SubjArrLength == 0) : continue #if array empty skip to next loop other wise it would * by zero and delete all previous loops' work
            ScheduleList = ScheduleList.copy() * SubjArrLength
            for SchedNum , Sched in enumerate(ScheduleList,1):
                    Sched.addSubj(SubjArray[round(SchedNum/SubjArrLength)])

            Schedule.removeClash(ScheduleList)
                    
                

        return ScheduleList

