Ecosystem Simulation
Description

This project is a dynamic simulation of predator-prey interactions within an evolving ecosystem. The simulation features entities like predators, prey, plants, and food sources. Using neural networks, the creatures make decisions based on their vision and surroundings, evolving over time through natural selection. The ecosystem constantly adapts as creatures' behaviors and interactions change, ensuring that only the most adaptive creatures survive.
Features
Predator-Prey Dynamics

    Predators and Prey:
        Predators need to consume prey to survive. When hunger levels are not satisfied, they actively pursue prey within their vision.
        Prey primarily prioritize plants as their food source. If plants are unavailable, they turn to food left on the ground.
        If two prey have enough energy, they reproduce, creating new offspring with similar neural weights, subject to mutations.
    Reproduction:
        Both predators and prey reproduce under favorable conditions. Reproduction depletes energy reserves, emphasizing strategic behavior.
        Predators reproduce after consuming enough food or prey, adding pressure on the prey population.
    Energy Costs:
        Predators move faster, consuming more energy. This behavior makes them rely on efficient hunting strategies.
        Prey conserve energy by moving cautiously and defending themselves only when attacked.

Plant Growth and Clustering

    Random Growth: Plants randomly spawn in the ecosystem, with a higher probability of appearing near existing plants, resulting in clusters.
    Growth Dynamics:
        Individual plants grow slowly to a maximum size.
        If a plant is partially eaten, it regenerates faster compared to respawning entirely.
        Clusters can expand to fill large sections of the ecosystem over time, regulating the prey population.

Neural Networks for Decision-Making

    Creatures use neural networks to process sensory data from their vision and decide their actions (e.g., movement, chasing, feeding).
    The neural networks evolve over time:
        Weights and biases change with mutations during reproduction.
        Favorable traits persist through natural selection, optimizing behavior over generations.

Vision-Based Behavior

    Creatures rely on raycasting for vision. Rays detect nearby entities (e.g., prey, plants, food) and prioritize actions based on importance:
        Prey prioritize plants, followed by food, and avoid predators.
        Predators focus on stationary food first and actively chase prey if their hunger persists.
    Vision data guides neural network inputs, enabling creatures to adapt to their environment.

Energy Management

    Movement, vision, and reproduction consume energy.
    Energy is replenished by consuming food (plants for prey, prey for predators).
    Creatures with efficient energy use are more likely to survive and reproduce.

Installation

Clone the repository to your local machine:

git clone git@github.com:BurakErdilli/ecosystem-simulation.git

Navigate to the project directory:

cd ecosystem-simulation

Install the required dependencies:

pip install -r requirements.txt

Running the Simulation

To run the simulation using Pygame:

python main.py

Requirements

    Python 3.9+
    Pygame: For rendering and simulation visualization.
    NumPy: For mathematical computations and efficient array handling.
    TensorFlow/PyTorch: For implementing neural networks (choose based on your preference).
    Raycasting Module: Custom implementation for vision mechanics.

Contributing

We welcome contributions to enhance the simulation, including:

    Optimizations for performance and scalability.
    Improvements to creature behaviors and evolution mechanics.
    New features like environmental effects or additional entity types.

To contribute:

    Fork this repository.
    Create a new branch for your feature: git checkout -b feature-name.
    Commit your changes: git commit -m "Add feature-name".
    Push to the branch: git push origin feature-name.
    Submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

    Pygame: For making 2D rendering simple and efficient.
    NumPy: For enabling quick calculations.
    AI and Evolutionary Biology Concepts: For inspiring the simulation design.
