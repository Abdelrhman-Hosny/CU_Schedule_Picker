#This is this terms subects that I'm taking on which I'm going to try the algorithm
from Subject import Subject
dis = []
dis.append(Subject("MTHN104" , "Sunday" ,8,0,11,0,Subject("MTHN104","Wednesday",13,0,15,0) ))
dis.append(Subject("MTHN104" , "Wednesday" ,8,0,11,0,Subject("MTHN104","Wednesday",11,0,13,0)) )
num = []
num.append(Subject("MTHN201" , "Thursday" ,8,0,11,0,Subject("MTHN201","Thursday",11,0,13,0)) )
num.append(Subject("MTHN201" , "Monday" ,8,0,11,0,Subject("MTHN201","Tuesday",13,0,15,0) ))

pres =[]
pres.append(Subject("GENN201","Sunday",9,0,11,0))
pres.append(Subject("GENN201","Sunday",11,0,13,0))
pres.append(Subject("GENN201","Tuesday",9,0,11,0))
pres.append(Subject("GENN201","Tuesday",11,0,13,0))

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

Subject_Dict = {}
Subject_Dict[dis[0].code] = dis
Subject_Dict[pres[0].code] = pres
Subject_Dict[num[0].code] = num
prod = 1
for key,val in Subject_Dict.items() :
    prod *= len(val)
print(prod*4*4*3)

