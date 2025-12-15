#opens file 
file = open("DayOneIn.txt", 'r')
lst = file.readlines()

newList = []
for line in lst:
    if line[-1] =="\n":
        newList.append(line[:-1])
    else:
        newList.append(line)
# position start at 50
pos = 50 

#counter for times at zero
taz = 0
for line in newList:

    #gets if L or R
    fChar = line[0]

    #gets # of moves
    rest = int(line[1:])

    #sets number of moves to < 100
    while rest > 99:
        rest = rest - 100
    


    if fChar == "L":
        pos = pos - rest
        if pos < 0:
            pos = pos + 100
    else:
        pos = pos + rest
        if pos > 99:
            pos = pos - 100
    
    if pos == 0:
        taz = taz + 1

print(taz)










# idetify the first careter beign iterh L R
# If L subtract foling number frm curent pos
# if curent pos - suptract that from 99 and if greater then 99 subtract 99 