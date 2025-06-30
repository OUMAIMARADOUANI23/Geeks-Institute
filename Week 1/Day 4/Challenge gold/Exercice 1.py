import random
class Gene:
    def __init__(self, value=None):
        self.value = random.choice([0, 1]) if value is None else value

    def mutate(self):
        if random.random() < 0.5:
            self.value = 1 - self.value

    def __repr__(self):
        return str(self.value)

class Chromosome:
    def __init__(self, genes=None):
        self.genes = [Gene() for _ in range(10)] if genes is None else genes

    def mutate(self):
        for gene in self.genes:
            gene.mutate()

    def is_full_of_ones(self):
        return all(g.value == 1 for g in self.genes)

    def __repr__(self):
        return ''.join(str(g) for g in self.genes)

class DNA:
    def __init__(self, chromosomes=None):
        self.chromosomes = [Chromosome() for _ in range(10)] if chromosomes is None else chromosomes

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_full_of_ones(self):
        return all(chromo.is_full_of_ones() for chromo in self.chromosomes)

    def __repr__(self):
        return '\n'.join(str(chromo) for chromo in self.chromosomes)

class Organism:
    def __init__(self, dna=None, environment=0.5):
        self.dna = DNA() if dna is None else dna
        self.environment = environment 

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()

    def is_perfect(self):
        return self.dna.is_full_of_ones()

    def __repr__(self):
        return str(self.dna)

def evolve_to_perfection(environment=0.8, max_generations=100000):
    generation = 0
    organism = Organism(environment=environment)
    while not organism.is_perfect() and generation < max_generations:
        organism.mutate()
        generation += 1
    if organism.is_perfect():
        print(f"\n✨ Organism reached perfect DNA (all 1s) in {generation} generations!")
    else:
        print(f"\n❌ Pas d’ADN parfait après {max_generations} générations.")
    return generation


if __name__ == "__main__":
    print("Test démarrage programme")
    g = evolve_to_perfection(environment=1.0)
    print("Générations nécessaires :", g)
