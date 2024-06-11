from model import *
import glm

class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object
        
        n_horizontal, n_vertical = 4, 20
        s = 2
        for x in range(n_horizontal):
            for z in range(n_vertical):
                add(StreetCube(app, pos=(x*s, -s, z*s), tex_id=0))

        # Add bicycle path
        bicycle_start = (n_horizontal)*s
        bicycle_width = 1
        bicycle_vertical = n_vertical
        for x in range(bicycle_width):
            for z in range(bicycle_vertical):
                add(ByciclePathCube(app, pos=((x*s)+bicycle_start, -s, z*s), tex_id=1))

        # Add buildings
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingRectangle(app, pos=(-s, building_pos_y, 3+s), scale=(1, 1, 1)))

        # Add shopping center
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + 4
        building_length = 3
        building_width = 20
        building_pos_x = n_horizontal * s + building_width / 2

        add(ShoppingCenterRectangle(app, pos=(building_pos_x-6, building_pos_y-1, building_length+6), scale=(1, 1, 1), rot=(0, 90, 0)))


    def destroy(self):
        for obj in self.objects:
            obj.destroy()

    def render(self):
        for obj in self.objects:
            obj.render()
