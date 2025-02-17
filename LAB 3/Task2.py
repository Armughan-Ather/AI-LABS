#Task2
from itertools import permutations

travel_costs = {
    'A': {'A': 0, 'B': 12, 'C': 18, 'D': 25},
    'B': {'A': 12, 'B': 0, 'C': 40, 'D': 22},
    'C': {'A': 18, 'B': 40, 'C': 0, 'D': 35},
    'D': {'A': 25, 'B': 22, 'C': 35, 'D': 0}
}

city_list = list(travel_costs.keys())
starting_city = 'A'
possible_routes = permutations([city for city in city_list if city != starting_city])

optimal_cost = float('inf')
optimal_route = []

for route in possible_routes:
    total_cost = 0
    current_city = starting_city

    for next_city in route:
        total_cost += travel_costs[current_city][next_city]
        current_city = next_city

    total_cost += travel_costs[current_city][starting_city]

    if total_cost < optimal_cost:
        optimal_cost = total_cost
        optimal_route = [starting_city] + list(route) + [starting_city]

print("Optimal Route:", " → ".join(optimal_route))
print("Optimal Route Cost:", optimal_cost)
