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
    distance = int(line[1:])

    #sets number of moves to < 100
    for _ in range(distance):
        if fChar == "L":
            pos -= 1
        else:
            pos += 1

        if pos > 99:
            pos -= 100
        elif pos < 0:
            pos += 100
        
        if pos == 0:
            taz += 1
    

print(taz)
