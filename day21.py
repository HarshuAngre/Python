"""import math

class Statistics:
    def __init__(self,data):
        self.data = sorted(data)

    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return self.sum() / self.count()
    
data = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27,
        24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24,
        33, 29, 26]

statistic = Statistics(data)

print("count: ", statistic.count())
print("sum: ", statistic.sum())
print("min: ", statistic.min())
print("max: ", statistic.max())
print("range: ", statistic.range())
print("Mean: ", statistic.mean())"""


class PersonAccount:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.income = {}
        self.expenses = {}

    def add_income(self,description,Amount):
        self.income[description] = self.income.get(description,0)+ Amount

    def add_expenses(self,description,Amount):
        self.expenses[description] = self.expenses.get(description,0)+ Amount

    def total_income(self):
        return sum(self.income.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"name: {self.firstname} {self.lastname}")
        print("\nincomes:")
        for desc,Amount in self.income.items():
            print(f"  {desc}: ${Amount}")
    
        print("\nexpenses:")
        for desc,Amount in self.expenses.items():
            print(f"  {desc}: ${Amount}")
    
        print(f"\nTotal Income: ₹{self.total_income()}")
        print(f"Total Expense: ₹{self.total_expense()}")
        print(f"Account Balance: ₹{self.account_balance()}")

person = PersonAccount("Harshu", "Angre")

person.add_income("Salary", 50000)
person.add_income("Freelancing", 10000)
person.add_income("Interest", 2000)

person.add_expenses("Rent", 15000)
person.add_expenses("Food", 6000)
person.add_expenses("Internet", 1000)

person.account_info()
