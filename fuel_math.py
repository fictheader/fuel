import math
import mathutils.geometry
from mathutils import Vector, Quaternion


def vec_distance(org, dst):
    acum = 0
    for num, el in enumerate(org):
        acum += (dst[num] - org[num]) * (dst[num] - org[num]) 
    return math.sqrt(acum)
        

def make_quat(axis_vec, degrees):
    from mathutils import Quaternion
    return Quaternion(axis_vec, math.radians(degrees))


def dot(vec1, vec2):
    return vec1.dot(vec2)


def cross(vec1, vec2): #order is V1 X V2
    return vec1.cross(vec2)


def sin(degrees):
    return  math.sin(math.radians(degrees))


def cos(degrees):
    return math.cos(math.radians(degrees))


def tan(degrees):
    return math.tan(math.radians(degrees))


def asin(ratio):
    return math.degrees(math.asin(ratio))


def acos(ratio):
    return math.degrees(math.acos(ratio))


def atan(ratio):
    return math.degrees(math.atan(ratio))


def pivotx(vec, degrees): 
    return (vec[0], cos(degrees) * vec[1] - sin(degrees) * vec[2], sin(degrees) * vec[1] + cos(degrees) * vec[2])


def pivoty(vec, degrees): 
    return (cos(degrees) * vec[0] + sin(degrees) * vec[2], vec[1], -sin(degrees) * vec[0] * cos(degrees) * vec[2])


def pivotz(vec, degrees): 
    return (cos(degrees) * vec[0] - sin(degrees) * vec[1], sin(degrees) * vec[0] + cos(degrees) * vec[1], vec[2])


def pivot_around_vec(vec, axis_vec_origin, axis_vec_target, degrees):
    q = Quaternion(Vector(axis_vec_target - axis_vec_origin), math.radians(degrees))
    base_vec = vec - axis_vec_origin
    base_vec.rotate(q)
    return base_vec + axis_vec_origin

    
def get_lookat_matrix(direction_vec, origin_vec, up_vec= (0, 0, 1)):
    import bgl
    return bgl.gluLookAt(direction_vec[0], direction_vec[1], direction_vec[2], origin_vec[0], origin_vec[1], origin_vec[2], up_vec[0], up_vec[1], up_vec[2])

