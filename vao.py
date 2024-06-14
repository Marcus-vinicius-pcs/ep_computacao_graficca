from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # cube vao
        self.vaos['street_cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['street_cube'])
        
        # bycicle_path vao
        self.vaos['bycicle_path_cube'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['bycicle_path_cube'])
        
        self.vaos['building_rectangle'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['building_rectangle']
        )

        self.vaos['building_2_rectangle'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['building_2_rectangle']
        )

        self.vaos['shopping_rectangle'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['shopping_rectangle']
        )

        self.vaos['store_rectangle'] = self.get_vao(
            program=self.program.programs['default'],
            vbo = self.vbo.vbos['store_rectangle']
        )

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()