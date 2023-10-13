#for number 2 of the assignment

import random

# Define the graph
G = {
    "a": [("b", 12), ("c", 4), ("d", 999), ("e", 999), ("f", 999), ("g", 12)],
    "b": [("a", 12), ("c", 8), ("d", 12), ("e", 999), ("f", 999), ("g", 999),],
    "c": [("a", 10), ("b", 8), ("d", 11), ("e", 3), ("f", 999), ("g", 9)],
    "d": [("a", 999), ("b", 12), ("c", 11), ("e", 11), ("f", 10), ("d", 999)],
    "e": [("a", 999), ("b", 999), ("c", 3), ("d", 11), ("g", 7), ("f", 6)],
    "f": [("a", 999), ("b", 999), ("c", 999), ("d", 10), ("e", 6), ("f", 9)],
    "g": [("a", 12), ("b", 999), ("c", 9), ("d", 999), ("e", 7), ("f", 9)]
}
#nodes that aren't connected to a specific node are given the weight 999 with that node to avoid errors

# Define parameters
population_size = 100
generations = 200
initial_mutation_rate = 0.5

def create_individual():
    nodes = list(G.keys())
    nodes.remove("a")
    random.shuffle(nodes)
    return ['a'] + nodes

def calculate_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        current_node = route[i]
        next_node = route[i + 1]
        for neighbor, distance in G[current_node]:
            if neighbor == next_node:
                total_distance += distance
                break

    last_node = route[-1]
    for neighbor, distance in G[last_node]:
        if neighbor == route[0]:
            total_distance += distance
            break

    return total_distance

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + [node for node in parent2 if node not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [node for node in parent1 if node not in parent2[:crossover_point]]
    return child1, child2

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(1, len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

population = set()
for i in range(population_size):
    while True:
        individual = tuple(create_individual())
        if individual not in population:
            population.add(individual)
            break

best_route = None
best_distance = float('inf')
mutation_rate = initial_mutation_rate

for generation in range(generations):
    new_population = set()

    for j in range(population_size):
        parent1, parent2 = random.sample(population, 2)
        child1, child2 = crossover(list(parent1), list(parent2))
        child1 = mutate(list(child1), mutation_rate)
        child2 = mutate(list(child2), mutation_rate)
        new_population.add(tuple(child1))
        new_population.add(tuple(child2))

    population = new_population
    current_best_route = min(population, key=lambda x: calculate_distance(list(x)))
    current_best_distance = calculate_distance(list(current_best_route))

    if current_best_distance < best_distance:
        best_route = current_best_route
        best_distance = current_best_distance

    mutation_rate *= 0.95

if best_route:
    best_distance = calculate_distance(list(best_route))
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
else:
    print("No valid routes found in the population.")