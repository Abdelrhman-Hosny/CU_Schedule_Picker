import datetime
class Subject:
    def __init__(self,code,day,startHour,startMin,endHour,endMin):
        self.code = code
        self.day = day
        self.startTime = datetime.time(startHour,startMin)
        self.endTime = datetime.time(endHour,endMin)
    
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
    
        
