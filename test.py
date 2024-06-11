import pygame
import moderngl as mgl
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np
import glm

# Initialize Pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# ModernGL context
ctx = mgl.create_context()

# Define shaders
vertex_shader = """
#version 330
in vec3 position;
uniform mat4 mvp;

void main() {
    gl_Position = mvp * vec4(position, 1.0);
}
"""

fragment_shader = """
#version 330
out vec4 fragColor;

void main() {
    fragColor = vec4(1.0, 1.0, 1.0, 1.0);
}
"""

# Compile shaders
shader = ctx.program(
    vertex_shader=vertex_shader,
    fragment_shader=fragment_shader,
)

# Camera settings
projection = glm.perspective(glm.radians(45.0), width / height, 0.1, 1000.0)
view = glm.lookAt(glm.vec3(0, 0, 5), glm.vec3(0, 0, 0), glm.vec3(0, 1, 0))

# Initialize cubes
class Cube:
    def __init__(self, position):
        self.position = position

    def render(self):
        glUseProgram(shader)
        model = glm.mat4(1.0)
        model = glm.translate(model, self.position)
        mvp = projection * view * model
        glUniformMatrix4fv(glGetUniformLocation(shader, "mvp"), 1, GL_FALSE, glm.value_ptr(mvp))
        # Render cube (assuming you have cube rendering logic)

# Create cubes for the avenue
avenue = []
num_cubes = 10
spacing = 2.0
for i in range(num_cubes):
    avenue.append(Cube(glm.vec3(i * spacing - (num_cubes - 1) * spacing / 2, 0, 0)))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    # Render each cube in the avenue
    for cube in avenue:
        cube.render()

    pygame.display.flip()
    pygame.time.wait(10)
