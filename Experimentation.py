from Subject import Subject

x1 = Subject("ELCN112L","Sunday",13,0,16,0)
x2 = Subject("CMPN102T","Thursday",16,0,19,0)

x = [x1 , x2]

x = x.copy() * 2
for i in x:
    print(i)

def remFirst(List):
    List.remove(1)


x = [1,2,3,4]

remFirst(x)

print(x)


