#This is this terms subects that I'm taking on which I'm going to try the algorithm
from Subject import Subject
from Schedule import Schedule
import time
dis = []
dis.append(Subject("MTHN104" , "Sunday" ,8,0,11,0,Subject("MTHN104","Wednesday",13,0,15,0) ))
dis.append(Subject("MTHN104" , "Wednesday" ,8,0,11,0,Subject("MTHN104","Wednesday",11,0,13,0)) )
num = []
num.append(Subject("MTHN201" , "Thursday" ,8,0,11,0,Subject("MTHN201","Thursday",11,0,13,0)) )
num.append(Subject("MTHN201" , "Monday" ,8,0,11,0,Subject("MTHN201","Tuesday",13,0,15,0) ))

""" pres =[]
pres.append(Subject("GENN201","Sunday",9,0,11,0))
pres.append(Subject("GENN201","Sunday",11,0,13,0))
pres.append(Subject("GENN201","Tuesday",9,0,11,0))
pres.append(Subject("GENN201","Tuesday",11,0,13,0))
 """
mech = []
mech.append(Subject("INTN125","Thursday",8,0,11,0,Subject("INTN125","Sunday",9,0,11,0)))
mech.append(Subject("INTN125","Monday",8,0,11,0,Subject("INTN125","Thursday",11,0,13,0)))

dat_lec = []

dat_lec.append(Subject("CMPN102L","Monday",11,0,13,0))
dat_lec.append(Subject("CMPN102L","Monday",14,0,16,0))
dat_lec.append(Subject("CMPN102L","Wednesday",9,0,11,0))
dat_lec.append(Subject("CMPN102L","Wednesday",11,0,13,0))
data_tut = []

data_tut.append(Subject("CMPN102T","Thursday",8,0,11,0))
data_tut.append(Subject("CMPN102T","Thursday",13,0,16,0))
data_tut.append(Subject("CMPN102T","Thursday",16,0,19,0))

circ_lec = []
circ_tut = []

circ_lec.append(Subject("ELCN112L","Sunday",13,0,16,0))
circ_lec.append(Subject("ELCN112L","Tuesday",13,0,16,0))
circ_lec.append(Subject("ELCN112L","Tuesday",8,0,11,0))
circ_tut.append(Subject("ELCN112T","Wednesday",11,0,13,0))
circ_tut.append(Subject("ELCN112T","Wednesday",14,0,16,0))
circ_tut.append(Subject("ELCN112T","Thursday",11,0,13,0))
circ_tut.append(Subject("ELCN112T","Thursday",14,0,16,0))


Subject_Dict = {}
Subject_Dict[dis[0].code] = dis
""" Subject_Dict[pres[0].code] = pres """
Subject_Dict[num[0].code] = num
Subject_Dict[dat_lec[0].code] = dat_lec
Subject_Dict[data_tut[0].code] = data_tut
Subject_Dict[mech[0].code] = mech
Subject_Dict[circ_lec[0].code] = circ_lec
Subject_Dict[circ_tut[0].code] = circ_tut


Schedule_List = Schedule.generateSchedule(Subject_Dict)



# for Sched in Schedule_List:
#     print('-'*50)
#     for keys , val in Sched.days.items():
#         print(keys , " : ", val)








