#include <iostream>

double calculateFare(double distance) {
    const double BASE_FARE = 200.0;
    const double COST_PER_KM = 50.0;
    return BASE_FARE + (distance * COST_PER_KM);
}

int main() {
    double distance;
    std::cout << "Enter distance in km: ";
    std::cin >> distance;

    double totalFare = calculateFare(distance);
    std::cout << "Total Fare: " << totalFare << " KES" << std::endl;
    
    return 0;
}