# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Name:PlayerDatabase.py
# Purpose: A program that will allow the user to add players to a temporary database
#
# Author: Mamujee. D
#
# Created: 16/01/2014
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import time
import random


# Class that stores players in a database
class PlayerDatabase:
    def __init__(self, player_first_name, player_last_name, player_age, player_num,
                 player_position, seasons_played, player_code,):
        # Encapsulates all fields
        self.__playerFirstName = player_first_name
        self.__playerLastName = player_last_name
        self.__playerAge = player_age
        self.__playerNum = player_num
        self.__playerPosition = player_position
        self.__seasonsPlayed = seasons_played
        self.__playerCode = player_code
        self.__dateAdded = time.strftime("%m/%d/%Y")
        # Appends player details to file
        temp_file = open("player_Database.dat", "a")
        temp_file.write("\n{0:<20}{1:<20}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format(
            player_last_name, player_first_name, player_num, player_age,
            player_position, seasons_played, self.__dateAdded, player_code))
        temp_file.close()

    # Methods that returns encapsulated field
    def get_player_first_name(self):
        return self.__playerFirstName

    def get_player_last_name(self):
        return self.__playerLastName

    def get_player_age(self):
        return self.__playerAge

    def get_player_num(self):
        return self.__playerNum

    def get_player_position(self):
        return self.__playerPosition

    def get_seasons_played(self):
        return self.__seasonsPlayed

    def get_date_added(self):
        return self.__dateAdded

    def get_player_code(self):
        return self.__playerCode


# All of the miscellaneous functions are sorted alphabetically


# Function that asks for password from user, to ensure they have authorization to delete players. Password is "hockey"
def delete_password_check():
    counter = 0
    user_input = input("Please enter password to delete players: ")
    while user_input != "hockey":
        user_input = input("Incorrect password. Please try again: ")
        counter += 1
        if user_input == "hockey":
            break
        # If user fails three times, acces denied, and retunr to main menu
        if counter > 1:
            print("Too many invalid entries. Returning to main menu")
            main_menu()
    if user_input == "hockey":
        print("Correct Password. Access Granted")


# Function that will delete a player from the database
def delete_player(temp_object_list):
    # Asks user to choose which player to delete
    input2 = input("Please enter the number at beginning of row which corresponds with player to delete: ")
    # Checks that user enters valid number
    while not int_check(input2):
        input2 = input("Invalid Input. please enter corresponding number: ")
    input2 = int(input2)

    while input2 < 0 or input2 > len(temp_object_list):
        input2 = input("Invalid Input. Please enter corresponding number: ")
        while not int_check(input2):
            input2 = input("Invalid Input. Please enter corresponding number: ")
        input2 = int(input2)

    while 0 < input2 <= len(temp_object_list):
        # Prints player in table for user to confirm deletion
        tempobjectlist1 = [temp_object_list[input2 - 1]]
        table_output(tempobjectlist1)
        input3 = input("Are you sure you want to delete this player? (Y/N): ")

        while input3 != "Y" and input3 != "N":
            input3 = input("Invalid input. Please choose yes or no (Y/N): ")
        if input3 == "Y":
            # Deletes player from object list and from dictionary
            del dictionary[temp_object_list[input2 - 1]]
            object_list.remove(temp_object_list[input2 - 1])
            print("Player has been deleted from the database")
            # Rewrites all players to file without deleted player
            given_file = open("player_Database.dat", "w")
            given_file.write(
                "{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format("Last Name", "First Name", "Number",
                                                                                 "Age", "Position", "Seasons Played",
                                                                                 "Date Added", "Player Code"))
            for i in object_list:
                given_file.write("\n{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format(
                    dictionary[i].get_player_last_name(), dictionary[i].get_player_first_name(),
                    dictionary[i].get_player_num(),
                    dictionary[i].get_player_age(), dictionary[i].get_player_position(),
                    dictionary[i].get_seasons_played(),
                    dictionary[i].get_date_added(), i))
            given_file.close()
            main_menu()

        # If user doesn't want to delete player, returns to main menu
        if input3 == "N":
            main_menu()


# This function checks to see if the given string is in the given list
def duplicate_check(given_list, temp):
    for item in given_list:
        if temp == item:
            return False
        else:
            continue
    return True


# Recursive function that searches through database by First Name
def first_name_search(given_input, given_list=None, i=0):
    if not given_list:
        given_list = []
    if i == len(object_list):
        return given_list
    else:
        if given_input == dictionary[object_list[i]].get_player_first_name():
            given_list.append(object_list[i])
        return first_name_search(given_input, given_list, i + 1)


# This function checks to see if a variable is a number
def int_check(num):
    try:
        float(num)
    except ValueError:
        return False
    else:
        return True


# Recursive function that searches through all players in database by Last Name.
def last_name_search(given_input, given_list=None, i=0):
    if not given_list:
        given_list = []
    if i == len(object_list):
        return given_list
    else:
        if given_input == dictionary[object_list[i]].get_player_last_name():
            given_list.append(object_list[i])
        return last_name_search(given_input, given_list, i + 1)


# Recursive function that returns total season played of all players in database
def list_total(temp_object_list, counter=0):
    if not temp_object_list:
        return 0
    if counter == len(temp_object_list) - 1:
        return int(dictionary[object_list[counter]].get_seasons_played())
    else:
        return int(dictionary[object_list[counter]].get_seasons_played()) + list_total(temp_object_list, counter + 1)


# The main menu of program
def main_menu():
    # Sorts the objectList, so that it is sorted by last name by default
    object_list.sort()
    user_input = input(
        "\nMAIN MENU:\n1. Add a new player\n2. Delete a player\n3. View players\n4. Search for players\n"
        "5. Calculate average and total seasons played by all players in database\n6. "
        "Exit\nChoose a number to do an action: ")
    # While loop that checks that input is valid
    while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" \
            and user_input != "5" and user_input != "6":
        user_input = input("Invalid Input. Please enter valid digit: ")
    if user_input == "1":
        player_creation()
    elif user_input == "2":
        player_deletion()
    elif user_input == "3":
        sort()
    elif user_input == "4":
        search()
    elif user_input == "5":
        seasons_total()
    elif user_input == "6":
        exit()


# A function that sorts list by merge sort
def merge_sort(given_list):  # Source: http://stackoverflow.com/questions/18761766/mergesort-python
    result = []
    if len(given_list) < 2:
        return given_list
    mid = int(len(given_list) / 2)
    y = merge_sort(given_list[:mid])
    z = merge_sort(given_list[mid:])
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


# Recursive function that searches through database by number
def number_search(user_input, given_list=None, i=0):
    if not given_list:
        given_list = []
    if i == len(object_list):
        return given_list
    else:
        if user_input == dictionary[object_list[i]].get_player_num():
            given_list.append(object_list[i])
        return number_search(user_input, given_list, i + 1)


def partition(num_list, start, end, string_list):  # Source: http://www.pythonschool.net/algorithms_quickSort/
    pivot = num_list[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and num_list[left] <= pivot:
            left += 1
        while num_list[right] >= pivot and right >= left:
            right -= - 1
        if right < left:
            done = True
        else:
            # swap places
            temp = num_list[left]
            temp1 = string_list[left]
            num_list[left] = num_list[right]
            string_list[left] = string_list[right]
            num_list[right] = temp
            string_list[right] = temp1
    # swap start with myList[right]
    temp = num_list[start]
    temp1 = string_list[start]
    num_list[start] = num_list[right]
    string_list[start] = string_list[right]
    num_list[right] = temp
    string_list[right] = temp1
    return right


def quick_sort(num_list, start, end, string_list):  # Source: http://www.pythonschool.net/algorithms_quickSort/
    if start < end:
        # partition the list
        pivot = partition(num_list, start, end, string_list)

        # sort both halves
        quick_sort(num_list, start, pivot - 1, string_list)
        quick_sort(num_list, pivot + 1, end, string_list)
    return string_list


# A function that is used in the search() function that will give the user the
# option to delete a player from the search results
def search_delete(temp_list):
    table_output(temp_list)
    # User is given option to return to delete one of the players, or to return ot the main menu
    input2 = input(
        "Would you like to:\n1. Delete a player in this list\n"
        "2. Return to the main menu\nPlease enter digit for your choice: ")
    while input2 != "1" and input2 != "2":
        input2 = input("Invalid Input. Please enter valid digit: ")
        # If user wants to delete player, delete functions are run
    if input2 == "1":
        delete_password_check()
        delete_player(temp_list)
    if input2 == "2":
        main_menu()


# This method checks to see if any part of variable is not alphabetic
def string_check(string):
    string = string.replace("-", "")
    i = 0
    try:
        len(string)
    except TypeError:
        return False
    else:
        while i < len(string):
            if string[i].isalpha():
                i += 1
            else:
                return False
        return True


# Outputs passed list in a table
def table_output(temp_object_list):
    # Labels the top row with column titles
    print("{0:<4}{1:<20}{2:<20}{3:<9}{4:<6}{5:<12}{6:<18}{7:<0}".format("#", "Last Name", "First Name", "Number", "Age",
                                                                        "Position", "Seasons Played", "Date Added"))
    print("-" * 100)
    counter = 0
    for i in temp_object_list:
        counter += 1
        print("{0:<4}{1:<20}{2:<20}{3:<9}{4:<6}{5:<12}{6:<18}{7:<0}".format(str(counter) + ".",
                                                                            dictionary[i].get_player_last_name(),
                                                                            dictionary[i].get_player_first_name(),
                                                                            dictionary[i].get_player_num(),
                                                                            dictionary[i].get_player_age(),
                                                                            dictionary[i].get_player_position(),
                                                                            dictionary[i].get_seasons_played(),
                                                                            dictionary[i].get_date_added()))
    print("\n")


# Now these are all of the functions that are the main functions thar are redirected to from the main menu
# Function that creates a new player for the database
def player_creation():
    # For each field, it asks for the info from the user, then temporarily stores it as variable
    player_first_name = input("Please enter the player's first name: ")
    # Then checks to see if input it valid
    while string_check(player_first_name) == False or int_check(player_first_name) == True or player_first_name == "":
        player_first_name = input("Invalid Name. Please enter first name: ")
    # Makes first letter uppercase, for sorting later
    player_first_name = player_first_name[0].upper() + player_first_name[1:]

    player_last_name = input("Please enter the player's last name: ")
    while string_check(player_last_name) == False or int_check(player_last_name) == True or player_last_name == "":
        player_last_name = input("Invalid Name. Please enter last name: ")
    player_last_name = player_last_name[0].upper() + player_last_name[1:]

    player_age = input("Please enter the player's age: ")
    while int_check(player_age) == False or player_age == "":
        player_age = input("Invalid age. Please enter age in digits: ")
        # If player is older than 17, then they are classified as an adult
    adult = False
    if int(player_age) > 17:
        adult = True

    player_num = input("Please enter the player's number: ")
    while int_check(player_num) == False or player_num == "":
        player_num = input("Invalid number. Please enter number in digits: ")

    player_position = input("Please enter the player's position (Player or Goalie): ")
    while player_position != "Player" and player_position != "Goalie":
        player_position = input("Invalid Input. Please enter position as either Player or Goalie: ")

    seasons_played = input("Please enter how many seasons the player has played: ")
    while int_check(seasons_played) == False or seasons_played == "":
        seasons_played = input("Invalid value. Please enter seasons played in digits: ")

    # Generates random four digit integer
    random_int = str(random.randint(1000, 9999))
    # Creates player code for player
    player_code = player_last_name + player_first_name + random_int
    if player_position == "Player":
        player_code += "P"
    else:
        player_code += "G"
    if adult:
        player_code += "A"
    # Checks that there isn't already a player with the same player code
    while not duplicate_check(object_list, player_code):
        # If player code is a duplicate, new player code is generated
        random_int = str(random.randint(1000, 9999))
        player_code = player_last_name + player_first_name + random_int
        if player_position == "Player":
            player_code += "P"
        else:
            player_code += "G"
        if adult:
            player_code += "A"
    # Player code is added to the object list
    object_list.append(player_code)
    # Object is created and is stored in dictionary
    dictionary[player_code] = PlayerDatabase(player_first_name, player_last_name, player_age, player_num,
                                             player_position, seasons_played, player_code)
    print("Player entered into database.")
    # Returns to main menu
    main_menu()


# Function that will ask for specific details of player to delete
def player_deletion():
    # If no players in database, returns to main menu
    if not object_list:
        print("There are no players in the database to delete ")
        main_menu()
    # Runs function that asks for deletion password, which is "hockey"
    delete_password_check()
    # Asks for details of desired player from user
    lastname = input("Please enter last name of player to delete: ")
    while string_check(lastname) == False or int_check(lastname) == True or lastname == "":
        lastname = input("Invalid Name. Please enter last name to delete: ")
    lastname = lastname[0].upper() + lastname[1:]
    firstname = input("Please enter first name of player to delete: ")
    while string_check(firstname) == False or int_check(firstname) == True or firstname == "":
        firstname = input("Invalid Name. Please enter first name to delete: ")
    firstname = firstname[0].upper() + firstname[1:]
    number = input("Please enter number of player to delete: ")
    while int_check(number) == False or number == "":
        number = input("Invalid age. Please enter age for deletion in digits: ")
    # Check from object list for each detail from user for the player
    tempobjectlist = []
    for i in object_list:
        if dictionary[i].get_player_last_name() == lastname:
            tempobjectlist.append(i)
        else:
            continue
    tempobjectlist1 = []
    for i in tempobjectlist:
        if dictionary[i].get_player_first_name() == firstname:
            tempobjectlist1.append(i)
        else:
            continue
    tempobjectlist2 = []
    for i in tempobjectlist1:
        if dictionary[i].get_player_num() == number:
            tempobjectlist2.append(i)
        else:
            continue
    if not tempobjectlist2:
        print("There are no players in the database with that information.")
        main_menu()
    else:
        # What happens if only one player is found with given details
        if len(tempobjectlist2) == 1:
            # Prints players in table and asks for deletion confirmation
            table_output(tempobjectlist2)
            input2 = input("Is this the player you want to delete? (Y/N): ")
            while input2 != "Y" and input2 != "N":
                input2 = input("Invalid input. Please choose yes or no (Y/N): ")
            if input2 == "Y":
                # Deletes player from object list and dictionary
                object_list.remove(tempobjectlist2[0])
                del dictionary[tempobjectlist2[0]]
                print("Player has been deleted from the database")
                main_menu()
            if input2 == "N":
                main_menu()
        # What happens if more than one players have the given details
        else:
            table_output(tempobjectlist2)
            delete_player(tempobjectlist2)

    # Rewrites all players in database to file, without deleted player
    temp_file = open("player_Database.dat", "w")
    temp_file.write(
        "{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format("Last Name", "First Name", "Number", "Age",
                                                                         "Position", "Seasons Played", "Date Added",
                                                                         "Player Code"))
    for i in object_list:
        temp_file.write(
            "\n{0:<15}{1:<15}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format(dictionary[i].get_player_last_name(),
                                                                               dictionary[
                                                                                   i].get_player_first_name(),
                                                                               dictionary[i].get_player_num(),
                                                                               dictionary[i].get_player_age(),
                                                                               dictionary[i].get_player_position(),
                                                                               dictionary[i].get_seasons_played(),
                                                                               dictionary[i].get_date_added(), i))
    temp_file.close()
    main_menu()


# Method that will sort players in the database
def sort():
    if not object_list:
        print("There are no players in the database to view. Returning to main menu")
        main_menu()
    user_input = input(
        "Would you like to:\n1. View all players\n2. Sort by a property\nPlease enter digit for your choice: ")
    while user_input != "1" and user_input != "2":
        user_input = input("Invalid Input. Please enter valid digit: ")
    if user_input == "1":
        table_output(object_list)
        main_menu()

    if user_input == "2":
        # Asks users by which property to sort by
        input2 = input(
            "Would you like to sort by:\n1. Last Name\n2. First Name\n3. Age\n4. Number\n"
            "5. Position\n6. Seasons Played\nPlease enter digit for your choice: ")

        while input2 != "1" and input2 != "2" and input2 != "3" and input2 != "4" and input2 != "5" and input2 != "6":
            input2 = input("Invalid Input. Please enter valid digit: ")
        # Sorts by Last Name
        if input2 == "1":
            objectlistcopy = object_list
            # Sorts list by merge sort, and prints it in table. Just the object List can be sorted,
            # as it has the player code in it, which have the player's last name first
            table_output(merge_sort(objectlistcopy))
            main_menu()

        # Sorts by First Name
        if input2 == "2":
            # Initializes list for sorted items
            firstnamelist = []
            objectlistcopy = object_list
            # Puts all first names of players in a list
            for i in object_list:
                firstnamelist.append(dictionary[i].get_player_first_name())
            # Sorts the players by first name
            output = quick_sort(firstnamelist, 0, len(firstnamelist) - 1, objectlistcopy)
            # Prints in table, then returns to main menu
            table_output(output)
            main_menu()

        # Sorts by Age
        if input2 == "3":
            agelist = []
            objectlistcopy = object_list
            for i in object_list:
                agelist.append(int(dictionary[i].get_player_age()))

            output = quick_sort(agelist, 0, len(agelist) - 1, objectlistcopy)
            table_output(output)
            main_menu()

        # Sort by Number
        if input2 == "4":
            numlist = []
            objectlistcopy = object_list
            for i in object_list:
                numlist.append(int(dictionary[i].get_player_num()))
            output = quick_sort(numlist, 0, len(numlist) - 1, objectlistcopy)
            table_output(output)
            main_menu()

        # Sorts by Position
        if input2 == "5":
            positionlist = []
            objectlistcopy = object_list
            for i in object_list:
                temp = dictionary[i].get_player_position()
                # For players, it give a value of 0, and a value of 1 for goalies.
                # Then when they get sorted, players will be above the goalies
                if temp == "Player":
                    positionlist.append(0)
                if temp == "Goalie":
                    positionlist.append(1)
            output = quick_sort(positionlist, 0, len(positionlist) - 1, objectlistcopy)
            table_output(output)
            main_menu()

        # Sorts by Seasons Played
        if input2 == "6":
            seasonsplayedlist = []
            objectlistcopy = object_list
            for i in object_list:
                seasonsplayedlist.append(int(dictionary[i].get_seasons_played()))
            output = quick_sort(seasonsplayedlist, 0, len(seasonsplayedlist) - 1, objectlistcopy)
            table_output(output)
            main_menu()


# Function that will search for specific players in database from info given by user
def search():
    templist = []
    if not object_list:
        print("There are no players in the database to search for. Returning to main menu")
        main_menu()
    # Asks user what property to sort by
    user_input = input(
        "Would you like to search by:\n1. Last Name\n2. First Name\n3. Number\n4. "
        "View all players\nPlease enter digit for your choice: ")
    while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4":
        user_input = input("Invalid Input. Please enter valid digit: ")
    # Searches for Last Name
    if user_input == "1":
        input1 = input("Please enter last name to search for: ")
        while string_check(input1) == False or int_check(input1) == True or input1 == "":
            input1 = input("Invalid first name. Please enter last name for search: ")
        input1 = input1[0].upper() + input1[1:]
        # Searches for players with given last name
        templist = last_name_search(input1, templist)
        # If list is empty, then there are no players with that last name in database
        if not templist:
            input2 = input(
                "There are no players with that last name in the database.\n Would you like to:\n"
                "1. Search for another player or \n2. Return to the main menu\nPlease enter digit for your choice: ")
            while input2 != "1" and input2 != "2":
                input2 = input("Invalid Input. Please enter valid digit: ")
            if input2 == "1":
                search()
            else:
                main_menu()

        # If there are players in list, user is given option to delete a player
        else:
            search_delete(templist)
            # Searches for First Name
    if user_input == "2":
        input1 = input("Please enter first name to search for: ")
        while string_check(input1) == False or int_check(input1) == True or input1 == "":
            input1 = input("Invalid first name. Please enter first name for search: ")
        input1 = input1[0].upper() + input1[1:]
        templist = first_name_search(input1, templist)
        if not templist:
            input2 = input(
                "There are no players with that first name in the database.\n Would you like to:\n"
                "1. Search for another player or \n2. Return to the main menu\nPlease enter digit for your choice: ")
            while input2 != "1" and input2 != "2":
                input2 = input("Invalid Input. Please enter valid digit: ")
            if input2 == "1":
                search()
            else:
                main_menu()
        else:
            search_delete(templist)

    # Searches for number
    if user_input == "3":
        input1 = input("Please enter number to search for: ")
        while int_check(input1) == False or input1 == "":
            input1 = input("Invalid number. Please enter number for search: ")
        templist = number_search(input1, templist)
        if not templist:
            input2 = input(
                "There are no players with that number in the database.\n Would you like to:\n"
                "1. Search for another player or \n2. Return to the main menu\nPlease enter digit for your choice: ")
            while input2 != "1" and input2 != "2":
                input2 = input("Invalid Input. Please enter valid digit: ")
            if input2 == "1":
                search()
            else:
                main_menu()
        else:
            search_delete(templist)
    # Prints all players
    if user_input == "4":
        if not object_list:
            print("There are no players in the database to print. Returning to main menu")
            main_menu()
        else:
            templist = object_list
            search_delete(templist)


# Function that will display total and average seasons played by all players in the database
def seasons_total():
    if not object_list:
        print("There are no players entered into the database. Returning to main menu")
        main_menu()
    # Finds seasons total from listTotal() function
    this_seasons_total = list_total(object_list)
    if this_seasons_total == 0:
        print("There are no seasons played entered into the database.")
    else:
        print("Total seasons played by all players is " + str(this_seasons_total) +
              ". The average seasons played is " + str(
            this_seasons_total / len(object_list)))
    main_menu()


# Initializes objectList and dictionary
object_list = []
dictionary = {}
# Writes the headings for the text file
global_file = open("player_Database.dat", "w")
global_file.write("{0:<20}{1:<20}{2:<10}{3:<8}{4:<15}{5:<20}{6:<15}{7:<15}".format(
    "Last Name", "First Name", "Number", "Age", "Position", "Seasons Played", "Date Added", "Player Code"))
global_file.close()
# Goes to the main menu for the first time
main_menu()
