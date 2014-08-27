#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Name:PlayerDatabase.py
#Purpose: A program that will allow the user to add players to a temporary database
#
#Author: Mamujee. D
#
#Created: 16/01/2014
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time
import random
#Class that stores players in a database
class playerDatabase():
    def __init__(self,playerFirstName,playerLastName,playerAge,playerNum,playerPosition,seasonsPlayed,playerCode,dateAdded = ""):
        #Encapsulates all fields
        self.__playerFirstName = playerFirstName
        self.__playerLastName = playerLastName
        self.__playerAge = playerAge
        self.__playerNum = playerNum
        self.__playerPosition = playerPosition
        self.__seasonsPlayed = seasonsPlayed
        self.__playerCode = playerCode
        self.__dateAdded = time.strftime("%m/%d/%Y")
        #Appends player details to file
        file = open("player_Database.dat","a")
        file.write("\n{0:<20}{1:<20}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format(playerLastName,playerFirstName,playerNum,playerAge,playerPosition,seasonsPlayed,self.__dateAdded,playerCode))
        file.close()
        
    #Methods that returns emcapsulated field
    def getPlayerFirstName(self):
        return self.__playerFirstName
    def getPlayerLastName(self):
        return self.__playerLastName
    def getPlayerAge(self):
        return self.__playerAge
    def getPlayerNum(self):
        return self.__playerNum
    def getPlayerPosition(self):
        return self.__playerPosition
    def getSeasonsPlayed(self):
        return self.__seasonsPlayed
    def getDateAdded(self):
        return self.__dateAdded
    def getPlayerCode(self):
        return self.__playerCode
    
#All of the miscellaneous functions are sorted alphabetically


#Function that asks for password from user, to ensure they have authorization to delete players. Password is "hockey"
def deletePasswordCheck():
    counter = 0
    Input = input("Please enter password to delete players: ")
    while Input != "hockey":
        Input = input("Incorrect password. Please try again: ")
        counter += 1
        if Input == "hockey":
            break
        #If user fails three times, acces denied, and retunr to main menu
        if counter > 1:
            print("Too many invalid entries. Returning to main menu")
            mainMenu()
    if Input == "hockey":
        print("Correct Password. Access Granted")
        
#Function that will delete a player from the database  
def deletePlayer(tempObjectList):
    #Asks user to choose which player to delete
    Input2 = input("Please enter the number at beginning of row which corresponds with player to delete: ")
    #Checks that user enters valid number
    while intCheck(Input2) == False:
        Input2 = input("Invalid Input. please enter corresponding number: ")
    Input2 = int(Input2)
    
    while Input2 < 0 or Input2 > len(tempObjectList):
        Input2 = input("Invalid Input. Please enter corresponding number: ")
        while intCheck(Input2) == False:
            Input2 = input("Invalid Input. Please enter corresponding number: ")
        Input2 = int(Input2)
        
    while Input2 > 0 and Input2 <= len(tempObjectList):
        #Prints player in table for user to confirm deletion
        tempObjectList1 = [tempObjectList[Input2-1]]
        tableOutput(tempObjectList1)
        Input3 = input("Are you sure you want to delete this player? (Y/N): ")
        
        while Input3 != "Y" and Input3 != "N":
            Input3 = input("Invalid input. Please choose yes or no (Y/N): ")
        if Input3 == "Y":
            #Deletes player from object list and from dictionary
            del dictionary[tempObjectList[Input2-1]]
            objectList.remove(tempObjectList[Input2-1])
            print("Player has been deleted from the database")
            #Rewrites all players to file without deleted player
            file = open("player_Database.dat","w")
            file.write("{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format("Last Name","First Name", "Number", "Age", "Position", "Seasons Played", "Date Added", "Player Code"))
            for i in objectList:
                file.write("\n{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format(dictionary[i].getPlayerLastName(),dictionary[i].getPlayerFirstName(),dictionary[i].getPlayerNum(),dictionary[i].getPlayerAge(),dictionary[i].getPlayerPosition(),dictionary[i].getSeasonsPlayed(),dictionary[i].getDateAdded(),i))
            file.close()  
            mainMenu()
            
        #If user doesn't want to delete player, returns to main menu
        if Input3 == "N":
            mainMenu()
        
#This function checks to see if the given string is in the given list
def duplicateCheck(List,temp):
    for item in List:
        if temp == item:
            return False
        else:
            continue
    return True
    
#Recursive function that searches through database by First Name
def firstNameSearch(Input,List = [],i = 0):
    if i == len(objectList):
        return List
    else:
        if Input == dictionary[objectList[i]].getPlayerFirstName():
            List.append(objectList[i])
        return firstNameSearch(Input,List,i+1)

#This function checks to see if a variable is a number
def intCheck(num): 
    try:
        float(num)
    except ValueError:
        return False
    else:
        return True
#Recursive function that searches through all players in database by Last Name.
def lastNameSearch(Input,List = [],i = 0):
    if i == len(objectList):
        return List
    else:
        if Input == dictionary[objectList[i]].getPlayerLastName():
            List.append(objectList[i])
        return lastNameSearch(Input,List,i+1)

#Recursive function that returns total season played of all players in database
def listTotal(tempObjectList,counter = 0):
    if tempObjectList == []:
        return 0
    if counter == len(tempObjectList)-1:
        return int(dictionary[objectList[counter]].getSeasonsPlayed())
    else:
        return int(dictionary[objectList[counter]].getSeasonsPlayed()) + listTotal(tempObjectList, counter + 1)

#The main menu of program    
def mainMenu():
    #Sorts the objectList, so that it is sorted by last name by default
    objectList.sort()
    userInput = input("\nMAIN MENU:\n1. Add a new player\n2. Delete a player\n3. View players\n4. Search for players\n5. Calculate average and total seasons played by all players in database\n6. Exit\nChoose a number to do an action: ")
    #While loop that checks that input is valid
    while userInput != "1" and userInput != "2" and userInput != "3" and userInput != "4" and userInput != "5" and userInput != "6":
            userInput = input("Invalid Input. Please enter valid digit: ")        
    if userInput == "1":
        playerCreation()    
    elif userInput == "2":
        playerDeletion()
    elif userInput == "3":
        sort()
    elif userInput == "4":
        search()
    elif userInput == "5":
        seasonsTotal()
    elif userInput == "6":
        exit()

#A function that sorts list by merge sort
def mergeSort(List):      #Source: http://stackoverflow.com/questions/18761766/mergesort-python
    result = []
    if len(List) < 2:
        return List
    mid = int(len(List)/2)
    y = mergeSort(List[:mid])
    z = mergeSort(List[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result

#Recursive function that searches throuhg database by number    
def numberSearch(Input,List = [],i = 0):
    if i == len(objectList):
        return List
    else:
        if Input == dictionary[objectList[i]].getPlayerNum():
            List.append(objectList[i])
        return numberSearch(Input,List,i+1)
    
def partition(numList, start, end, stringList):     #Source: http://www.pythonschool.net/algorithms_quickSort/
    pivot = numList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and numList[left] <= pivot:
            left = left + 1
        while numList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=numList[left]
            temp1 = stringList[left]
            numList[left]=numList[right]
            stringList[left]=stringList[right]
            numList[right]=temp
            stringList[right]=temp1
    # swap start with myList[right]
    temp=numList[start]
    temp1 = stringList[start]
    numList[start]=numList[right]
    stringList[start]=stringList[right]
    numList[right]=temp
    stringList[right]=temp1
    return right

def quickSort(numList, start, end, stringList):      #Source: http://www.pythonschool.net/algorithms_quickSort/
    if start < end:
        # partition the list
        pivot = partition(numList, start, end, stringList)
        
        # sort both halves
        quickSort(numList, start, pivot-1, stringList)
        quickSort(numList, pivot+1, end, stringList)
    return stringList

#A function that is used in the search() function that will give the user the option to delete a player from the search results
def searchDelete(tempList):
    tableOutput(tempList)
    #User is given option to return to delete one of the players, or to return ot the main menu
    Input2 = input("Would you like to:\n1. Delete a player in this list\n2. Return to the main menu\nPlease enter digit for your choice: ")
    while Input2 != "1" and Input2 != "2":
        Input2 = input("Invalid Input. Please enter valid digit: ")
        #If user wants to delete player, delete functions are run
    if Input2 == "1":
        deletePasswordCheck()
        deletePlayer(tempList)
    if Input2 == "2":
        mainMenu()

#This method checks to see if any part of variable is not alphabetic
def stringCheck(string):
    string = string.replace("-", "")
    i = 0
    try: len(string)
    except TypeError:
        return False
    else:
        while i < len(string):
            if string[i].isalpha() == True:
                i += 1
            else:
                return False
        return True

#Outputs passed list in a table
def tableOutput(tempObjectList):
    #Labels the top row with column titles
    print("{0:<4}{1:<20}{2:<20}{3:<9}{4:<6}{5:<12}{6:<18}{7:<0}".format("#","Last Name","First Name", "Number", "Age", "Position", "Seasons Played", "Date Added"))
    print("-"*100)
    counter = 0
    for i in tempObjectList:
        counter += 1
        print("{0:<4}{1:<20}{2:<20}{3:<9}{4:<6}{5:<12}{6:<18}{7:<0}".format(str(counter) + ".",dictionary[i].getPlayerLastName(),dictionary[i].getPlayerFirstName(),dictionary[i].getPlayerNum(),dictionary[i].getPlayerAge(),dictionary[i].getPlayerPosition(),dictionary[i].getSeasonsPlayed(),dictionary[i].getDateAdded()))
    print("\n")

#Now these are all of the functions that are the main functions thar are redirected to from the main menu
#Function that creates a new player for the database
def playerCreation():
    #For each field, it asks for the info from the user, then temporarily stores it as variable
    playerFirstName = input("Please enter the player's first name: ")
    #Then checks to see if input it valid
    while stringCheck(playerFirstName) == False or intCheck(playerFirstName) == True or playerFirstName == "":
        playerFirstName = input("Invalid Name. Please enter first name: ")
    #Makes first letter uppercase, for sorting later
    playerFirstName = playerFirstName[0].upper() + playerFirstName[1:]
           
    playerLastName = input("Please enter the player's last name: ")
    while stringCheck(playerLastName) == False or intCheck(playerLastName) == True or playerLastName == "":
        playerLastName = input("Invalid Name. Please enter last name: ")
    playerLastName = playerLastName[0].upper() + playerLastName[1:]
        
    playerAge = input("Please enter the player's age: ")
    while intCheck(playerAge) == False or playerAge == "":
        playerAge = input("Invalid age. Please enter age in digits: ")         
    #If player is older than 17, then they are classified as an adult
    adult = False
    if int(playerAge) > 17:
        adult = True
        
    playerNum = input("Please enter the player's number: ")
    while intCheck(playerNum) == False or playerNum == "":
        playerNum = input("Invalid number. Please enter number in digits: ")      

    playerPosition = input("Please enter the player's position (Player or Goalie): ")
    while playerPosition != "Player" and playerPosition != "Goalie":
        playerPosition = input("Invalid Input. Please enter position as either Player or Goalie: ")

    seasonsPlayed = input("Please enter how many seasons the player has played: ")
    while intCheck(seasonsPlayed) == False or seasonsPlayed == "":
        seasonsPlayed = input("Invalid value. Please enter seasons played in digits: ")

    #Generates random four digit integer
    randomInt = str(random.randint(1000,9999))
    #Creates player code for player
    playerCode = playerLastName + playerFirstName + randomInt
    if playerPosition == "Player":
        playerCode = playerCode + "P"
    else:
        playerCode = playerCode + "G"
    if adult == True:
        playerCode = playerCode + "A"
    #Checks that there isn't already a player with the same player code
    while duplicateCheck(objectList,playerCode) == False:
        #If player code is a duplicate, new player code is generated
        randomInt = str(random.randint(1000,9999))
        playerCode =  playerLastName + playerFirstName + randomInt
        if playerPosition == "Player":
            playerCode = playerCode + "P"
        else:
            playerCode = playerCode + "G"
        if adult == True:
            playerCode = playerCode + "A"
    #Player code is added to the object list    
    objectList.append(playerCode)
    #Object is created and is stored in dictionary
    dictionary[playerCode] = playerDatabase(playerFirstName,playerLastName,playerAge,playerNum,playerPosition,seasonsPlayed,playerCode)
    print("Player entered into database.")
    #Returns to main menu
    mainMenu()

    
#Function that will ask for specific details of player to delete
def playerDeletion():
    #If no players in database, returns to main menu
    if objectList == []:
        print("There are no players in the database to delete ")
        mainMenu()
    #Runs function that asks for deletion password, which is "hockey"
    deletePasswordCheck()
    #Asks for details of desired player from user        
    lastName = input("Please enter last name of player to delete: ")
    while stringCheck(lastName) == False or intCheck(lastName) == True or lastName == "":
        lastName = input("Invalid Name. Please enter last name to delete: ")
    lastName = lastName[0].upper() + lastName[1:]
    firstName = input("Please enter first name of player to delete: ")
    while stringCheck(firstName) == False or intCheck(firstName) == True or firstName == "":
        firstName = input("Invalid Name. Please enter first name to delete: ")
    firstName = firstName[0].upper() + firstName[1:]
    number = input("Please enter number of player to delete: ")
    while intCheck(number) == False or number == "":
        number = input("Invalid age. Please enter age for deletion in digits: ")
    #Check from object list for each detail from user for the player
    tempObjectList = []
    for i in objectList:
        if dictionary[i].getPlayerLastName() == lastName:
            tempObjectList.append(i)
        else:
            continue
    tempObjectList1 = []
    for i in tempObjectList:
        if dictionary[i].getPlayerFirstName() == firstName:
            tempObjectList1.append(i)
        else:
            continue
    tempObjectList2 = []
    for i in tempObjectList1:
        if dictionary[i].getPlayerNum() == number:
            tempObjectList2.append(i)
        else:
            continue
    if tempObjectList2 == []:
        print("There are no players in the database with that information.")
        mainMenu()
    else:
        #What happens if only one player is found with given details
        if len(tempObjectList2) == 1:
            #Prints players in table and asks for deletion confirmation
            tableOutput(tempObjectList2)
            Input2 = input("Is this the player you want to delete? (Y/N): ")
            while Input2 != "Y" and Input2 != "N":
                Input2 = input("Invalid input. Please choose yes or no (Y/N): ")
            if Input2 == "Y":
                #Deletes player from object list and dictionary
                objectList.remove(tempObjectList2[0])
                del dictionary[tempObjectList2[0]]
                print("Player has been deleted from the database")
                mainMenu()
            if Input2 == "N":
                mainMenu()
        #What happens if more than one players have the given details
        else:
            tableOutput(tempObjectList2)
            deletePlayer(tempObjectList2)
            
    #Rewrites all players in database to file, without deleted player
    file = open("player_Database.dat","w")
    file.write("{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format("Last Name","First Name", "Number", "Age", "Position", "Seasons Played", "Date Added", "Player Code"))
    for i in objectList:
        file.write("\n{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format(dictionary[i].getPlayerLastName(),dictionary[i].getPlayerFirstName(),dictionary[i].getPlayerNum(),dictionary[i].getPlayerAge(),dictionary[i].getPlayerPosition(),dictionary[i].getSeasonsPlayed(),dictionary[i].getDateAdded(),i))
    file.close()    
    mainMenu()

#Method that will sort players in the database
def sort():
    if objectList == []:
        print("There are no players in the database to view. Returning to main menu")
        mainMenu()
    Input = input("Would you like to:\n1. View all players\n2. Sort by a property\nPlease enter digit for your choice: ")
    while Input != "1" and Input != "2":
        Input = input("Invalid Input. Please enter valid digit: ")
    if Input == "1":
        tableOutput(objectList)
        mainMenu()
        
    if Input == "2":
        #Asks users by which property to sort by
        Input2 = input("Would you like to sort by:\n1. Last Name\n2. First Name\n3. Age\n4. Number\n5. Position\n6. Seasons Played\nPlease enter digit for your choice: ")

        while Input2 != "1" and Input2 != "2" and Input2 != "3" and Input2 != "4" and Input2 != "5" and Input2 != "6":
            Input2 = input("Invalid Input. Please enter valid digit: ")
        #Sorts by Last Name
        if Input2 == "1":
            objectListCopy = objectList
            #Sorts list by merge sort, and prints it in table. Just the object List can be sorted, as it has the player code in it, which have the player's last name first
            tableOutput(mergeSort(objectListCopy))
            mainMenu()
            
        #Sorts by First Name            
        if Input2 == "2":
            #Initializes list for sorted items
            firstNameList = []
            objectListCopy = objectList
            #Puts all first names of players in a list
            for i in objectList:
                firstNameList.append(dictionary[i].getPlayerFirstName())
            #Sorts the players by first name
            output = quickSort(firstNameList,0,len(firstNameList)-1,objectListCopy)
            #Prints in table, then returns to main menu
            tableOutput(output)
            mainMenu()
            
        #Sorts by Age    
        if Input2 == "3":
            ageList = []
            objectListCopy = objectList
            for i in objectList:
                ageList.append(int(dictionary[i].getPlayerAge()))

            output = quickSort(ageList,0,len(ageList)-1,objectListCopy)
            tableOutput(output)
            mainMenu()

        #Sort by Number   
        if Input2 == "4":
            numList = []
            objectListCopy = objectList
            for i in objectList:
                numList.append(int(dictionary[i].getPlayerNum()))
            output = quickSort(numList,0,len(numList)-1,objectListCopy)
            tableOutput(output)
            mainMenu()

        #Sorts by Position
        if Input2 == "5":
            positionList = []
            objectListCopy = objectList
            for i in objectList:
                temp = dictionary[i].getPlayerPosition()
                #For players, it give a value of 0, and a value of 1 for goalies. Then when they get sorted, players will be above the goalies
                if temp == "Player":
                    positionList.append(0)
                if temp == "Goalie":
                    positionList.append(1)
            output = quickSort(positionList,0,len(positionList)-1,objectListCopy)
            tableOutput(output)
            mainMenu()
            
        #Sorts by Seasons Played
        if Input2 == "6":
            seasonsPlayedList = []
            objectListCopy = objectList
            for i in objectList:
                seasonsPlayedList.append(int(dictionary[i].getSeasonsPlayed()))
            output = quickSort(seasonsPlayedList,0,len(seasonsPlayedList)-1,objectListCopy)
            tableOutput(output)
            mainMenu()

    
#Function that will search for specific players in database from info given by user            
def search():
    tempList = []
    if objectList == []:
        print("There are no players in the database to search for. Returning to main menu")
        mainMenu()
    #Asks user what property to sort by
    Input = input("Would you like to search by:\n1. Last Name\n2. First Name\n3. Number\n4. View all players\nPlease enter digit for your choice: ")
    while Input != "1" and Input != "2" and Input != "3" and Input != "4":
        Input = input("Invalid Input. Please enter valid digit: ")
    #Searches for Last Name
    if Input == "1":
        Input1 = input("Please enter last name to search for: ")
        while stringCheck(Input1) == False or intCheck(Input1) == True or Input1 == "":
            Input1 = input("Invalid first name. Please enter last name for search: ")
        Input1 = Input1[0].upper() + Input1[1:]
        #Searches for players with given last name
        tempList = lastNameSearch(Input1,tempList)
        #If list is empty, then there are no players with that last name in database
        if tempList == []:
            Input2 = input("There are no players with that last name in the database.\n Would you like to:\n1. Search for another player or \n2. Return to the main menu\nPlease enter digit for your choice: ")
            while Input2 != "1" and Input2 != "2":
                Input2 = input("Invalid Input. Please enter valid digit: ")
            if Input2 == "1":
                search()
            else:
                mainMenu()
                
        #If there are players in list, user is given option to delete a player
        else:
            searchDelete(tempList)            
    #Searches for First Name        
    if Input == "2":
        Input1 = input("Please enter first name to search for: ")
        while stringCheck(Input1) == False or intCheck(Input1) == True or Input1 == "":
            Input1 = input("Invalid first name. Please enter first name for search: ")
        Input1 = Input1[0].upper() + Input1[1:]
        tempList = firstNameSearch(Input1,tempList)
        if tempList == []:
            Input2 = input("There are no players with that first name in the database.\n Would you like to:\n1. Search for another player or \n2. Return to the main menu\nPlease enter digit for your choice: ")
            while Input2 != "1" and Input2 != "2":
                Input2 = input("Invalid Input. Please enter valid digit: ")
            if Input2 == "1":
                search()
            else:
                mainMenu()
        else:
            searchDelete(tempList)
                
    #Searches for number    
    if Input == "3":
        Input1 = input("Please enter number to search for: ")
        while intCheck(Input1) == False or Input1 == "":
            Input1 = input("Invalid number. Please enter number for search: ") 
        tempList = numberSearch(Input1,tempList)
        if tempList == []:
            Input2 = input("There are no players with that number in the database.\n Would you like to:\n1. Search for another player or \n2. Return to the main menu\nPlease enter digit for your choice: ")
            while Input2 != "1" and Input2 != "2":
                Input2 = input("Invalid Input. Please enter valid digit: ")
            if Input2 == "1":
                search()
            else:
                mainMenu()
        else:
            searchDelete(tempList)
    #Prints all players
    if Input == "4":
        if objectList == []:
            print("There are no players in the database to print. Returning to main menu")
            mainMenu()
        else:
            tempList = objectList
            searchDelete(tempList)
            
   
#Function that will display total and average seasons played by all players in the database
def seasonsTotal():
    if objectList == []:
        print("There are no players entered into the database. Returning to main menu")
        mainMenu()
    #Finds seasons total from listTotal() function
    seasonsTotal = listTotal(objectList)
    if seasonsTotal == 0:
        print("There are no seasons played entered into the database.")
    else:
        print("Total seasons played by all players is " + str(seasonsTotal) + ". The average seasons played is " + str(seasonsTotal/len(objectList)))
    mainMenu()

#Initializes objectList and dictionary
objectList = []
dictionary = {}
#Writes the headings for the text file
file = open("player_Database.dat","w")
file.write("{0:<20}{1:<20}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format("Last Name","First Name", "Number", "Age", "Position", "Seasons Played", "Date Added", "Player Code"))
file.close()
#Goes to the main menu for the first time
mainMenu()
