from tabulate import tabulate  # to print tabular data into formatted tables
from datetime import datetime  # to get current date/time
import copy  # to create a copy
import random  # to generate randomly
import time

data_repository = []  # for storing driver data as a nested list from appending data_compile


def driver_details():  # Function to add new driver data to data_repository
    initiation()
    data_compile = []  # for storing driver data to append to data_repository

    name = input("\033[1;30mEnter diver Name: ")
    if name.upper() in [item[0] for item in data_repository]:  # checking whether the new driver name already exists
        print("\033[1;91mError.This name already exists.")
        user_decision = input("\033[1;33mDo you wish to enter a new entry?(yes/no) ")
        if 'yes' == user_decision.lower():
            driver_details()  # going back to the start of the function

        else:
            conclusion()
            return  # exit from the function and going back to the start menu

    while True:  # infinite loop to get the input
        try:
            age = int(input("\033[1;30mEnter driver age: "))
            break  # if no value error occurred break the loop
        except ValueError:  # if occurred, handle the value error
            print("\033[1;91mError.Enter a valid input.")

    team = input("Enter the team name: ")
    car_model = input("Enter the model of the car: ")

    while True:
        try:
            current_points = int(input("\033[1;30mEnter the current points: "))
            break
        except ValueError:
            print("\033[1;91mError.Enter a valid input.")

    data_compile.append(name.upper())  # appending name to data_compile
    data_compile.append(age)
    data_compile.append(team)
    data_compile.append(car_model)
    data_compile.append(current_points)
    data_repository.append(data_compile)  # appending data_compile list to data_repository

    print("\n\033[1;94mDriver details entered successfully")

    conclusion()


# referred from www.learnbyexample.org/python-nested-list/
# referred from www.gist.github.com/manojnaidu619
# referred from www.youtu.be/Hs0ySdsuxm8


def delete_driver_details():  # Function to delete driver data from data_repository
    initiation()
    delete_index = input("\033[1;30mEnter driver name to delete details: ")
    temp_name = [item[0] for item in data_repository]  # list with 1st element of each item in the data_repository

    if delete_index.upper() in temp_name:  # check driver name in the temp_name
        name_index = temp_name.index(delete_index.upper())  # get the index of driver in the data_repository to delete
        del data_repository[int(name_index)]  # delete driver details

        print("\n\033[1;94mDriver details deleted successfully.")

        conclusion()
    else:
        print("\n\033[1;91mInvalid input.Driver name not found.")
        retry = input("\033[1;91mDo you want to try again?(yes/no) ")
        if 'yes' == retry.lower():
            delete_driver_details()  # going back to the start of the function
        else:
            conclusion()


def update_driver_details():  # Function to update driver data in data_repository
    def upd_details():  # Function to get driver details to update
        while True:
            try:
                new_age = int(input("\033[1;30mEnter new driver age: "))
                break
            except ValueError:
                print("\033[1;91mError.Enter a valid input.")

        new_team = input("Enter the new team name: ")
        new_car_model = input("Enter the new model of the car: ")

        while True:
            try:
                new_points = int(input("\033[1;30mEnter the current new points of the team: "))
                break
            except ValueError:
                print("\033[1;91mError.Enter a valid input.")

        data_repository[int(name_index)][1] = new_age  # change the value of the element corresponding to the index
        data_repository[int(name_index)][2] = new_team
        data_repository[int(name_index)][3] = new_car_model
        data_repository[int(name_index)][4] = new_points

        print("\n\033[1;94mDriver details updated successfully.")

        conclusion()
        return  # exit from the function and going back to the start menu

    initiation()
    update_index = input("\033[1;30mEnter driver name to update: ")  # get the driver name to change
    temp_name = [item[0] for item in data_repository]

    if update_index.upper() in temp_name:
        name_index = temp_name.index(update_index.upper())  # if name is in the list, get the index of it
        update_name = input("\033[1;33mDo you want to change the name?(yes/no) ")
        if 'yes' != update_name.lower():
            upd_details()  # if user doesn't want to change name, go to upd_details function

        else:  # if user want to change name
            while True:
                temp_name[int(name_index)] = '...'  # change selected name temporarily
                new_name = input("\033[1;30mEnter new name:")
                if new_name.upper() in temp_name:  # check whether the new name already exists
                    print("\033[1;91mError.Driver under this name already exists.\n"
                          "Enter a valid name.")
                    continue  # if name exists, get a new name again
                else:
                    data_repository[int(name_index)][0] = new_name.upper()
                    break

            upd_details()

    else:
        print("\n\033[1;91mInvalid input.Driver name not found.")
        retry = input("\033[1;33mDo you want to try again?(yes/no) ")
        if 'yes' == retry.lower():
            update_driver_details()
        else:
            conclusion()


def display_standings():  # Function to display driver standings
    temp_standings = [[item[0], item[2], item[3], item[4]] for item in
                      data_repository]  # make a nested list with elements of each item in the data_repository
    standings_sorted = sorted(temp_standings, key=lambda driver: driver[3],
                              reverse=True)  # sort each item according to the driver points in ascending order
    table_index = list(range(1, len(temp_standings) + 1))  # get a list of numbers within a range

    print(tabulate(standings_sorted, headers=["Position", "Driver Name", "Driver team", "Car model", "Points"],
                   colalign=("center", "left", "center", "center", "center"), showindex=table_index, tablefmt="pretty"))
    # print sorted data in a tabular format
    conclusion()


def stimulate_race():  # Function to stimulate a random race
    def race_countdown():  # Function to start race countdown
        time.sleep(3)
        print('\n\033[1;91mRace start in ......3', end='')
        time.sleep(1)
        print('.....2', end='')
        time.sleep(1)
        print('.....1', end='')
        time.sleep(1)
        print(' Race start!')
        time.sleep(2)

    def leaderboard_loading():  # Function to display 'leaderboards loading' statement
        time.sleep(2)
        print('\033[1;30mRace Leaderboards loading........', end='')
        for i in range(5):
            print('....' * i, end='')
            time.sleep(1)
        time.sleep(2)

    if len(data_repository) < 3:  # check whether sufficient drivers are available
        print("\n\033[1;91mTo stimulate a race, at least three players needed.", '\n')

    else:
        initiation()
        time.sleep(1)
        try:
            print(f"\n\033[1;94m{open('Race_stimulation_details.txt').readlines()[0].rstrip()}")
            #  print lines from the txt file
            time.sleep(3)
            print(f"{open('Race_stimulation_details.txt').readlines()[1].rstrip()}", )
            time.sleep(1)

            location = list(open('Race_stimulation_details.txt').read().splitlines()[6:12])
            # read locations from txt file and append them to the list
            random_location = random.choice(location)  # get a random location
            index = location.index(random_location)  # get the index of the random location

            print(
                f"\n\033[1;94m{open('Race_stimulation_details.txt').readlines()[2].rstrip()} "
                f"\033[1;32m{random_location}")  # print the random location
            time.sleep(1)
            print(
                f"\033[1;94m{open('Race_stimulation_details.txt').readlines()[3].rstrip()} "
                f"\033[1;32m{open('Race_stimulation_details.txt').readlines()[index + 14].rstrip()}")
            # print a set txt line(date) according to the selected location
        except FileNotFoundError:
            print("\033[1;91mError.No game details found.")

        race_countdown()
        initiation()
        leaderboard_loading()
        print()

        temper_results = copy.deepcopy(data_repository)  # create a copy of data_repository
        points_to_assign = [10, 7, 5]
        count = 0
        index_except = []

        while count != 3:  # run till count reaches three
            random_index = random.randrange(len(temper_results))  # returns a random number within a range as index
            if random_index not in index_except:  # check whether the number in index_except
                index_except.append(random_index)  # if not append that number
                point_assign = random.choice(points_to_assign)  # randomly choice a point from points_to_assign
                temper_results[int(random_index)][4] += point_assign  # add the chosen point to the selected driver
                points_to_assign.remove(point_assign)  # remove the chose point from points_to_assign list
                count += 1
            else:
                continue

        temp_standings = [[item[0], item[2], item[4]] for item in temper_results]
        standings_sorted = sorted(temp_standings, key=lambda driver: driver[2], reverse=True)
        table_index = list(range(1, len(temp_standings) + 1))

        print(tabulate(standings_sorted, headers=["Position", "Driver Name", "Driver team", "Points"],
                       colalign=("center", "left", "center", "center"), showindex=table_index, tablefmt="pretty"))

        conclusion()


def view_race_table():  # Function to view race table
    initiation()
    try:
        file = open("Race_settings.txt", 'r')  # open txt file in read mode
        lines = file.read().splitlines()[1:]  # read text file line by line
        file.close()

        race_settings = []
        for line in lines:
            race_settings.append(line.split(','))  # append as one item with two elements to the list

        races_sorted = sorted(race_settings, key=lambda date: datetime.strptime(date[1], "%d-%m-%Y"), reverse=False)
        table_index = list(range(1, len(race_settings) + 1))
        print(f"\033[1;94m{'Race table of 2023 as for': >30} {datetime.date(datetime.now())}")
        time.sleep(1)
        print(tabulate(races_sorted, headers=["Index", "Circuit", "Date"], showindex=table_index,
                       colalign=("center", "left", "center"), tablefmt="pretty"))
    except FileNotFoundError:
        print("\033[1;91mError.No data found.")

    conclusion()


# referred from blog.finxter.com/python-list-copy/


def save_driver_data():
    initiation()
    print(f"\033[1;33mWould you like to add to existing data or overwrite data?\n"
          f"{'* Type EXD to add to existing data.': >40}\n"
          f"{'* Type OVD to overwrite.': >29}")

    user_decision = input("\nEnter your choice: ")
    if user_decision.upper() == "EXD":
        with open('Driver_details.txt', 'a') as file:  # to overwrite the txt file
            for sublist in data_repository:
                line = "{},{},{},{},{}\n".format(sublist[0], sublist[1], sublist[2], sublist[3], sublist[4])
                file.write(line)  # save each element in item of data_repository in a set format
    elif user_decision.upper() == "OVD":
        with open('Driver_details.txt', 'w') as file:  # to append to the txt file
            for sublist in data_repository:
                line = "{},{},{},{},{}\n".format(sublist[0], sublist[1], sublist[2], sublist[3], sublist[4])
                file.write(line)
    else:
        print("\n\033[1;91mInvalid input! Back to the menu.")
        conclusion()
        return

    print("\033[1;94mDriver details saved successfully.")

    conclusion()


# referred from stackoverflow.com/questions/47126718/writing-nested-lists-into-a-txt-file
# original author srikavineehari

def load_driver_data():  # to load data from saved txt file
    initiation()
    try:
        file = open("Driver_details.txt", 'r')
        lines = file.readlines()  # to read each line in the txt file
        file.close()

        for line in lines:
            data_repository.append(line.split(','))  # append as one item with two elements to the list
        for i in range(len(data_repository)):
            data_repository[i][1], data_repository[i][4] = int(data_repository[i][1]), int(data_repository[i][4])
            # convert certain values in an item to integers in the list

        time.sleep(0.5)
        print("\033[1;94mDriver details loaded successfully.")
    except FileNotFoundError:
        print("\033[1;91mError.No data found.")

    conclusion()


# referred from www.sololearn.com/discuss/1626124/read-contents-of-a-file-and-create-nested-list
# refereed from www.programiz.com/python-programming/examples/read-line-by-line

def conclusion():  # Function to display at the end
    for i in range(4):
        print("\033[1;93m-------------" * i, end='')
        time.sleep(0.5)
    print()


def initiation():  # Function to display in the beginning
    for i in range(4):
        print("\033[1;92m-------------" * i, end='')
        time.sleep(0.8)
    print()


load_count = 0

print("\n\033[1;94m______________World Rally Cross Championship Management System______________")
time.sleep(1)

while True:  # Displaying the Console menu
    if len(data_repository) < 1:  # Displaying the Console menu only when the length of data_repository < one.
        print(f"\n\033[1;33m{'Console menu' : >40}",
              "\n\033[1;30m1. Type 'ADD' to enter new driver details",
              "\n2. Type 'RFF' to load data from previous record",
              "\n3. Type 'VRL' to view race table",
              "\n4. Type 'ESC' to exit")

    else:  # Displaying the Console menu when length of data_repository > one.
        print(f"\n\033[1;33m{'Console menu' : >40}",
              "\n\033[1;30m1. Type 'ADD' to enter new driver details",
              "\n2. Type 'RFF' to load data from previous record",
              "\n3. Type 'DDD' to delete driver details",
              "\n4. Type 'UDD' to update driver details",
              "\n5. Type 'VCT' to view rally cross standings",
              "\n6. Type 'SRR' to simulate a random race",
              "\n7. Type 'VRL' to view race table",
              "\n8. Type 'STF' to save the current data",
              "\n9. Type 'ESC' to exit")

    user_input = input("\nEnter your choice: ")  # Getting user input for the console menu

    if 'ADD' == user_input.upper():
        driver_details()  # Calling driver_details function

    elif 'RFF' == user_input.upper():
        if load_count == 0:
            load_count += 1
            load_driver_data()  # Calling load_driver_data function
        else:
            print(f"\n\033[1;91mWARNING!"
                  f"\nYou have loaded data {load_count} time/s."
                  f"This might cause driver details duplication.")
            user_permission = input("\n\033[1;33mDo you wish to continue?(yes/no) ")
            if 'yes' == user_permission.lower():
                load_count += 1
                load_driver_data()

            else:
                conclusion()
                continue

    elif 'DDD' == user_input.upper() and len(data_repository) >= 1:
        delete_driver_details()  # Call delete_driver_details function

    elif 'UDD' == user_input.upper() and len(data_repository) >= 1:
        update_driver_details()  # Call update_driver_details function

    elif 'VCT' == user_input.upper() and len(data_repository) >= 1:
        print()
        display_standings()  # Call display_standings function

    elif 'VRL' == user_input.upper():
        view_race_table()  # Call view_race_table function

    elif 'STF' == user_input.upper():
        save_driver_data()  # Call save_driver_data function

    elif 'SRR' == user_input.upper() and len(data_repository) >= 1:
        stimulate_race()  # C stimulate_race function

    elif user_input.upper() == 'ESC':
        break  # Call to exit the program
    else:
        print("\033[1;91mInvalid Choice, Try again!")
