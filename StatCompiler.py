# David Ertel
# 27/1/2023
# StatCompiler

import os, time

canRun = True
picking = True
teamsFolder = str(os.getcwd()) + '/TEAMS'
teamTable = []
fileTable = []
foundFolder = False

# Tony's code that returns all of the information in the file in one line
# (1 indexed because it is lined based

def extractData (filepath):
  with open(filepath, 'r') as doc:
    return "".join(doc.readlines()).split("\n")

# gets an array of all the folders

for path in os.walk(teamsFolder):
    
    for team in path[1]:
        teamTable.append(team)

for path in os.walk(str(teamsFolder + '/' + '446')):
  print(path)
  for file in path[2]:          
        fileTable.append(file)

# MAIN #################################################################################

while canRun:
    while picking:
        for i in teamTable: # prints out all of the teams
            print('> ', i)
            
        userInput = input('Enter a team name:\n')

        for i in teamTable: # iterates through the array with all the team names
            
            if str(userInput) == str(i): # if there is a match between the name and a folder name

                while picking:
                    
                            
                    for k in fileTable:
                        print('> ', k)
                        
                    userInput2 = input('Enter a data file name:\n')
                    
                    for i in fileTable: # iterates through the array with all the team names
            
                        if str(userInput2) == str(i): # if there is a match between the
                            foundFolder = True
                            folderDir = teamsFolder + '/' + str(userInput) + '/' + str(userInput2) # saves the folderDir to be inputted as one string
                            print(extractData(folderDir))
                            break
                        
                    
            
        if not foundFolder: # if the program coudn't find the folder
            print('Unable to find folder.')
            
            time.sleep(1) # waits for 1 second and then the screen clears
            os.system('cls')
            
    picking = True # resets the picking boolean for the next iteration
    
    time.sleep(1) # waits for 1 second and then the screen clears
    os.system('cls')
