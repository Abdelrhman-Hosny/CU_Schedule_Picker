import datetime
weekdays = ["Sunday","Monday",'Tuesday','Wednesday','Thursday']
class Subject:
    def __init__(self,code,day,startHour,startMin,endHour,endMin,link=None):
        self.code = code.upper()
        self.day = day.lower()
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
        return "{} : {} from {} to {} ".format(self.code,self.day,self.startTime,self.endTime)

    def __repr__(self):
        return str(self)
    

    
        
