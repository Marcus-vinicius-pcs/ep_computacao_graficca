import pygame as pg
import moderngl as mgl
import glm

# Código feito com base no tutorial do vídeo referenciado no relatório
class Texture:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/asphalt.jpg')
        self.textures[1] = self.get_texture(path='textures/bycicle_path.jpg')
        self.textures[2] = self.get_texture(path='textures/glass_building.jpg')
        self.textures[3] = self.get_texture(path='textures/office_building.jpg')
        self.textures[4] = self.get_texture(path='textures/building_1.jpg')
        self.textures[5] = self.get_texture(path='textures/building_2.jpg')
        self.textures[6] = self.get_texture(path='textures/building_3.jpg')
        self.textures[7] = self.get_texture(path='textures/building_4.jpg')
        self.textures[8] = self.get_texture(path='textures/store_1.jpg')
        self.textures[9] = self.get_texture(path='textures/store_2.jpg')
        self.textures[10] = self.get_texture(path='textures/shopping.jpg')

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]