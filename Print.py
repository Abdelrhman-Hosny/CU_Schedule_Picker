from Action import Action
import os
import Schedule
import Subject

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

        # Opens file and prints Schedules inside it

        f = open(os.path.expanduser(self.filename),"w+")
        for i , Sched in enumerate(self.ScheduleList,1):
            f.write('-'*25 + ' Schedule ( '+ str(i) + ' ) ' + '-' * 25)
            f.write("\n")
            for key , val in Sched.days.items():
                line = key + " : " +  str(val)
                f.write(line)
                f.write("\n")

        f.close()

        # destroy window
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


