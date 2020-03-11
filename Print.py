from Action import Action
import os
import Schedule
import Subject
from Error import Error
class Print(Action):

    def __init__(self,SubjectList):
        super().__init__()
        self.butt.config(text="Print")
        self.SubjectList = SubjectList
        self.wind.bind("<Return>",self.execute)


    def execute(self, event = None):
        Action.execute(self)
        self.generate_dict()
        self.generate_schedule()

        #checking that the user enters a name 

        if(len(self.filename)==0):
            _ = Error("File must have a name")
            return

        # Opens file and prints Schedules inside it
        fullfilename = os.getcwd() + '/' +self.filename +'.txt'
        self.filename = fullfilename
        f = open(os.path.expanduser(self.filename),"w+")
        for i , Sched in enumerate(self.ScheduleList,1):
            f.write('-'*25 + ' Schedule ( '+ str(i) + ' ) ' + '-' * 25)
            f.write("\n")
            for key , val in Sched.days.items():
                line = key + " : " +  str(val)
                f.write(line)
                f.write("\n")
        
        self.filename = ""
        f.close()

        self.wind.destroy()

    def generate_dict(self):
        self.SubjectDict = {}
        for Subj in self.SubjectList:
            self.SubjectDict.setdefault(Subj.SubObj.code,[])
            self.SubjectDict[Subj.SubObj.code].append(Subj.SubObj)


    def generate_schedule(self,event=None):
        self.generate_dict()
        self.ScheduleList = Schedule.Schedule.generateSchedule(self.SubjectDict)
        Schedule.Schedule.sort_schedule(self.ScheduleList)


