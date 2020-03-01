import tkinter as tk
from Subject import Subject


class SubjectLabel(tk.Label):

    def __init__(self,Frame,lecText,tutText=None):
        self.cd , self.dy , self.stH , self.stM , self.enH , self.enM = lecText.split(",")
        if not (tutText == None):
            #splitting string
            self.cd1 , self.dy1 , self.stH1 , self.stM1 , self.enH1 , self.enM1 = tutText.split(",")

            #intializing Subject object
            self.SubObj = Subject(self.cd , self.dy , int(self.stH) , int(self.stM) , int(self.enH) , int(self.enM)
            ,Subject(self.cd1 , self.dy1 , int(self.stH1) , int(self.stM1) , int(self.enH1) , int(self.enM1)))

            #intializing Subejct Label
            self.SubLabel = tk.Label(Frame, text = "Lecture : " + self.SubObj.code + ' ' + self.SubObj.day + ' '+ str(self.SubObj.startTime) + ' to ' + str(self.SubObj.endTime) +
             ' Tut : ' + self.dy1 + ' ' + str(self.SubObj.link.startTime) + ' to ' + str(self.SubObj.link.endTime) , pady = 10)

        else:
            
            #intializing Subject object
            self.SubObj = Subject(self.cd , self.dy ,int(self.stH) , int(self.stM) , int(self.enH) , int(self.enM))

            #intializing Subejct Label
            self.SubLabel = tk.Label(Frame, text = "Lecture : " + self.SubObj.code + ' ' + self.SubObj.day + ' '+ str(self.SubObj.startTime) + ' to ' + str(self.SubObj.endTime),pady = 10)




    def __del__(self):
        pass 


