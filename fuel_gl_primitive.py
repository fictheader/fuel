import bgl
import bpy
import blf


#FORMAT start, end : (0, 0, 0)
def draw_line(start, end, cl = (0, 0, 0, 1), width = 1.0):

    bgl.glBegin(bgl.GL_LINES)
    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)
    bgl.glVertex3f(*start)
    bgl.glVertex3f(*end)
    bgl.glEnd()


#FORMAT verts : [(0, 0, 0), (1, 1, 1)...]
def draw_line_strip(verts, cl = (0, 0, 0, 1), width = 1.0):

    for n in range(len(verts) - 1):
        draw_line(verts[n], verts[n + 1], cl, width)


#FORMAT verts : [(0, 0, 0), (1, 1, 1), (2, 2, 2)...]
def draw_line_loop(verts, cl = (0, 0, 0, 1), width = 1.0):

    for n in range(len(verts) - 1):
        draw_line(verts[n], verts[n + 1], cl, width)
    draw_line(verts[len(verts) - 1], verts[0], cl, width)


#FORMAT triangle : [(0, 0, 0), (1, 1, 1), (2, 2, 2)]
def draw_triangle(triangle, cl = (0, 0, 0, 1), width = 1.0):
                
    bgl.glBegin(bgl.GL_TRIANGLES)
    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)
    bgl.glVertex3f(*triangle[0])
    bgl.glVertex3f(*triangle[1])
    bgl.glVertex3f(*triangle[2])
    bgl.glEnd()


#FORMAT triangles : [[(0, 0, 0), (1, 1, 1), (2, 2, 2)], [(3, 3, 3), (4, 4, 4), (5, 5, 5)]...]
def draw_triagnles(triangles, cl = (0, 0, 0, 1), width = 1.0):

    for triangle in triangles:
        draw_triangle(triangle, cl, width)


#FORMAT triangle_strip: [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)...]
def draw_triangle_strip(triangle_strip, cl = (0, 0, 0, 1), width = 1.0):    
    
    bgl.glBegin(bgl.GL_TRIANGLE_STRIP)
    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)
    for vert in triangle_strip:
        bgl.glVertex3f(*vert)
    bgl.glEnd()


#FORAMT start_vert : (0, 0, 0)
#       other_verts : [(1, 1, 1), (2, 2, 2), (3, 3, 3)...]
def draw_triangle_fan(start_vert, other_verts, cl = (0, 0, 0, 1), width = 1.0):

    bgl.glBegin(bgl.GL_TRIANGLE_FAN)
    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)
    bgl.glVertex3f(*start_vert)
    for vert in other_verts:
        bgl.glVertex3f(*vert)
    bgl.glEnd()


#FORMAT quad : [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3)]
def draw_quad(quad, cl = (0, 0, 0, 1), width = 1.0):
    
    bgl.glBegin(bgl.GL_QUADS)
    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)
    for vert in quad:
        bgl.glVertex3f(*vert)
    bgl.glEnd()


#FORMAT quads : [[(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3)], [(4, 4, 4), (5, 5, 5), (6, 6, 6), (7, 7, 7)]...]
def draw_quads(quads, cl = (0, 0, 0, 1), width = 1.0):

    for quad in quads:
        draw_quad(quad, cl, width)
        

#FORMAT vertical_edges : [[(0, 0, 0), (1, 1, 1)], [(2, 2, 2), (3, 3, 3)]...]
def draw_quad_strip(vertical_edges, cl = (0, 0, 0, 1), width = 1.0):

    bgl.glBegin(bgl.GL_QUAD_STRIP)
    for vertical_edge in vertical_edges:
        bgl.glVertex3f(*vertical_edge[0])
        bgl.glVertex3f(*vertical_edge[1])
    bgl.glEnd()


#FORMAT polygon : [(0, 0 ,0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)...]
def draw_polygon(polygon, cl = (0, 0, 0, 1), width = 1.0):

    bgl.glBegin(bgl.GL_POLYGON)
    for vert in polygon:
        bgl.glVertex3f(*vert)
    bgl.glEnd()


def draw_circle_2d(origin, radius, points, cl = (0, 0, 0, 1), width = 1.0):
    degrees = float(360.0/points)
    point_list = [(origin[0] + radius * math.cos(math.radians(n * degrees)), origin[1] + radius * math.sin(math.radians(n * degrees))) for n in range(point_list)]
    
    bgl.glEnable(bgl.GL_BLEND)
    bgl.glBegin(bgl.GL_LINES)

    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)

    for n in range(len(point_list)):
        bgl.glVertex2f(*point_list[n % len(point_list)])
        bgl.glVertex2f(*point_list[(n + 1) % len(point_list)])

    bgl.glEnd()
    bgl.glDisable(bgl.GL_BLEND)


#FORMAT quad2d : [(0, 0), (1, 1), (2, 2), (3, 3)] 
def draw_quad_2d(quad2d, cl = (0, 0, 0, 1), width = 1.0):
    
    bgl.glBegin(bgl.GL_QUADS)

    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)

    for vert in quad2d:
        bpl.glVertex2f(*vert)
    bgl.glEnd()


#FORMAT top_left : (0, 0), bottom_right : (1, 1)
def draw_rect_2d_1(top_left, bottom_right, cl = (0, 0, 0, 1), width = 1.0):
    
    top_right = (bottom_right[0], top_left[1])
    bottom_left = (top_left[0], bottom_right[1])

    bgl.glBegin(bgl.GL_QUADS)

    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)

    bgl.glVertex2f(*top_left)
    bgl.glVertex2f(*top_right)
    bgl.glVertex2f(*bottom_right)
    bgl.glVertex2f(*bottom_left)
    bgl.glEnd()

#FORMAT center : (0, 0), width : 1, height 1
def draw_rect_2d_2(center = (0, 0), rect_width = 1, rect_height = 1, cl = (0, 0, 0, 1), width = 1.0):

    top_left = (center[0] - rect_width/2, center[1] - rect_height/2)
    top_right = (center[0] + rect_width/2, center[1] - rect_height/2)
    bottom_right = (center[0] + rect_width/2, center[1] + rect_height/2)
    bottom_left = (center[0] - rect_width/2, center[1] + rect_height/2)

    bgl.glBegin(bgl.GL_QUADS)

    bgl.glLineWidth(width)
    bgl.glColor4f(*cl)

    bgl.glVertex2f(*top_left)
    bgl.glVertex2f(*top_right)
    bgl.glVertex2f(*bottom_right)
    bgl.glVertex2f(*bottom_left)
    bgl.glEnd()


