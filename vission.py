import math
from utils import intersects,calculate_distance

class Vision:
    def __init__(self, fov, num_rays, range):
        self.fov = fov
        self.num_rays = num_rays
        self.range = range

    def generate_rays(self, x, y, angle):
        rays = []
        angle_step = self.fov / (self.num_rays - 1)
        for i in range(self.num_rays):
            ray_angle = math.radians(angle - self.fov / 2 + i * angle_step)
            dx = math.cos(ray_angle) * self.range
            dy = math.sin(ray_angle) * self.range
            rays.append(((x, y), (x + dx, y + dy)))
        return rays

    def process_rays(self, rays, objects):
        zones = []
        for ray in rays:
            closest_object = None
            closest_distance = float("inf")
            for obj in objects:
                if intersects(ray, obj):  # Custom intersection check
                    dist = calculate_distance(ray[0], obj.position)
                    if dist < closest_distance:
                        closest_object = obj
                        closest_distance = dist
            zones.append((closest_object, closest_distance))
        return zones
