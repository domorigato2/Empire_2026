# Save as fcc_budget.py in C:\Users\sheil\Empire_2026\

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category_object):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category_object.name}")
            category_object.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

if __name__ == "__main__":
    print("\n" + "="*50)
    print(" FREECODECAMP BUDGET APP ENGINE")
    print("="*50)
    
    war_chest = Category("War_Chest")
    war_chest.deposit(4.32, "Initial PayPal Balance")
    war_chest.withdraw(4.50, "BPART Transit Toll (Pending)")
    
    print(war_chest)
    print("="*50 + "\n")