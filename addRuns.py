import csv
from collections import deque

def calRuns():
    filename = "scrapped.csv"

    headers = []
    csvList = []
    
    with open(filename,"r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        headers = csvreader.next()
        headers.append("Run")
        headers.append("Team_In_Run")
        
        print headers
        curr_ind = headers.index('Team_Committing_Action')
        homepts_ind = headers.index('Home_PTS')
        visitpts_ind = headers.index('Visitor_PTS')
        time_ind = headers.index('Play_Clock_Time')
        pd_ind = headers.index('Period')
        shot_ind = headers.index('Shot_Value')
        
        team_In_Run = ""
        team_Dif = 0
        curr_pd = "1"
        isRun = False

        lst = deque()
        for i, r in enumerate(csvreader):

            curr_team = r[curr_ind]
            if curr_team == "0":
                r[curr_ind] = "None"
            homepts = r[homepts_ind]
            awaypts = r[visitpts_ind]
            time = r[time_ind]
            pd = r[pd_ind]
            shotval = int(r[shot_ind]) if curr_team == r[0] else int(r[shot_ind]) * -1

            
            if (pd != curr_pd):
                print ("Swap quarters")
                isRun = False
                curr_pd = pd
            elif(len(lst) > 10 and abs(shotval) != 0):
                print("Checking if run or nah")
                
                lst.popleft()
                lst.append(shotval)
                team_Dif = abs(sum(list(lst)))
                # print lst
                # print(team_Dif)
                # raw_input()
                
                if (team_Dif > 8):
                    isRun = True
                else:
                    isRun = False
                
            elif(abs(shotval) != 0):
                print("Need more items in list")
                
                lst.append(shotval)
                    
            r.append(isRun)
            r.append(team_In_Run)    
            csvList.append(r)
            
    with open("scrapped_withRuns.csv", "w") as writefile:
        filewriter = csv.writer(writefile, delimiter=',')
        filewriter.writerow(headers)
        for r in csvList:
            print ("writing")
            filewriter.writerow(r)
            

calRuns()

