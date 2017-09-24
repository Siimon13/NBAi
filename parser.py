import csv
import json

DIR = "json/"

def csvToJson(filename):
    json_write = []
    impHeaders = []
    csvWriter = []
    playerMap = {}
    teamMap = {}
    
    with open("Team_Map.csv","r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvreader.next()

        for r in csvreader:
            teamMap[r[1]] = r[4]
        
    
    with open("Player_Map.csv","r") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        csvreader.next()

        for r in csvreader:
            playerMap[r[0]] = r[2]
            
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        headers = csvreader.next()
        included_cols = [7, 8, 9, 10, 11, 14, 15, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 29, 25, 24, 23, 19, 20]

        impHeaders = list(headers[i] for i in included_cols)
        for r in csvreader:
            if len(r) != 40:
                print r
                continue

            for i in range(len(r)):
                if playerMap.get(r[i]) and i != 14 and i != 25 and i != 11 and i != 19 and i != 20:
                    r[i] = playerMap[r[i]]

                if teamMap.get(r[i]):
                    r[i] = teamMap[r[i]]

            content = list(r[i] for i in included_cols)
            csvWriter.append(content)

    with open("scrapped.csv", "w") as writefile:
        filewriter = csv.writer(writefile, delimiter=',')
        filewriter.writerow(impHeaders)
        for r in csvWriter:
            print ("writing")
            filewriter.writerow(r)
                
        
csvToJson('Play_by_Play.csv')
