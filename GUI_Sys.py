import tkinter as tk
from Subject import Subject 
import Schedule , os
import tkinter.messagebox as msg
from SubjectLabel import SubjectLabel



class ScheduleMaker(tk.Tk):

    def __init__(self):
        super().__init__()

        #intializing the main dictionary and list that'll contain all subjects

        self.SubjectDict = {}
        self.SubjectList = []
        

        #Title and window Size 

        self.title("Schedule Picker v1")
        self.geometry("700x500")

        #creating and packing canvas and frames and scrollbar

        self.subj_canvas = tk.Canvas(self)

        self.subj_frame = tk.Frame(self.subj_canvas)
        self.entry_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.subj_canvas,orient="vertical",command=self.subj_canvas.yview)

        self.subj_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.entry_frame.pack(side=tk.BOTTOM , fill = tk.X)
        
        self.scrollbar.pack(side=tk.RIGHT , fill = tk.Y)

        self.subj_canvas.pack(side=tk.TOP,fill = tk.BOTH , expand = 1)

        #creating and packing Entry for tutorial and lecture
        self.lblfrm = tk.LabelFrame(self.entry_frame,text = "Enter Lecture and Tutorial info",pady = 15,bg="#808080")
        self.lbl_lect = tk.Label(self.lblfrm , text = "Lecture",padx = 10 ,pady = 10,bg="#808080")
        self.lbl_tut = tk.Label(self.lblfrm , text = "Tutorial", bg="#808080")
        self.lectureEntry = tk.Entry(self.lblfrm,width = 35)
        self.tutorialEntry = tk.Entry(self.lblfrm,width = 35)

        self.lblfrm.pack(side = tk.BOTTOM , fill = tk.X)
        self.lbl_lect.grid(row = 0 , column = 0)
        self.lbl_tut.grid(row = 1 , column = 0)
        self.lectureEntry.grid(row = 0 , column = 2)
        self.tutorialEntry.grid(row = 1 , column = 2)

        self.canvas_frame = self.subj_canvas.create_window((0,0),window=self.subj_frame,
        anchor="n")

    




        # Binding keys to certain functions
        self.bind("<Return>",self.add_subj)
        self.bind("<Configure>", self.on_subj_configure)
        self.bind("<Control-Return>",self.generate_schedule)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)

        

        
    # def add_subj(self,event=None):
    
    #     lecText = self.lectureEntry.get().strip()
    #     tutText = self.tutorialEntry.get().strip()

    #     if not (tutText == ""):
    #         #self.SubjectList.append(Subject.from_string(lecText,tutText))
    #         new_subj = tk.Label(self.subj_frame,text = "Lect " +lecText + " Tut " + tutText , pady = 10)

    #         new_subj.bind("<Button-1>",self.remove_subj)
    #         new_subj.pack(side = tk.TOP , fill = tk.X , anchor = "center")

    #         self.SubjectLabels.append(new_subj)
    #     else:
    #         #self.SubjectList.append(Subject.from_string(lecText))
    #         new_subj = tk.Label(self.subj_frame,text = "Lect " +lecText , pady = 10 )

    #         new_subj.bind("<Button-1>",self.remove_subj)
    #         new_subj.pack(side = tk.TOP , fill = tk.X,anchor = "center")

    #         self.SubjectLabels.append(new_subj)
            

    #     self.tutorialEntry.delete(0,tk.END)
    #     self.lectureEntry.delete(0,tk.END)

    def add_subj(self , event = None):
        lecText = self.lectureEntry.get().strip()
        tutText = self.tutorialEntry.get().strip()
        if not (tutText == ""):
            #subNlabel = Subject and Label
            subNlabel = SubjectLabel(self.subj_frame,lecText,tutText)
            subNlabel.SubLabel.pack(side = tk.TOP , fill = tk.X , anchor = "center")
            subNlabel.SubLabel.bind("<Button-1>",self.remove_subj)
            self.SubjectList.append(subNlabel)
        else:
            #subNlabel = Subject and Label
            subNlabel = SubjectLabel(self.subj_frame,lecText)
            subNlabel.SubLabel.pack(side = tk.TOP , fill = tk.X , anchor = "center")
            subNlabel.SubLabel.bind("<Button-1>",self.remove_subj)
            self.SubjectList.append(subNlabel)
        
        self.tutorialEntry.delete(0,tk.END)
        self.lectureEntry.delete(0,tk.END)


    def generate_dict(self):
        self.SubjectDict = {}
        for Subj in self.SubjectList:
            self.SubjectDict.setdefault(Subj.SubObj.code,[])
            self.SubjectDict[Subj.SubObj.code].append(Subj.SubObj)


    def generate_schedule(self,event=None):
        self.generate_dict()
        self.ScheduleList = Schedule.Schedule.generateSchedule(self.SubjectDict)
        Schedule.Schedule.sort_schedule(self.ScheduleList)

    # def print_schedule(self):
    #     path = os.getcwd()
    #     f = open(path+r'/'+self.filename,"w+")

    #     for i , Sched in enumerate(self.ScheduleList,1):
    #         f.write('-'*25 + ' Schedule ( '+ str(i) + ' ) ' + '-' * 25)
    #         f.write("\n")
    #         for key , val in Sched.days.items():
    #             line = key + " : " +  str(val)
    #             f.write(line)
    #             f.write("\n")

    #     f.close()

    def remove_subj(self, event):
        subj = event.widget
        if msg.askyesno("Really Delete?", "Delete " + subj.cget("text") + "?"):

            for subj in self.SubjectList:
                if(subj.SubLabel == event.widget):
                    self.SubjectList.remove(subj)
                    event.widget.destroy()
            # self.SubjectLabels.remove(event.widget)
            # event.widget.destroy()
            # #self.recolour_tasks()

    def mouse_scroll(self, event):
        if event.delta:
            self.subj_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1

            self.subj_canvas.yview_scroll(move, "units")

    def on_subj_configure(self, event=None):
        self.subj_canvas.configure(scrollregion=self.subj_canvas.bbox("all"))

if __name__ == "__main__":

    sch = ScheduleMaker()
    sch.mainloop()




