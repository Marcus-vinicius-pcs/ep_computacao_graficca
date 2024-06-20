import glm
import pygame as pg

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.005
SENSITIVITY = 0.04

# Código feito com base no tutorial do vídeo referenciado no relatório
class Camera:
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def rotate(self):
        # Para habilitar rotação só descomentar o código abaixo
        # rel_x, rel_y = pg.mouse.get_rel()
        # self.yaw += rel_x * SENSITIVITY
        # self.pitch -= rel_y * SENSITIVITY
        # self.pitch = max(-89, min(89, self.pitch))
        # Posiciona a visão no centro da tela olhando de frente para a paisagem
        self.yaw = 91.63999999999989
        self.pitch = 1.4000000000000008

    def update_camera_vectors(self):
        # Essa função atualiza os vetores da câmera na medida que há movimentação da visão
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        # para habilitar movimentação com AWSD só comentar a linha 50 em que fixamos a posição da câmera
        self.position = glm.vec3(4.16832, 1.08734, -8.22933)
        self.move()
        self.rotate()
        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def move(self):
        # Habilita a movimentação da câmera
        velocity = SPEED * self.app.delta_time
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.position += self.forward * velocity
        if keys[pg.K_s]:
            self.position -= self.forward * velocity
        if keys[pg.K_a]:
            self.position -= self.right * velocity
        if keys[pg.K_d]:
            self.position += self.right * velocity
        if keys[pg.K_q]:
            self.position += self.up * velocity
        if keys[pg.K_e]:
            self.position += self.up * velocity

    def get_view_matrix(self):
        # Retorna a matriz de visão
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        # Retorna a matriz de projeção
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
