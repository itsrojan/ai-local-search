import random

# Genetic Algorithm Parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
MAX_GENERATIONS = 1000

# Fitness Function: Calculate the number of non-attacking pairs of queens.
def fitness(individual):
    non_attacking_pairs = 0
    n = len(individual)
    for i in range(n):
        for j in range(i + 1, n):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i - j):
                non_attacking_pairs += 1
    return non_attacking_pairs

# Generate initial population
def initialize_population(size, n=8):
    return [random.sample(range(n), n) for _ in range(size)]

# Selection: Choose the best individuals to form the next generation
def selection(population, fitness_scores):
    selected = random.choices(
        population, weights=fitness_scores, k=len(population)//2
    )
    return selected

# Crossover: Perform crossover between two parents to create offspring
def crossover(parent1, parent2):
    n = len(parent1)
    crossover_point = random.randint(0, n - 1)
    child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    return child

# Mutation: Randomly change one gene in the individual
def mutate(individual, mutation_rate=0.1):
    if random.random() < mutation_rate:
        n = len(individual)
        i, j = random.sample(range(n), 2)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

# Genetic Algorithm to solve the Eight Queens problem
def genetic_algorithm():
    population = initialize_population(POPULATION_SIZE)
    n = len(population[0])

    for generation in range(MAX_GENERATIONS):
        # Evaluate fitness of each individual
        fitness_scores = [fitness(individual) for individual in population]

        # Check if a solution is found
        if n * (n - 1) // 2 in fitness_scores:
            solution = population[fitness_scores.index(n * (n - 1) // 2)]
            print(solution)
            return

        # Selection
        selected_individuals = selection(population, fitness_scores)

        # Create next generation through crossover and mutation
        next_generation = []
        while len(next_generation) < POPULATION_SIZE:
            parent1, parent2 = random.sample(selected_individuals, 2)
            child = crossover(parent1, parent2)
            child = mutate(child, MUTATION_RATE)
            next_generation.append(child)

        population = next_generation

    print("No result found")

# Run the Genetic Algorithm
genetic_algorithm()