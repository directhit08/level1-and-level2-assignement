class Patient:
    def __init__(self, name, policy_number):
        self.name = name
        self.policy_number = policy_number

    def calculate_claim(self, amount):
        return amount * 0.90