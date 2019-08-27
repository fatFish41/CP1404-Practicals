import csv
import copy
import operator

# use for organize the data, organize them into different part
def sort_data(data):
    data.sort(key=operator.itemgetter(3, 2))
    return data
# this is to organize the places into a list
# the things about the row is use for putting the number in order
# and the V shows the place that have not visit yet which will show by *
def show_list():
    locationreader = open('places.csv')
    location = list(csv.reader(locationreader, delimiter=','))
    location_temp = copy.copy(location)
    for row in location_temp:
        row[2] = int(row[2])
    location_temp = sort_data(location_temp)
    for i in range(1, len(location_temp)+1, 1):
        if location_temp[i-1][3] == 'V':
            location_temp[i-1][3] = '*'
        else:
            location_temp[i-1][3] = ''
        print(i, '. {:1} {:10} {:1} {:15} {} {} {}'.format(location_temp[i-1][3], location_temp[i-1][0], 'in',
                                                           location_temp[i-1][1], ' Priority(', location_temp[i-1][2], ')'))

# this is the option for menu which is the main function
def main():
    print("Travel Tracker 1.0 - by Weilun Tu")
    data = list(csv.reader(open("places.csv")))
    menu = ">>> "
    print("Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit")
    while menu.upper() != 'Q':
        for row in data:
            row[2] = int(row[2])
        data = sort_data(data)
        menu = input()
        if menu == "L" or menu == "l":
            show_list()
            print("{} places. You still want to visit {} places.".format(len(data), get_unvisited_num(data)))
            print("Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit")

        elif menu == "A" or menu == "a":
            name = input("Name: ")
            newplaces = []
            while name == "":
                print("Input can not be blank")
                name = input("Name: ")
            newplaces.append(name)
            country=input("Country: ")
            while country == "":
                print("Input can not be blank")
                country = input("Country: ")
            newplaces.append(country)
            valid_input = False
            while not valid_input:
                try:
                    Priority = int(input("Priority:"))

                except ValueError:
                    print("Invaild input; exnter a vaild number.")

                else:
                    if Priority <= 0:
                        print("cannot be less than 0")
                    else:
                        valid_input = True
            newplaces.append((Priority))
            newplaces.append("V")
            with open('places.csv', 'a') as places:
                writer = csv.writer(places)
                writer.writerow(newplaces)
            print("{} in {} (priority {}) added to Travel Tracker".format(name, country, Priority))
            print("")
            print("Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit")

        elif menu == "M" or menu == "m":

            if get_unvisited_num(data) == 0:
                print("No unvisited places")
            else:
                show_list()
                print("Enter the number of a place to mark as visited")
                num_mark = input(">>> ")
                while mark(num_mark) != 0:
                    num_mark = input(">>> ")
                while int(num_mark) > len(data):
                    print("Invalid place number")
                    num_mark = input(">>> ")
                if data[int(num_mark)-1][3] == "Y":
                    print("That place is already visited")
                else:
                    data[int(num_mark)-1][3] = "Y"
                    with open("places.csv", "w") as csv_places:
                        writer = csv.writer(csv_places, delimiter=",")
                        for row in data:
                            writer.writerow([row[0], row[1], row[2], row[3]])
                    print(data[int(num_mark)-1][0] + " in " + data[int(num_mark)-1][1] + " visited!")


            print("Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit")


        elif menu == "Q" or menu == "q":
            print(str(len(data))+" places saved to places.csv. Have a nice day :)")

        else:
            print("Invalid menu choice")
            print("Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit")

# this is a function to get the number of unvisited
def get_unvisited_num(data):
    unvisited_num = 0
    for i in range(len(data)):
        if data[i][3] == "V":
            unvisited_num += 1
    return unvisited_num

# this ia to make sure that the user does not put in the wrong number
def mark(num):
    try:
        num = int(str(num))
        if isinstance(num, int) == True:
            if num <= 0:
                print("Number must be > 0")
                return 1
            return 0
        else:
            return 2
    except:
        print("Invalid input; enter a valid number")
        return 2

main()
