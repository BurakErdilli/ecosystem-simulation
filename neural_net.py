import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_hidden = np.zeros(hidden_size)
        self.bias_output = np.zeros(output_size)

    def forward(self, inputs):
        hidden = np.tanh(np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        output = np.tanh(np.dot(hidden, self.weights_hidden_output) + self.bias_output)
        return output
