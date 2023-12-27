class Category:
    def __init__(self,name: str):
        self.ledger = []
        self.name = name 
        self.withdrawals = []

    def deposit(self, amount: float, description = ""):
        self.ledger.append({"amount":amount,
                            "description":description})
        return True

    def withdraw(self,amount: float, description = ""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({"amount":-1*amount,
                                "description":description})
            self.withdrawals.append({"amount":-1*amount,
                                "description":description})
            return True

    def get_balance(self):
        funds = 0
        for transaction in self.ledger:
            funds += transaction["amount"]
        return funds

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def transfer(self, amount, destination):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount,f"Transfer to {destination.name}")
            destination.deposit(amount,f"Transfer from {self.name}")
            return True

    def __repr__(self):
        stars = ""
        star_count = 30
        category_length = len(self.name)
        stars_on_each_side = ""
        for _ in range(int((star_count-category_length)/2)):
            stars_on_each_side += "*"
        stars = stars_on_each_side + self.name + stars_on_each_side
        dicvalues = []
        for i in self.ledger:
            value_list = []
            for _,values in i.items():
                value_list.append(str(values).strip())
            dicvalues.append(value_list)

        dummy = ""
        for i in dicvalues:
            i[0] = "{:.2f}".format(float(i[0]))
            length_description = len(i[1])
            length_quantity = len(i[0])
            if length_description > 23:
                length_description = 23
            spaces = ""
            length_spaces = int(star_count - length_description - length_quantity)
            for j in range(length_spaces):
                spaces += " "

            dummy += f"{i[1][0:length_description]}" + f"{spaces}" + f"{i[0]}" + "\n"

        total_spent = "Total: {:.2f}".format(self.get_balance())
        return f"{stars}\n{dummy}{total_spent}".strip()


def create_spend_chart(categories):
    withdrawal_amounts = {}
    total_spent = 0
    for category in categories:
        withdrawal_transactions = []
        for withdrawal in category.withdrawals:
            withdrawal_transactions.append(withdrawal["amount"])
        withdrawal_amounts[category.name] = (abs(sum(withdrawal_transactions)))
        total_spent += abs(sum(withdrawal_transactions))

    percentage_spent = {}
    for cats,amount_spent in withdrawal_amounts.items():
        percentage_spent[cats] = round((amount_spent/total_spent)*100)

    s = "Percentage spent by category\n"
    
    for n in range(100,-1,-10):
        s += f"{str(n)+'|':>4}"
        temp_s = ""
        for i, percent in enumerate(percentage_spent.values()):
            if (i == 0) and (percent >= n):
                temp_s += " o"
            elif (i == 0):
                temp_s += " " * 2
            if  (i > 0) and (percent >= n):
                temp_s += "  o"
            elif (i > 0):
                temp_s += " " * 3
        s += temp_s + "  "
        s += "\n"
    s += "    --"

    dummy = 0
    for _ in categories:
        if dummy == 0:
            s += "--"
            dummy += 1
        else:
            s += "---"

    s += "\n"

    list_categories = []
    for cats in percentage_spent.keys():
        list_categories.append(cats)

    length = max(len(word) for word in list_categories)
    modified_categories = []
    for cat in list_categories:
        while len(cat) < length:
            cat += " "
        modified_categories.append(cat)

    for i in range(length):
        s += " " * 5
        for word in modified_categories:
            s += f"{word[i]}  "
        s += "\n"
    s = s.strip()
    s += "  "
    return s

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([food, business,entertainment]))