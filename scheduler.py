
import sys, getopt

def FCFS(data):                                                                                         #FCFS method
    gantt = []                                                                                         #Initlilize varibles 
    burst = []
    for i in range(len(data)):
        burst.append(data[i][2])                                                                        #Add another bust time to take away from
    stats = []
    print('----------------- FCFS -----------------')                                                   #print beginning things
    print('Process ID | Waiting Time | Turnaround Time')
    currtime = 0
    for i in range( len(data)):                                                                          #repeate for each process in data
        arrtime = data[i][1]
        if((currtime < arrtime) and (i != len(data)-1)):                                                #if current time is less than arival time system is IDLE
            holder = arrtime-currtime
            tempstr = ("[   "+str(currtime)+"   ]-- IDLE--[   "+str(data[i+1][1]-1)+"   ]")             #add IDLE string to list gantt
            gantt.append(tempstr)
            currtime = currtime +holder                                                                  #add differerence in time to current time 
        if(currtime >=arrtime):                                                                         #not IDLE if current time is greater than arival time of next item
            help = []
            help.append(data[i][0])
            help.append(data[i][1])                                                                        #add data like start and end time to an 2d list to print out adv waiting time later 
            help.append(currtime) 
            help.append(currtime + data[i][2])
            help.append(burst[i])
            tempstr = ("[   "+ str(currtime)+"   ]--  "+str(data[i][0])+"  --[   "+str(currtime + data[i][2])+"   ]")
            stats.append(help)                                                                              #add non IDLE string to gantt
            gantt.append(tempstr)
            currtime = currtime + data[i][2]
    stats.sort(key=lambda x: x[0])                                                                      #sort the stats list by PID
    num = []
    for j in range(len(stats)):
        temp = []
        tempstr = ("      "+ str(stats[j][0])+"    |      "+str(stats[j][3] - stats[j][1] - stats[j][4])+"       |      "+str(stats[j][3] -stats[j][1])+"   ]")
        print(tempstr)                                                                                    #calculate and print out stats for each program
        temp.append(stats[j][0])
        temp.append(stats[j][2] - stats[j][1])
        temp.append(stats[j][3] - stats[j][1])
        num.append(temp)

    print('\nGantt Chart is:')
    for k in range(len(gantt)):
        print(gantt[k])                                                                                     #print each element in gantt
    totalWaitTime = 0
    totalTurnTime = 0
    for m in range(len(num)):
        totalWaitTime = totalWaitTime + num[m][1]                                                           #add up all total wait and turnaround times 
        totalTurnTime = totalTurnTime + num[m][2]
    print('Average Waiting Time: ',str(totalWaitTime/len(num)))
    print('Average Turnaround Time:', str(totalTurnTime/len(num)))                                          #print out adv times and throughtput
    print('Throughput:', str(len(num)/currtime),'\n \n')

def SJFP(data):                                                                                             #SJF method
    burst = []
    for i in range(len(data)):                                                                              #add burst to subract from to get remaining time
        burst.append(data[i][2])
    for i in range(len(data)):
        data[i].append(data[i][2])
    gantt = []
    stats = []                                                                                              #initilize varibles
    help = [0]*len(data)
    q = []
    last =0
    count = 0
    processCount = 0
    PID =0
    print('----------------- SJFP -----------------')                                                          #print beginning statements
    print('Process ID | Waiting Time | Turnaround Time')
    currtime = 0
    
    while(True):
            for i in range(len(data)):
                if (data[i][1] == currtime and data[i] not in q):
                    q.append(data[i])
                    q.sort(key=lambda x: x[2])                                                              #sort by ramining time and make lowest PID next in q 
                    for i in range(5):
                        for j in range( len(info)-1):
                             if (info[j][1] == info[j+1][2] and info[j][0] > info[j+1][0]):
                               swap = info[j]
                               info[j] = info[j+1]
                               info[j+1] = swap
            if (processCount == len(data)):                                                                    #done if done processes is same as len of data
              break
            elif (len(q) == 0):                                                                                #if nothing in q IDLE
               tempstr = ("[   "+str(currtime)+"   ]-- IDLE--[   "+str(data[processCount+1][1]-1)+"   ]")
               gantt.append(tempstr)
               q.append(data[processCount])
               currtime = currtime + q[0][1] - currtime
               last = q[0]                                                                                      #set last to next item in q
            elif(q[0]==last or last ==0):                                                                       #checks to see if it was the same process as last time or idle last time
               PID = int (q[0][0]) -1
               count = count +1
               timeLeft = q[0][2]
               timeLeft = timeLeft - 1                                                                          #change time left to time left-1 to chek and see if a new process came
               q[0][2] = timeLeft
               last = q[0]
               currtime = currtime +1                                                                            #increase time that has gone by 
               if(q[0][2] == 0):                                                                                 #check and see if time remaining is 0 because that means that process is done 
                       

                         tempstr = ("[   "+ str(currtime - count)+"   ]--  "+str(q[0][0])+"  --[   "+str(currtime)+"   ]")
                         gantt.append(tempstr)                                                                     #add string showing how long the process went on for
                         PIDi = -1

                         for p in range(len(data)):
                             if (data[p][0] == PID+1):                                                              #find where in data correspodning PID is to gather info
                                 PIDi = p
                         temp = []
                         temp.append(data[PIDi][0])                                                                 #add stats for the done process to calculate waiting and turnaround times later 
                         temp.append(data[PIDi][1])
                         temp.append(int(currtime - count))
                         temp.append(currtime)
                         temp.append(burst[PIDi])
                         stats.append(temp)
                         processCount = processCount + 1                                                            #increase done process count 
                         del q[0]
                         count = 0
               for t in range(len(data)):
                   if(data[t][1]==currtime and data[t][2] < q[0][2]):                                               #checks to see if this process will be running again print if not 
                        tempstr = ("[   "+ str((currtime) - count)+"   ]--  "+str(q[0][0])+"  --[   "+str(currtime)+"   ]")
                        if(help[PID]==0):
                            help[PID] = currtime - count
                        count = 0
                        gantt.append(tempstr)
            else:

                last = q[0]                                                                                          #if nothing else set last equal to fist item in q to avoid inf. loop
    stats.sort(key=lambda x: x[0])                                                                                    #sort stats by PID
    advWait = 0
    advTurn = 0
    for j in range(len(stats)):
        tempstr = ("      "+ str(stats[j][0])+"    |      "+str(stats[j][3] -stats[j][1]- stats[j][4])+"       |      "+str(stats[j][3] -stats[j][1])+"   ]")
        advWait = advWait + stats[j][3] -stats[j][1]- stats[j][4]                                                     #print out correct times and add to total waittime to find adv
        advTurn = advTurn + stats[j][3] -stats[j][1]
        print(tempstr)
    print('\nGantt Chart is:')
    for k in range(len(gantt)):
        print(gantt[k])                                                                                                #print each item in ghantt list 
    
    print('Average Waiting Time: ',advWait/len(data))                                                                   #print wait time over len of data for find adv same for turnaround time
    print('Average Trunaround Time: ',advTurn/len(data))
    print('Throughput: ', len(data)/currtime, '\n \n')

def RR(data, t):                                                                                                        #Start of Round Robin method
    tq =int(t)
    burst = []                                                                                                          #get copy of burst to decresee the time 
    for i in range(len(data)):
        burst.append(data[i][3])
    gantt = []
    stats = []                                                                                                          #initilize varibles 
    help = [0]*len(data)
    finished =[]
    q = []
    currtime = 0
    temp = []
    while(True):                                                                                                        #go until finihsed break out of loop
         for i in range(len(data)):                                                                             
                if (data[i][1] == currtime and data[i] not in q):
                    temp.append(data[i])
                    temp.sort(key=lambda x: x[1])                                                                        #sort by arival time and PID 

         while(len(temp)!=0):
               q.insert(0,( temp[len(temp)-1]))                                                                            #add in reverse order to make sure lowest PID for that time is 1st
               temp.pop()
         if(len(q) ==1 and len(finished) == len(data)-1):                                                                   #if only 1 process left finishe it ignorint the time quantum
              currs = str(currtime) 
              ftime = currtime+q[0][3]
              tempstr = ("[   "+ str((currs))+"   ]--  "+str(q[0][0])+"  --[   "+str(ftime)+"   ]")                     #add string showing completion
              gantt.append(tempstr)
              PIDi = 0
              PID = q[0][0]
              for p in range(len(data)):
                             if (data[p][0] == PID):
                                 PIDi = p
              tempstats = []
              tempstats.append(data[PIDi][0])                                                                               #add stats to calulate thing later
              tempstats.append(data[PIDi][1])
              tempstats.append(int(currtime))
              tempstats.append(int(currtime + q[0][3]))
              tempstats.append(burst[PIDi])
              stats.append(tempstats)
              currtime = currtime + q[0][3]
              break                                                                                                         #break out of inf. loop
         elif(len(q)==0):                                                                                                   #if q is empty then IDLE
              currs = str(currtime) 
              ftime = data[len(finished)][1]
              tempstr = ("[   "+str(currs)+"   ]-- IDLE--[   "+str(ftime)+"   ]")
              gantt.append(tempstr)
              x = len(finished)
              currtime =  data[len(finished)][1]
              q.append(data[len(finished)])
         elif(int(q[0][3])<=int(t)):                                                                                        #if time quantum is greater or equal to remaing time then process will be complete
             currs = str(currtime) 
             x = currtime
             ftime = currtime+q[0][3]                                                                                       #create sting to show what happened 
             tempstr = ("[   "+ str((currs))+"   ]--  "+str(q[0][0])+"  --[   "+str(ftime)+"   ]")
             gantt.append(tempstr)                                                                                          #add string to list
             PIDi = 0
             PID = q[0][0]
             for p in range(len(data)):
                             if (data[p][0] == PID):
                                 PIDi = p
             tempstats = []
             tempstats.append(data[PIDi][0])                                                                                   #add to stats to find waiting time and turnaorund time later
             tempstats.append(data[PIDi][1])
             tempstats.append(int(currtime))
             tempstats.append(int(currtime + q[0][3]))
             tempstats.append(burst[PIDi])
             stats.append(tempstats)


             currtime = currtime + q[0][3]                                                                              #increse current time and add to finished q and delete from real q 
             finished.append(q[0])
             del q[0]

             for i in range(len(data)):
                 for j in range (x,currtime):
                    if (data[i][1] == j and data[i] not in q and data[i] not in finished):                               #check to see if a process arived durring the time quantum 
                     temp.append(data[i])
                     temp.sort(key=lambda b: b[1])

         elif(int(q[0][3])>int(t)):                                                                                        #cif remaing time is greater than time quantum will need to add to q again
             currs = str(currtime)
             ftime = (currtime + t)
             tempstr = ("[   "+ str((currs))+"   ]--  "+str(q[0][0])+"  --[   "+str(ftime)+"   ]")
             gantt.append(tempstr)                                                                                          #create and add strig telling what happended 
             x = currtime
             currtime = currtime + t                                                                                    #increse current time bassed of time qunatum 
             q[0][3] = int(q[0][3]-t)
             q.append(q[0])                                                                                             #reduce time remaining and add to back of list 
             del q[0]                                                                                                   #delete from frount of list

             for i in range(len(data)):         
                 for j in range (x,currtime):
                    if (data[i][1] == j and data[i] not in q and data[i] not in finished):                               #checks to see if process arived durring the time it took to complete this processs
                     temp.append(data[i])
                     temp.sort(key=lambda b: b[1])

    print('----------------- Round Robin -----------------')
    print('Process ID | Waiting Time | Turnaround Time')                                                                #print intial things 
    stats.sort(key=lambda b: b[0])                                                                                      #sort stats by PID
    advWait = 0
    advTurn = 0
    for j in range(len(stats)):
        tempstr = ("      "+ str(stats[j][0])+"    |      "+str(stats[j][3] -stats[j][1]- stats[j][4])+"       |      "+str(stats[j][3] -stats[j][1])+"   ]")
        advWait = advWait + stats[j][3] -stats[j][1]- stats[j][4]                                                        #add waitime and turnaround time of each process up 
        advTurn = advTurn + stats[j][3] -stats[j][1]
        print(tempstr)                                                                                                    #print the valuse for this PID
    print('\nGantt Chart is:')
    for k in range(len(gantt)):                                                                                         #print out gantt chart
        print(gantt[k])
    
    print('\nAverage Waiting Time: ',advWait/len(data))                                                                    #find adv wait and turnaround times 
    print('Average Trunaround Time: ',advTurn/len(data))
    print('Throughput: ', len(data)/currtime, '\n \n')





numarg =(len(sys.argv))
if(numarg !=3):
    print('\nIncorrect number of args. Only include file name and time quantum\n')
    quit()
array=[]                                                                                                                    #start of main
                                                                                                                            #initlizlize varibles
info=[]
count =0
with open(sys.argv[1], 'r') as f:                                                                                           #open file and read lines
    while True:
        line = f.readline()
        if not line:
            break
        array.append(line.split(','))                                                                                       #seperate by ,
        count = count +1                                                                                                    #count the lines
        if not line:
            break
del array[0]
for i in range( len(array)):
    testing=[]
    for j in range ( len(array[i])):
        z = array[i][j]                                                                                                     #converting char to int 
        if(z != '\n'):                                                                                                      #but leave it if its null
         temp = int(z)
         temp =int( array[i][j])                                                                                             #convert from chars to ints 
         testing.append(temp)                                                                                                #put in an array 
        if(j==2):
            info.append(testing)
info.sort(key=lambda x: x[1])                                                                                               #sort array by arival time
for i in range(5):
    for i in range( len(info)-1):
      if (info[i][1] == info[i+1][1] and info[i][0] > info[i+1][0]):                                                        #checks to see if same arival time and swap if needed 
         swap = info[i]
         info[i] = info[i+1]
         info[i+1] = swap

tq= int (sys.argv[2])                                                                                                       #converts the time quantum arg to int from char
FCFS(info)                                                                                                                  #calls the 3 schedulaing methods 
SJFP(info)
RR(info,tq)

