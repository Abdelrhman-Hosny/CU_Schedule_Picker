from Action import Action
import os
from Error import Error

class Save(Action):

    def __init__(self,ScheduleList):
        super().__init__()
        self.butt.config(text = "Save")
        self.ScheduleList = ScheduleList
        self.wind.bind("<Return>",self.execute)

    
    def execute(self,event = None):
        Action.execute(self)
        #making sure filename isn't "" and that it doesnt have commas
        if(len(self.filename)==0):
            _ = Error("File must have a name")
            return
        if( "," in self.filename):
            _ = Error("Cannot use commas in filename when saving")
            return

        #saving items into the file
        fullfilename = os.getcwd() + '/' +self.filename +'.txt'
        self.filename = fullfilename
        f = open(os.path.expanduser(self.filename),"w+")
        for i , subj in enumerate(self.ScheduleList, 1):
            f.write(str(i) + "\t")
            lectext = subj.cd + ','+ subj.dy + ',' + subj.stH + ',' +subj.stM + ',' +subj.enH + ','+ subj.enM
            f.write(lectext)
            f.write("\t")
            if not (subj.SubObj.link == None):
                tuttext = subj.dy1 + ',' + subj.stH1 + ',' +subj.stM1 + ',' +subj.enH1 + ','+ subj.enM1
                f.write(tuttext)
            else:
                f.write("None")
            f.write("\n")
            
        f.close()
        self.filename = ""
        self.wind.destroy()