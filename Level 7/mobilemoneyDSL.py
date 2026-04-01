import re

class MobileMoneyDSL:
    def __init__(self, accounts):
        self.accounts = accounts  

    def execute(self, command):
        pattern = r"TRANSFER (\d+) FROM (\w+) TO (\w+) IF BALANCE > (\d+)"
        match = re.match(pattern, command)

        if not match:
            return "❌ Error: Invalid Syntax"

        amount = int(match.group(1))
        sender = match.group(2)
        receiver = match.group(3)
        threshold = int(match.group(4))

        # 3. Interpreter Logic & Validation
        if sender not in self.accounts:
            return f"❌ Error: Sender '{sender}' not found."
        
        current_balance = self.accounts[sender]

        if current_balance <= threshold:
            return f"🚫 Declined: Balance {current_balance} is not above threshold {threshold}."
        
        if current_balance < amount:
            return f"🚫 Declined: Insufficient funds for transfer."

        self.accounts[sender] -= amount
        self.accounts[receiver] = self.accounts.get(receiver, 0) + amount
        
        return (f"✅ Success! Transferred {amount} from {sender} to {receiver}. "
                f"New Balance: {self.accounts[sender]}")


db = {"Alice": 5000, "Bob": 200}
engine = MobileMoneyDSL(db)

print(engine.execute("TRANSFER 1000 FROM Alice TO Bob IF BALANCE > 1000"))


print(engine.execute("TRANSFER 500 FROM Bob TO Alice IF BALANCE > 1000"))