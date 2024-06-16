import glm

class Light:
    def __init__(self, position=(50, 50, -10), color=(1, 1, 1), direction=(0, 0, 0)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(direction)  # Adjust this to point to your avenue
        # intensities
        self.Ia = 0.06 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1.0 * self.color  # specular
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))
    
    
    def get_color(self):
        return self.color
    

    def get_position(self):
        return self.position
    

    def update_light_position(self, position):
        self.positon = glm.vec3(position)


    def update_light_color(self, color):
        self.color = glm.vec3(color)