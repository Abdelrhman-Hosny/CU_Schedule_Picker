import tkinter as tk
from Subject import Subject 
import Schedule , os
import tkinter.messagebox as msg
from SubjectLabel import SubjectLabel
from Save import Save
from Load import Load
from Print import Print
from Error import Error


class ScheduleMaker(tk.Tk):

    def __init__(self):
        super().__init__()

        #intializing the list that'll contain all subjects

        self.SubjectList = []
        
        #filename init

        self.filename = ""

        #Title and window Size 

        self.title("Schedule Picker v1")
        self.geometry("700x500")

        #Creating a dropdown menu
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.subMenu1 = tk.Menu(self.menu)

        self.menu.add_cascade(label ="Save/Load", menu = self.subMenu1)
        self.subMenu1.add_command(label = "Save",command = self.save)
        self.subMenu1.add_separator()
        self.subMenu1.add_command(label="Clear All",command=self.clear)
        self.subMenu1.add_command(label= "Load", command = self.load)
        self.subMenu1.add_command(label= "Clear & Load",command = self.load_clear)

        self.subMenu2 = tk.Menu(self.menu)
        self.menu.add_cascade(label ="Print", menu = self.subMenu2)
        self.subMenu2.add_command(label = "Print" , command = self.print)
        


        #creating and packing canvas and frames and scrollbar

        self.subj_canvas = tk.Canvas(self)

        self.subj_frame = tk.Frame(self.subj_canvas)
        self.entry_frame = tk.Frame(self)

        self.scrollbar = tk.Scrollbar(self.subj_canvas,orient="vertical",command=self.subj_canvas.yview)

        self.subj_canvas.configure(yscrollcommand=self.scrollbar.set)

        self.entry_frame.pack(side=tk.BOTTOM , fill = tk.X)
        
        self.scrollbar.pack(side=tk.RIGHT , fill = tk.Y)

        self.subj_canvas.pack(side=tk.TOP,fill = tk.BOTH , expand = 1)

        #creating and packing Entry & Label/Label Frames for tutorial and lecture

        self.lblfrm = tk.LabelFrame(self.entry_frame,text = "Enter Lecture and Tutorial info",pady = 15,bg="#808080")
        self.lbl_lect = tk.Label(self.lblfrm , text = "Lecture",padx = 10 ,pady = 10,bg="#808080")
        self.lbl_tut = tk.Label(self.lblfrm , text = "Tutorial", bg="#808080")


        #Labels to guide user

        self.CodeLabel = tk.Label(self.lblfrm , text = "Name", bg="#808080")
        self.DayLabel = tk.Label(self.lblfrm,text = "Day", bg="#808080")
        self.TimeSH = tk.Label(self.lblfrm,text = "Start Hour", bg="#808080")
        self.TimeSM = tk.Label(self.lblfrm,text = "Start Min", bg="#808080")
        self.TimeEH = tk.Label(self.lblfrm,text = "End Hour", bg="#808080")
        self.TimeEM = tk.Label(self.lblfrm,text = "End Min", bg="#808080")
        self.timeFrom1 = tk.Label(self.lblfrm,text = " From", bg="#808080")
        self.timeFrom2 = tk.Label(self.lblfrm,text = " From", bg="#808080")
        self.timeTo1 = tk.Label(self.lblfrm,text = " to ", bg="#808080")
        self.timeTo2 = tk.Label(self.lblfrm,text = " to ", bg="#808080")


        #Entries for lecture

        self.lectureCode_Entry = tk.Entry(self.lblfrm,width = 10)
        self.lectureDay_Entry = tk.Entry(self.lblfrm,width = 10 )
        self.lectureStartH_Entry = tk.Entry(self.lblfrm,width = 3)
        self.lectureStartM_Entry = tk.Entry(self.lblfrm,width = 3)
        self.lectureEndH_Entry = tk.Entry(self.lblfrm,width = 3)
        self.lectureEndM_Entry = tk.Entry(self.lblfrm,width = 3)

        #Entries for tutorial

        self.tutorialDay_Entry = tk.Entry(self.lblfrm,width = 10)
        self.tutorialStartH_Entry = tk.Entry(self.lblfrm,width = 3)
        self.tutorialStartM_Entry = tk.Entry(self.lblfrm,width = 3)
        self.tutorialEndH_Entry = tk.Entry(self.lblfrm,width = 3)
        self.tutorialEndM_Entry = tk.Entry(self.lblfrm,width = 3)


        #Packing Label Frame

        self.lblfrm.pack(side = tk.BOTTOM , fill = tk.X)

        #grid for user guiding labels

        self.lbl_lect.grid(row = 1 , column = 0)
        self.lbl_tut.grid(row = 2 , column = 0)
        self.CodeLabel.grid(row = 0 , column = 1)
        self.DayLabel.grid(row = 0 , column = 2)
        self.TimeSH.grid(row = 0 , column = 4)
        self.TimeSM.grid(row = 0 , column = 5)
        self.TimeEH.grid(row = 0 , column = 7)
        self.TimeEM.grid(row = 0 , column = 8)

        #Packing Lecture Entries

        self.lectureCode_Entry.grid(row = 1 , column = 1)
        self.lectureDay_Entry.grid(row = 1 , column = 2)
        self.timeFrom1.grid(row = 1 , column = 3)
        self.lectureStartH_Entry.grid(row = 1 , column = 4)
        self.lectureStartM_Entry.grid(row = 1 , column = 5)
        self.timeTo1.grid(row = 1 , column = 6)
        self.lectureEndH_Entry.grid(row = 1 , column = 7)
        self.lectureEndM_Entry.grid(row = 1 , column = 8)

        #Packing Tutorial Entries

        self.tutorialDay_Entry.grid(row = 2 , column = 2)
        self.timeFrom2.grid(row = 2 , column = 3)
        self.tutorialStartH_Entry.grid(row = 2 , column = 4)
        self.tutorialStartM_Entry.grid(row = 2 , column = 5)
        self.timeTo2.grid(row = 2 , column = 6)
        self.tutorialEndH_Entry.grid(row = 2 , column = 7)
        self.tutorialEndM_Entry.grid(row = 2 , column = 8)

        self.canvas_frame = self.subj_canvas.create_window((0,0),window=self.subj_frame,
        anchor="n")


        # Binding keys to certain functions
        self.bind("<Return>",self.add_subj)
        self.bind("<Configure>", self.on_subj_configure)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)

        

        

    def add_subj(self , event = None):
        lecText = ','.join([self.lectureCode_Entry.get().strip(),self.lectureDay_Entry.get().strip() ,self.lectureStartH_Entry.get().strip(),
        self.lectureStartM_Entry.get() , self.lectureEndH_Entry.get() , self.lectureEndM_Entry.get()])

        tutText = ','.join([self.tutorialDay_Entry.get().strip(),self.tutorialStartH_Entry.get(),self.tutorialStartM_Entry.get(),
        self.tutorialEndH_Entry.get(),self.tutorialEndM_Entry.get()])

        if not (tutText == ",,,,"):
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
        
        
        self.lectureDay_Entry.delete(0,tk.END)
        self.lectureStartH_Entry.delete(0,tk.END)
        self.lectureStartM_Entry.delete(0,tk.END)
        self.lectureEndH_Entry.delete(0,tk.END)
        self.lectureEndM_Entry.delete(0,tk.END)

        self.tutorialDay_Entry.delete(0,tk.END)
        self.tutorialEndM_Entry.delete(0,tk.END)
        self.tutorialEndH_Entry.delete(0,tk.END)
        self.tutorialStartH_Entry.delete(0,tk.END)
        self.tutorialStartM_Entry.delete(0,tk.END)








    
    def remove_subj(self, event):
        subj = event.widget
        if msg.askyesno("Really Delete?", "Delete " + subj.cget("text") + "?"):

            for subj in self.SubjectList:
                if(subj.SubLabel == event.widget):
                    self.SubjectList.remove(subj)
                    event.widget.destroy()
            # #self.recolour_tasks()




    
    

    def save(self):
        _ = Save(self.SubjectList)


    def load(self):
        _ = Load(self.subj_frame,self.SubjectList)

        
    def clear(self,event=None):

        if msg.askyesno("Clear","Clear All Subjects ?"):
            for subj in self.SubjectList:
                subj.SubLabel.destroy()
        self.SubjectList = []

    def load_clear(self):
        self.clear()
        self.load()

    def print(self):
        _ = Print(self.SubjectList)
        

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




