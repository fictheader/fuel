#TODO Need a design changing maybe..

#TODO Add to next version

import bpy
import bgl


def load_image_to_preview(icon_name, file_path):
    pcoll = bpy.utils.previews.new()
    pcoll.load(icon_name, file_path, 'IMAGE')
    return pcoll


def get_preview_image_size(pcoll_image):
    return pcoll_image.image_size


def get_preview_image_pixels(pcoll_image):
    return pcoll_image.image_pixels


class Image2D(): #TODO
    def get_width():
        pass

    def get_height():
        pass

    def load(self, icon_name, file_path):
        def load_image_to_preview(icon_name, file_path):
            pcoll = bpy.utils.previews.new()
            pcoll.load(icon_name, file_path, 'IMAGE')
            return pcoll

        def make_rgba_array(image_pixels):
            rgba = []
            for pix in image_pixels:
                a = (pix >> 24) & 255
                r = (pix >> 16) & 255
                g = (pix >> 8) & 255
                b = pix & 255
                rgba.append(r)
                rgba.append(g)
                rgba.append(b)
                rgba.append(a)
            return rgba

        texture = bgl.Buffer(bgl.GL_INT, 1)
        bgl.glGenTextures(1, texture)
        self.id = texture[0]
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.id)
        bgl.glPixelStore(bgl.GL_UNPACK_ALIGNMENT, 4)
        bgl.glTexImage2D(bgl.GL_TEXTURE_2D, 0, bgl.GL_RGBA, self.width, self.height, 0, bgl.GL_RGBA, bgl.GL_UNSIGNED_BYTE, rgba)
        bgl.glTexParametri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MAG_FILTER, bgl.GL_NEREST)
        bgl.glTexParametri(bgl.GL_TEXTURE_2D, bgl.GL_TEXTURE_MIN_FILTER, bgl.GL_NEREST)

    def bind(self):
        bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.id)

    def __init__(self, file_path):
        self.id = None
        self.width = get_width()
        self.height = get_height()

    def __dell__(self):
        if self.id:
            texture = bgl.Buffer(bgl.GL_INT, 1)
            texture[0] = self.id
            bgl.glBindTexture(bgl.GL_TEXTURE_2D, self.id)
            bgl.glDeleteTextures(1, texture)
            self.id = None

        
def get_image_width(image):
    return image.size[0]


def get_image_height(image):
    return image.size[1]


def load_image_to_data(file_path):
    image = bpy.data.images.load(file_path)
    image.gl_load(0, bgl.GL_NEREST, bgl.GL_NEREST)
    return image


def remove_image_from_data(image):
    image.user_clear()
    image.gl_free()
    bpy.data.images.remove(image)


def bind_image(image):
    bgl.glBindTexture(bgl.GL_TEXTURE_2D, image.bindcode[0])


def draw_image_data(file_path, center_coord):

    bgl.glEnable(bgl.GL_BLEND)
    bgl.glEnable(bgl.GL_TEXTURE_2D)

    image  = load_image_to_data(file_path)
    width = get_image_width(image)
    height = get_image_height(image)

    top_left = (center_coord[0] - width/2, center_coord[1] - height/2)
    top_right = (center_coord[0] + width/2, center_coord[1] - height/2)
    bottom_right = (center_coord[0] + width/2, center_coord[1] + height/2)
    bottom_left = center_coord(0 - width/2, center_coord[1] + height/2)

    bind_image(image)
    
    bgl.glBegin(bgl.GL_QUADS)
    bgl.glTexCoord2f(0.0, 0.0)
    bgl.glVertex2f(*top_left)

    bgl.glTexCoord2f(1.0, 0.0)
    bgl.glVertex2f(*top_right)

    bgl.glTexCoord2f(1.0, 1.0)
    bgl.glVertex2f(*bottom_right)

    bgl.glTexCoord2f(0.0, 1.0)
    bgl.glVertex2f(*bottom_left)
    bgl.glEnd()

    bgl.glDisable(bgl.GL_TEXTURE_2D)
    bgl.glDisable(bgl.GL_BLEND)


