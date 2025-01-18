import pygame
from simulation import Simulation

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    simulation = Simulation(width=800, height=600)

    # Add entities to simulation
    simulation.add_entity("predator", 400, 300)
    simulation.add_entity("prey", 200, 150)
    simulation.add_entity("plant", 100, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        simulation.update()
        simulation.render(screen)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
