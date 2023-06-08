#FCFS
def findWaitingTime1(processes, n, bt, wt):
    wt[0] = 0
    for i in range(1, n ):
        wt[i] = bt[i - 1] + wt[i - 1]
def findTurnAroundTime1(processes, n, bt, wt, tat):
        for i in range(n):
            tat[i] = bt[i] + wt[i]
def findavgTime1( processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    findWaitingTime1(processes, n, bt, wt)
    findTurnAroundTime1(processes, n, bt, wt, tat)
    print( "Processes Burst time " +" Waiting time " +" Turn around time")
    for i in range(n):     
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(" " + str(i + 1) + "\t\t" +str(bt[i]) + "\t " +str(wt[i]) + "\t\t " +str(tat[i])) 
    print( "Average waiting time = "+str(total_wt / n))
    print("Average turn around time = "+str(total_tat / n))

if __name__ =="__main__":
    processes = [ 1, 2, 3]
    n = len(processes)
    burst_time = [10, 5, 8]
    findavgTime1(processes, n, burst_time)

#priority
def findWaitingTime(processes, n, wt):
	wt[0] = 0
	for i in range(1, n):
		wt[i] = processes[i - 1][1] + wt[i - 1]
def findTurnAroundTime(processes, n, wt, tat):
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]
def findavgTime(processes, n):
	wt = [0] * n
	tat = [0] * n
	findWaitingTime(processes, n, wt)
	findTurnAroundTime(processes, n, wt, tat)
	print("\nProcesses Burst Time Waiting","Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",processes[i][1], "\t\t",wt[i], "\t\t", tat[i])
	print("\nAverage waiting time = %.5f "%(total_wt /n))
	print("Average turn around time = ", total_tat / n)
def priorityScheduling(proc, n):
	proc = sorted(proc, key = lambda proc:proc[2],reverse = True);
	print("Order in which processes gets executed")
	for i in proc:
		print(i[0])
	findavgTime(proc, n)
	
if __name__ =="__main__":
	proc = [[1, 10, 1],[2, 5, 0],[3, 8, 1]]
	n = 3
	priorityScheduling(proc, n)
    
    #round robin
def findWaitingTime(processes, n, bt,wt, quantum):
	rem_bt = [0] * n
	for i in range(n):
		rem_bt[i] = bt[i]
	t = 0 # Current time
	while(1):
		done = True
		for i in range(n):
			if (rem_bt[i] > 0) :
				done = False # There is a pending process				
				if (rem_bt[i] > quantum) :
					t += quantum
					rem_bt[i] -= quantum
				else:
					t = t + rem_bt[i]
					wt[i] = t - bt[i]
					rem_bt[i] = 0
		if (done == True):
			break
def findTurnAroundTime(processes, n, bt, wt, tat):
	for i in range(n):
		tat[i] = bt[i] + wt[i]
def findavgTime(processes, n, bt, quantum):
	wt = [0] * n
	tat = [0] * n
	findWaitingTime(processes, n, bt,wt, quantum)
	findTurnAroundTime(processes, n, bt,wt, tat)
	print("Processes Burst Time	 Waiting","Time Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", i + 1, "\t\t", bt[i],
			"\t\t", wt[i], "\t\t", tat[i])
	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = %.5f "% (total_tat / n))
	
if __name__ =="__main__":
	proc = [1, 2, 3]
	n = 3
	burst_time = [10, 5, 8]
	quantum = 2;
	findavgTime(proc, n, burst_time, quantum)

#SJF
def findWaitingTime2(processes, n, wt):
	rt = [0] * n
	for i in range(n):
		rt[i] = processes[i][1]
	complete = 0
	t = 0
	minm = 999999999
	short = 0
	check = False
	while (complete != n):
		for j in range(n):
			if ((processes[j][2] <= t) and
				(rt[j] < minm) and rt[j] > 0):
				minm = rt[j]
				short = j
				check = True
		if (check == False):
			t += 1
			continue
		rt[short] -= 1
		minm = rt[short]
		if (minm == 0):
			minm = 999999999
		if (rt[short] == 0):
			complete += 1
			check = False
			fint = t + 1
			wt[short] = (fint - proc[short][1] -proc[short][2])
			if (wt[short] < 0):
				wt[short] = 0
		t += 1
def findTurnAroundTime2(processes, n, wt, tat):
	for i in range(n):
		tat[i] = processes[i][1] + wt[i]
def findavgTime2(processes, n):
	wt = [0] * n
	tat = [0] * n
	findWaitingTime2(processes, n, wt)
	findTurnAroundTime2(processes, n, wt, tat)
	print("Processes Burst Time	 Waiting","Time	 Turn-Around Time")
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" ", processes[i][0], "\t\t",processes[i][1], "\t\t",wt[i], "\t\t", tat[i])
	print("\nAverage waiting time = %.5f "%(total_wt /n) )
	print("Average turn around time = ", total_tat / n)
	
if __name__ =="__main__":
	proc = [[1, 6, 1], [2, 8, 1], [3, 7, 2], [4, 3, 3]]
	n = 4
	findavgTime2(proc, n)

    
