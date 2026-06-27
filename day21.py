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
print("Mean: ", statistic.mean())


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

person.account_info()"""




"""
import requests
from bs4 import BeautifulSoup
import json

url = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

data = {}

for section in soup.find_all(["section","div"]):
    heading = section.find(["h2","h3"])
    if heading:
        stats = {}

        for items in section.find_all("li"):
            text = items.get_text(" ", strip=True)
            if text:
                stats[f"item_{len(stats)+1}"] = text
        
        if stats:
            data[heading.get_text(strip=True)] = stats


with open("bu_facts_stats.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

print("Data successfully saved to bu_facts_stats.json")"""


"""import requests
from bs4 import BeautifulSoup
import json

url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

tables = soup.find_all("tables")

table = tables[5]

headers = []

header_row = table.find("tr")
for th in header_row.find_all(["th", "td"]):
    headers.append(th.text(strip=True))

data = []

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")

    if len(row) == len(headers):
        row_data = {}

        for i in range(len(headers)):
            row_data[headers[i]] = cols[i].get_text(" ", strip=True)
        data.append(row_data)

with open("uci_datasets.json", "w", encoding="utf-8") as file:
    json.dump(data,file,indent=4)

print("Data saved to uci_datasets.json")"""


"""import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

# Get webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the first wikitable (Presidents table)
table = soup.find("table", class_="wikitable")

# Get column headers
headers = []
header_row = table.find("tr")

for th in header_row.find_all("th"):
    header = th.get_text(" ", strip=True)
    headers.append(header)

# Extract rows
presidents = []

for row in table.find_all("tr")[1:]:
    cols = row.find_all(["td", "th"])

    # Skip incomplete rows
    if len(cols) < len(headers):
        continue

    president = {}

    for i in range(len(headers)):
        president[headers[i]] = cols[i].get_text(" ", strip=True)

    presidents.append(president)

# Save as JSON
with open("us_presidents.json", "w", encoding="utf-8") as file:
    json.dump(presidents, file, indent=4, ensure_ascii=False)

print("Data saved to us_presidents.json")"""