class PricingEngine:
    def __init__(self, base_fare=200, cost_per_km=50):
        self.base_fare = base_fare
        self.cost_per_km = cost_per_km

    def calculate_total(self, distance):
        return self.base_fare + (distance * self.cost_per_km)


nairobi_engine = PricingEngine()
distance_input = 200
print(f"Total Fare (OOP): {nairobi_engine.calculate_total(distance_input)} KES")