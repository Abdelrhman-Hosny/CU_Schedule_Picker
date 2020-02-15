import Subject as sb



class Schedule:
    
    def __init__(self):
        self.days = {}
        for day in sb.weekdays:
            self.days.setdefault(day ,[])
    
    def addSubj(self , Subj):
        for items in self.days[Subj.day]:
            if(Subj.isClash(Subj,items)): return False
        self.days[Subj.day].append(Subj)
        return True

