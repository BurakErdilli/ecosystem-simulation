import numpy as np
from neural import NeuralNetwork

class GeneticAlgorithm:
    def __init__(self, mutation_rate=0.1, crossover_rate=0.5):
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate

    def calculate_fitness(self, entities):
        return [entity.health + entity.energy for entity in entities]

    def mutate(self, neural_net):
        for weight in neural_net.weights_input_hidden.flatten():
            if np.random.rand() < self.mutation_rate:
                weight += np.random.randn() * 0.1
        return neural_net

    def crossover(self, parent1, parent2):
        child = NeuralNetwork(parent1.input_size, parent1.hidden_size, parent1.output_size)
        child.weights_input_hidden = (parent1.weights_input_hidden + parent2.weights_input_hidden) / 2
        return child
