#Personal Expense Tracker
import json
import os

# For Add User:
class add_user :
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

# For Add Expenses:
class add_expense :
    def __init__(self,expenses,category,note,date):
        self.expenses = expenses
        self.category = category
        self.note = note
        self.date = date
        expense_dict = {
            "date" : self.date,
            "Expenses" : self.expenses,
            "Category" : self.category,
            "Note" : self.note
        }

        file_path = "E:\\Expense Tracker App\\Expense.json" # File path where data will be stored
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0 :
            try :
                with open("Expense.json", 'r') as f:
                    data = json.load(f)
            except FileNotFoundError:
                data = []
        else :
            data = []

        data.append(expense_dict)

        with open("Expense.json", 'w') as f :
            json.dump(data, f, indent=4)

# Main function for expense tracking:
def main() :
    name = "YourName" # Enter your name
    lastname = "YourLastName" # Enter your last name
    person = add_user(firstname=name, lastname=lastname)
    print(f"Hello {person.firstname} {person.lastname}")
    # Main loop of the program.
    # It runs continuously and lets the user add new expenses
    # or view existing expenses until the user exits the program.
    while True:
        print("\n1.Add Expense \n2.Show Expense \n3.Exit")
        task = input("Enter Your Task from the above (1/2/3): ")

        if task == "1":
            add_expense(date=input("Enter Date of the expense (DD-MM-YY) : "),
                        expenses=input("Enter Your Expenses : "),
                        category=input("Enter the reason for expense : "),
                        note=input("Enter Your note : "))

            print("Expense is Added.")

        elif task == "2" :
            with open("Expense.json", 'r') as exp:
                r = json.load(exp)

            for exp in r:
                print("\n")
                print("1.Date :", exp["date"])
                print("2.Expense :", exp["Expenses"])
                print("3.Category :", exp["Category"])
                print("4.Note :", exp["Note"])

        elif task == "3" :
            print("Exiting the App....")
            break

        else :
            print("Please Write the valid task.")

if "__main__" == __name__:
    main()