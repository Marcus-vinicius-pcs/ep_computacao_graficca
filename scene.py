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

        # Add bicycle path
        bicycle_start = (n_horizontal)
        bicycle_width = 1
        bicycle_vertical = n_vertical
        for x in range(bicycle_width):
            for z in range(bicycle_vertical):
                add(ByciclePathCube(app, pos=((x*s)+bicycle_start, -s, z*s), tex_id=1))

        for x in range(n_horizontal+1):
            for z in range(n_vertical):
                add(StreetCube(app, pos=(x*s, -s, z*s), tex_id=0))

        # Add buildings
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingRectangle(app, pos=(-s-0.5, building_pos_y, 3+s), scale=(1, 1, 1), tex_id=3))

        # Add buildings
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingRectangle(app, pos=(-s-0.5, building_pos_y+0.75, s), scale=(1, 1.2, 1.2), tex_id=6))

        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingRectangle(app, pos=(-s+12, building_pos_y, 18.5+s), scale=(1, 1, 1), tex_id=3))

        # Add FIESP body
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingFIESPbody(app, pos=(-s-1, building_pos_y, 18.5+s), scale=(1, 1, 1), tex_id=3))

        # Add FIESP nose
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingFIESP(app, pos=(-s+1, building_pos_y, 18.5+s), scale=(1, 1, 1), tex_id=2))

        # Add store
        building_height = 8
        building_pos_y = -s + 4
        building_length = 3
        building_width = 20
        building_pos_x = n_horizontal * s + building_width / 2

        add(StoreRectangle(app, pos=(-s-1.5, building_pos_y-2, building_length+8.5), scale=(1, 1, 1), rot=(0, 90, 0), tex_id=8))

        # Add buildings
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingRectangle(app, pos=(-s-0.5, building_pos_y+2, 25+s), scale=(1, 1.5, 1.8), tex_id=7))

        # Add buildings
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingRectangle(app, pos=(-s-0.5, building_pos_y, 29+s), scale=(1, 1, 1), tex_id=4))

        # Add buildings
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(BuildingRectangle(app, pos=(-s-0.5, building_pos_y-1, 34+s), scale=(1, 0.75, 3), tex_id=5))

        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + building_height / 2
        add(Building2Rectangle(app, pos=(-s+13, building_pos_y, 24+s), scale=(1, 1, 1), tex_id=6))

        # Add shopping center
        building_height = 8  # Altura do paralelepípedo
        building_pos_y = -s + 4
        building_length = 3
        building_width = 20
        building_pos_x = n_horizontal * s + building_width / 2

        add(BuildingRectangle(app, pos=(building_pos_x-7, building_pos_y-0.5, building_length+6), scale=(1, 1, 1), rot=(0, 0, 0), tex_id=5))
        add(BuildingRectangle(app, pos=(building_pos_x-7, building_pos_y-0.5, building_length+3), scale=(1, 1, 1), rot=(0, 0, 0), tex_id=4))
        add(Building2Rectangle(app, pos=(building_pos_x-7, building_pos_y, 12+s), scale=(1, 1, 1), tex_id=6))
        # Add store
        building_height = 8
        building_pos_y = -s + 4
        building_length = 3
        building_width = 20
        building_pos_x = n_horizontal * s + building_width / 2

        add(StoreRectangle(app, pos=(building_pos_x-6.5, building_pos_y-2, building_length+31.5), scale=(1, 1, 1), rot=(0, 270, 0), tex_id=9))

    def destroy(self):
        for obj in self.objects:
            obj.destroy()

    def render(self):
        for obj in self.objects:
            obj.render()
