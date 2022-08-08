class Category:
    all=[]
    first_response_not_seven=True
    def __init__(self,name,id):
        self.name = name
        self.id=id
        Category.all.append(self)

    def __repr__(self):
        return f"{self.name}"

    @classmethod
    def first_question(cls):
        first_response=int(input('What will you be doing today? Please enter the number corresponding with the options.\n1. Check Balance \n2. See transactions \n3. Deposit \n4. Spend \n5. Withdraw \n6. Transfer\n7. Make New Category\n'))
        if first_response==7:
            Category.first_response_not_seven=True
        return first_response
    @staticmethod
    def second_question():
        if Category.first_response_not_seven is True:
            return None
        else:
            print("Which budget?")
            Category.every_category()
            second_response=int(input())
            return Category.find_category_by_id(second_response)


    @staticmethod
    def system_response(first_response,second_response):
        if first_response==1:
            print(second_response.category_total())
        if first_response==2:
            Transaction.print_transactions(second_response.transactions_in_category())
        if first_response==3:
            deposit_amount = float(input("How much would you like to deposit?\n "))
            second_response.add_balance("Deposit",deposit_amount)
            #Transaction.print_transactions(second_response.transactions_in_category())
        if first_response==4:
            amount=float(input("How much  would you like to spend?\n"))
            second_response.expense_check(amount)
            description=input("What is the expense for? \n")
            second_response.add_expense(description,amount)
            #Transaction.print_transactions(second_response.transactions_in_category())
        if first_response==5:
            amount = float(input("How much  would you like to withdraw?\n"))
            second_response.expense_check(amount)
            description="Withdraw"
            second_response.add_expense(description, amount)
            # Transaction.print_transactions(second_response.transactions_in_category())
        if first_response==6:
            amount=float(input("How much would you like to transfer from "+second_response.name +"?\n"))
            second_response.expense_check(amount)
            print("To which budget? Input the number corresponding to the Category")
            second_response.transfer_method()
            transfer_response=int(input())
            second_response.transfer(amount,Category.find_category_by_id(transfer_response))
            print(Transaction.all)
        if first_response==7:
            new_category=Category(input("Name of the new Category?\n"),Category.next_id())
            new_category.add_balance("Initial amount",0)
            print(Category.all)
            print(Transaction.all)



    @classmethod
    def find_category_by_id(cls,id):
        for category in Category.all:
            if category.id==id:
                return category
                break

    '''def transactions_in_category(self):
        filter=[]
        for entry in Transaction.all:
            if entry.category==self:
                filter.append(entry)
        return filter'''

    def transactions_in_category(self):
        filter=[]
        for entry in Transaction.all:
            if entry.category==self:
                filter.append(entry)
        return filter

    def transfer_method(self):
        for category in Category.all:
            if category!=self:
                print(str(category.id)+". "+category.name)

    @classmethod
    def every_category(self):
        for category in Category.all:
            print(str(category.id)+". "+category.name)

    def add_balance(self,description,amount):
        Transaction(description,amount,self)

    def expense_check(self,amount):
        if eval(self.category_total()[:1]+self.category_total()[2:])<amount:
            print("Amount inputted higher then current budget.")
            return exit()

    def add_expense(self, description, amount):
            Transaction(description, -1*amount, self)
            print("Expense added")

    def transfer(self,amount,transfer_from):
        transfer_from.add_balance("Transfer from "+self.name,amount)
        self.add_expense("Transfer to "+transfer_from.name, amount)


    '''def transactions_in_category(self):
        filter=[]
        for entry in Transaction.all:
            if entry.category==Category.all[self]:
                filter.append(entry)
        return filter'''

    def count_in_category(self):
        number_transaction=0
        for item in Transaction.all:
            if item.category==self:
                number_transaction+=1
        return number_transaction


    def category_total(self):
        total=0
        for entry in self.transactions_in_category():
            total=total+eval(entry.amount[0:1]+entry.amount[2:])
        if total<0:
            return "-${:.2f}".format(abs(total))
        else:
            return " ${:.2f}".format(abs(total))

    '''def category_total(self):
        total = 0
        for entry in Category.transactions_in_category(self):
            total = total + eval(entry.amount[0:1] + entry.amount[2:])
        if total < 0:
            return "-${:.2f}".format(abs(total))
        else:
            return " ${:.2f}".format(abs(total))'''

    @classmethod
    def expense_ranking(cls):
        category_expense={}
        for group in Category.all:
            expense=0
            for transaction in group.transactions_in_category():
                if eval(transaction.amount[0:1]+transaction.amount[2:])<0:
                    expense=expense+eval(transaction.amount[0:1]+transaction.amount[2:])
            category_expense[group]=expense
        high_to_low = sorted(category_expense.items(), key=lambda x: x[1])
        return [x[0] for x in high_to_low]

    def low_to_high_category(self):
        count={}
        for item in Transaction.all:
            if item.category not in count:
                count[item.category]=1
            else:
                count[item.category]=count[item.category]+1
        low_to_high_category = sorted(count.items(), key=lambda x: x[1])
        return low_to_high_category

    @classmethod
    def next_id(cls):
        return len(Category.all)+1

food_obj=Category("Food",1)
utility_obj=Category("Utility",2)
travel_obj=Category("Travel",3)

class Transaction:
    all=[]

    def __init__(self,description,amount,category):
        if amount<0:
            self.amount = '-${:.2f}'.format(abs(amount))
        else:
            self.amount=' ${:.2f}'.format(amount)
        self.description=description
        self.category=category
        Transaction.all.append(self)
        #Transaction.all.append((self.description, "${: .2f}".format(self.amount), self.description))

    @staticmethod
    def print_transactions(list):
        print((10 * "*" + " " + str(list[0].category)+ " Transacstions " + 10 * "*"))
        for transaction in list:
            print(transaction)

    def __repr__(self):
        #return f"{self.description} "+"${:.2f}".format(self.amount)+f" {self.category}"
        return f"{self.description,self.amount,self.category}"
gas_deposit=Transaction("deposit",1000,utility_obj)
bus_deposit=Transaction("deposit",1000,travel_obj)
food_deposit=Transaction("deposit",1000,food_obj)
grocery_obj=Transaction("grocery",-10,food_obj)
electricity_obj=Transaction("electricity",-20,utility_obj)
gas_obj=Transaction("gas",-14,utility_obj)
bus_obj=Transaction("bus",-2,travel_obj)
groc_obj=Transaction("groc",-4,food_obj)

#print(food_obj.id)
#print(Category.all[1])
#############################################################################################################
Category.system_response(Category.first_question(),Category.second_question())
