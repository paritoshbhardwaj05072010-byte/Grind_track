from datetime import date

def write_logs(choice):
    if choice == "1":
        today = date.today()
        print(today)
        coding = input("Enter coding hours: ")
        workout = input("Did you workout today? (yes/no): ")
        sleep = input("Enter sleep hours: ")
        water = input("Enter water intake (in glasses): ")
        study = input("Enter study hours: ")
        file = open("log.txt", "a")
        content = file.write("Date: " + str(today) + "\n\n" + "Coding: " + coding + "\n\n" + "Workout: " + workout + "\n\n" + "Sleep: " + sleep + "\n\n" + "Water: " + water + "\n\n" + "Study: " + study)
        print("Your log has been saved. Keep up the good work!")
        file.close()

def read_logs(choice):
    if choice == "2":
        file = open("log.txt", "r")
        content = file.read()
        print(content)
        file.close()

def main():
    greet = input("enter your name: ")
    print("hello " + greet + " welcome to the grindtrack")
    while True:
        choice = input("what do you want to do? \n 1. Write today's logs \n 2. Read your logs \n 3. Exit \n 4. Clear logs \n")
        if choice == "1":
            write_logs(choice)
        elif choice == "2":
            read_logs(choice)
        elif choice == "3":
            print("\nGoodbye! Keep grinding!")
            break
        elif choice == "4":
            clear_logs()
        else:
            print("\nInvalid choice. Please try again.")
def clear_logs():
    confirm = input("Are you sure you want to clear all logs? (yes/no): ")

    if confirm.lower() == "yes":
        open("log.txt", "w").close()
        print("\nLogs cleared successfully.")
    else:
        print("Cancelled.")

main()
