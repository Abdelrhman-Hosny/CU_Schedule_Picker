import datetime
weekdays = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Saturday']
class Subject:
    def __init__(self,code,day,startHour,startMin,endHour,endMin,link=None):
        self.code = code.strip().upper()
        self.day = day.strip().lower().capitalize()
        self.startTime = datetime.time(startHour,startMin)
        self.endTime = datetime.time(endHour,endMin)
        self.link = link
    
    @staticmethod
    def isBetween(T1,T2,T3):
        '''returns true if the time object T1 is between the times T2 and T3 
           returns false otherwise'''
        if(T1 > T2 and T1 < T3): return True
        return False


    def isClash(self,Subj):
        if(self.day != Subj.day): return False
        if(self.startTime == Subj.startTime): return True
        if(Subject.isBetween(self.startTime, Subj.startTime , Subj.endTime)):return True
        if(Subject.isBetween(Subj.startTime , self.startTime,self.endTime)): return True
        return False

    def __str__(self):
        return "{} from {} to {} ".format(self.code,self.startTime,self.endTime)

    def __repr__(self):
        return str(self)
    
    @classmethod
    def from_string(cls , s_main , s_link=None):
        cd , dy , stH , stM ,enH , enM = s_main.split(',')
        if not(s_link == None):
            _ , dy1 , stH1 , stM1 ,enH1 , enM1 = s_link.split(',')
            return cls(cd,dy,int(stH),int(stM),int(enH),int(enM),cls(cd,dy1,int(stH1),int(stM1),int(enH1),int(enM1)))
        return cls(cd,dy,int(stH),int(stM),int(enH),int(enM))

    def __eq__(self,sub2):
        if not isinstance(sub2 , Subject):
            return False 
        
        compLect = (self.code == sub2.code) and (self.startTime == sub2.startTime) and (self.endTime == sub2.endTime) and (self.day == sub2.day)
        
        if (self.link == None or sub2.link == None):
            compTut = True
        else:
            compTut = (self.link.code == sub2.link.code) and (self.link.startTime == sub2.link.startTime) and (self.link.endTime == sub2.link.endTime) and (self.link.day == sub2.link.day)
        return (compLect and compTut)
        



