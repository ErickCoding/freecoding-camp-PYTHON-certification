import sys
class App:
    id = 0
    all = []
    login_dictionary = {}
    first_response_not_seven_or_eight = True
    logged_in = False
    exit = False

    @classmethod
    def id_assignment(cls):
        cls.id += 1
        return cls.id

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.primary_id = App.id_assignment()
        App.all.append(self)
        App.login_dictionary[self.username] = [self.password,  self.primary_id]

    def __repr__(self):
        return f"{self.username}"  # self.password,self.primary_id}"

    @classmethod
    def add_account(cls):
        distinct_user = False
        while distinct_user is False:
            new_username = input("Enter the Username you would like to have.\n").lower()
            if new_username in cls.login_dictionary:
                print("This Username Is Taken. Please Enter Another Username.")
            else:
                distinct_user = True
        new_password = input("Enter your Password. This is Case Sensitive.\n")
        new_account =App(new_username, new_password)
        print("Account Created")
        return new_account.username

    @classmethod
    def do_you_have_an_account(cls):
        return int(input("Do you have an account with us?\n1. Yes\n2. No\n3. Exit\n"))

    @classmethod
    def login_verification(cls, username, password):
        if username in App.login_dictionary and password == cls.login_dictionary[username][0]:
            App.logged_in = True
            return App.logged_in
        else:
            print("The Information You Entered is Incorrect. Please try again")

    @classmethod
    def welcome(cls):
        print("Welcome to I should be Asleep Budget App.")
        response=cls.do_you_have_an_account()
        if response == 1:
            while App.logged_in is False:
                username = input("Type in your username information.   username=a    \n").lower()
                password = input("Type in your password information.This is Case-Sensitive    password=a    \n")
                cls.login_verification(username, password)
            return username
        elif response == 2:
            App.logged_in = True
            return cls.add_account()
        elif response == 3:
            exit()

    @staticmethod
    def first_question(current_user):
        first_response = int(input("Hello " +current_user +' what will you be doing today? Please enter the number corresponding with the options.\n1. Check Balance \n2. See transactions \n3. Deposit \n4. Spend \n5. Withdraw \n6. Transfer\n7. Make New Category\n8. See Bar table of your percent spending\n9. Log Out\n'))
        if first_response == 7 or first_response==8 or first_response==9:
            App.first_response_not_seven_or_eight = False
            return first_response
        else:
            return first_response

    @staticmethod
    def second_question():
        if App.first_response_not_seven_or_eight is False:
            return None
        else:
            print("Which budget?")
            Category.print_every_category()
            second_response = int(input())
            return Category.find_category_by_id(second_response)

    @classmethod
    def current_user(cls):
        return str(cls.welcome())

    @staticmethod
    def current_id(cls):
        return cls.welcome().username

    @classmethod
    def complete_run(cls):
        while True:
            name_input=cls.current_user()
            try:
                current_id = App.login_dictionary[name_input][1]
            except:
                print("Please pick a number in the menu.\n")
            while cls.logged_in is True:
                cls.system_response(cls.first_question(name_input), cls.second_question(), current_id)

    @staticmethod
    def system_response(first_response, second_response, current_id):
        if first_response == 1:
            print(Category.check_balance(second_response, current_id))
        if first_response == 2:
            print(Category.see_transactions(second_response,current_id))
        if first_response == 3:
            deposit_amount = float(input("How much would you like to deposit?\n "))
            print("Your  " +Category.deposit(second_response, deposit_amount, current_id) +" has been successfully deposited into  " +second_response.name)
            Transaction.print_transactions(second_response.transactions_in_category_id(current_id),current_id)
        if first_response == 4:
            amount = float(input("How much  would you like to spend?\n"))
            if second_response.expense_check(amount, current_id) is True:
                description = str(input("What is the expense for? \n"))
                Category.spend(second_response, amount, current_id,description)
                print(" ${:.2f}".format(amount ) +" has been successfully deducted from  " +second_response.name)
                Transaction.print_transactions(second_response.transactions_in_category_id(current_id),current_id)

        if first_response == 5:
            amount = float(input("How much  would you like to withdraw?\n"))
            if second_response.expense_check(amount, current_id) is True:
                Category.withdraw(second_response, amount,current_id)
                print(" ${:.2f}".format(amount) + " has been successfully withdrawn from " + second_response.name)
                Transaction.print_transactions(second_response.transactions_in_category_id(current_id),current_id)

        if first_response == 6:
            amount = float(input("How much would you like to transfer from " + second_response.name + "?\n"))
            if second_response.expense_check(amount, current_id) is True:
                print("To which budget? Input the number corresponding to the Category")
                option_left=second_response.transfer_method()
                transfer_response = int(input())
                while (transfer_response not in option_left) is True:
                    print("Please select a number on the menu.\n")
                    option_left = second_response.transfer_method()
                    transfer_response = int(input())
                Category.transfer(second_response,  amount, transfer_response, current_id)
        if first_response == 7:
            name_of_category = input("Name of the new Category?\n")
            Category.make_new_category(name_of_category,current_id)
            print(Category.all)
            print(Transaction.all)
        if first_response == 8:
            App.percent_bar_chart(current_id)
        if first_response ==9:
            App.logged_in = False


    '''@classmethod
    def chart_o(cls):
        category_o = {}
        for category in cls.all:
            category_o[category.name] = " "
        return category_o'''

    @staticmethod
    def percent_bar_chart(current_id):
        x = 100
        chart = {}
        for category in Category.all:
            chart[category.name] = " "
        print("Percentage spent per Category")
        while x >= 0:
            space = (4 - len(str(x))) * " "
            row_print = space + str(x) + "| "
            for category in Category.all:
                if chart[category.name] == " " and int(category.category_spending_ratio(current_id)) >= x:
                    chart[category.name] = "o"
                row_print = row_print + chart[category.name] + "  "
            print(row_print)
            x = x - 10
        print("     " + (len(Category.all) * 3 + 1) * "-")
        for number in range(0, Category.category_name_max_len()):
            string = "      "
            for category in Category.all:
                try:
                    string = string + category.name[number] + "  "
                except:
                    string = string + "   "
            print(string)

#######################################################################################################################
class Category:
    all = []
    id = 0

    @classmethod
    def id_assignment(cls):
        cls.id += 1
        return cls.id

    def __init__(self, name):
        self.name = name
        self.id = Category.id_assignment()
        Category.all.append(self)

    def __repr__(self):
        return f"{self.name}"

    @staticmethod
    def check_balance(second_response, current_id):
        return second_response.category_total(current_id)

    @staticmethod
    def see_transactions(second_response ,current_id):
        return Transaction.print_transactions(second_response.transactions_in_category_id(current_id),current_id)

    @staticmethod
    def deposit(second_response,deposit_amount,current_id):
        # deposit_amount = float(input("How much would you like to deposit?\n "))
        second_response.add_balance("Deposit", deposit_amount, current_id)
        return " ${:.2f}".format(deposit_amount)
        # Transaction.print_transactions(second_response.transactions_in_category_id())

    @staticmethod
    def spend(second_response, amount, current_id, description):
        second_response.add_expense(description, amount,current_id)

    @staticmethod
    def withdraw(second_response, amount, current_id):
        second_response.add_expense("Withdraw", amount,current_id)
        # Transaction.print_transactions(second_response.transactions_in_category_id())

    @staticmethod
    def transfer(second_response, amount, transfer_response,current_id):
        transfer_to = Category.find_category_by_id(transfer_response)
        second_response.add_expense("Transfer to " + transfer_to.name, amount,current_id)
        transfer_to.add_balance("Transferred from " + second_response.name, amount,current_id)

    @classmethod
    def make_new_category(cls, new_name,current_id):
        new_category = Category(new_name)
        new_category.add_balance("Initial amount", 100,current_id)

    @classmethod
    def find_category_by_id(cls, input_id):
        for category in cls.all:
            if category.id == input_id:
                return category

    @classmethod
    def category_name_max_len(cls):
        len_of_name = []
        for category in cls.all:
            len_of_name.append(len(category.name))
        return max(len_of_name)

    def transactions_in_category_id(self, current_id):
        filter = []
        for entry in Transaction.all:
            if entry.category == self and entry.user_id == current_id:
                filter.append(entry)
        return filter

    def transfer_method(self):
        remaining_options=[]
        for category in Category.all:
            if category != self:
                print(str(category.id) + ". " + category.name)
                remaining_options.append(category.id)
        return remaining_options

    @classmethod
    def print_every_category(cls):
        for category in cls.all:
            print(str(category.id) + ". " + category.name)

    def add_balance(self, description, amount, user_id):
        Transaction(description, amount, self, user_id)

    def expense_check(self, amount, current_id):
        if eval(self.category_total(current_id)[:1] + self.category_total(current_id)[2:]) < amount:
            print("Amount inputted higher then current budget.\nTransaction did not go through.")
        else:
            return True

    def add_expense(self, description, amount,user_id):
        Transaction(description, -1 * amount, self, user_id)
        return "Expense added"

    # def transfer(self, amount, transfer_from):
    #  Category.find_category_by_id(transfer_from).add_balance("Transfer from " + self.name, amount)
    # Category.find_category_by_id(self).add_expense("Transfer to " + transfer_from.name, amount)

    def count_in_category(self):
        number_transaction = 0
        for item in Transaction.all:
            if item.category == self:
                number_transaction += 1
        return number_transaction

    def category_total(self, current_id):
        total = 0
        for entry in self.transactions_in_category_id(current_id):
            total = total + eval(entry.amount[0:1] + entry.amount[2:])
        if total < 0:
            return "-${:.2f}".format(abs(total))
        else:
            return " ${:.2f}".format(abs(total))

    def category_spending(self ,current_id):
        expense = 0
        for transaction in self.transactions_in_category_id(current_id):
            if eval(transaction.amount[0:1] + transaction.amount[2:]) < 0:
                expense = expense + eval(transaction.amount[0:1] + transaction.amount[2:])
        return "-${:.2f}".format(abs(expense))

    def category_saving(self ,current_id):
        saving = 0
        for transaction in self.transactions_in_category_id(current_id):
            if eval(transaction.amount[0:1] + transaction.amount[2:]) > 0:
                saving = saving + eval(transaction.amount[0:1] + transaction.amount[2:])
        return " ${:.2f}".format(saving)

    def category_spending_ratio(self,current_id):
        try:
            return round((eval(self.category_spending(current_id)[2:]) / eval(self.category_saving(current_id)[2:])) * 100, -1)
        except:
            return 0

    @classmethod
    def expense_ranking(cls):
        category_expense = {}
        for group in Category.all:
            expense = 0
            for transaction in group.transactions_in_category_id():
                if eval(transaction.amount[0:1] + transaction.amount[2:]) < 0:
                    expense = expense + eval(transaction.amount[0:1] + transaction.amount[2:])
            category_expense[group] = expense
        high_to_low = sorted(category_expense.items(), key=lambda x: x[1])
        return [x[0] for x in high_to_low]

    @staticmethod
    def low_to_high_category():
        count = {}
        for item in Transaction.all:
            if item.category not in count:
                count[item.category] = 1
            else:
                count[item.category] = count[item.category] + 1
        low_to_high_category = sorted(count.items(), key=lambda x: x[1])
        return low_to_high_category


food_obj = Category("Food")
utility_obj = Category("Utility")
travel_obj = Category("Travel")

#####################################################################################################################
class Transaction:
    all = []

    def __init__(self, description, amount, category ,user_id):
        if amount < 0:
            self.amount = '-${:.2f}'.format(abs(amount))
        else:
            self.amount = ' ${:.2f}'.format(amount)
        self.description = description
        self.category = category
        self.user_id =user_id
        Transaction.all.append(self)
        # Transaction.all.append((self.description, "${: .2f}".format(self.amount), self.description))

    @classmethod
    def print_transactions(cls, list, current_id):
        if len(list)==0:
            return "There are currently no transactions"
        else:
            number_of_asterisk = round((30 - len(str(list[0].category))) / 2)
            print((number_of_asterisk * "*" + str(list[0].category) + number_of_asterisk * "*"))
            for transaction in list:
                length_space = 30 - len(transaction.description) - len(transaction.amount)
                print(transaction.description[0:24] + length_space * " " + transaction.amount[0:8])
            return "Total: " + str(list[0].category.category_total(current_id))

    #
    def __repr__(self):
        # return f"{self.description} "+"${:.2f}".format(self.amount)+f" {self.category}"
        return f"{self.description, self.amount, self.category}"

    @staticmethod
    def user_transactions(id):
        filter =[]
        for transaction in Transaction.all:
            if transaction.user_id == id:
                filter.append(transaction)
        return filter


gas_deposit = Transaction("deposit", 100, utility_obj, 1)
bus_deposit = Transaction("deposit", 100, travel_obj, 1)
food_deposit = Transaction("deposit", 100, food_obj, 1)
grocery_obj = Transaction("grocery", -10, food_obj, 1)
electricity_obj = Transaction("electricity", -20, utility_obj, 1)
gas_obj = Transaction("gas", -14, utility_obj, 2)
bus_obj = Transaction("bus", -2, travel_obj ,1)
groc_obj = Transaction("groc", -4, food_obj ,1)
first_user = App("a", "a")
second_user = App("john", "Abc123")
#############################################################################################################
#print(type(App.second_question()))
App.complete_run()
